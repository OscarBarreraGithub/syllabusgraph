from copy import deepcopy
from pathlib import Path
import runpy

import pytest

from syllabusgraph.io import ProjectError, digest, write_yaml
from syllabusgraph.project import load_project, validate_knowledge

inspect_bank = runpy.run_path(
    str(Path(__file__).resolve().parents[1] / 'scripts/check_graph_bank.py')
)['inspect_bank']


def book_project(root, sample, identity):
    config = deepcopy(sample.config)
    config.update(id=identity, sources=[{k: v for k, v in s.items() if k != 'public_file'}
                                       for s in config['sources']])
    write_yaml(root / 'project.yaml', config)
    write_yaml(root / config['knowledge'], sample.knowledge)
    write_yaml(root / 'review.yaml', {
        'status': 'partial-model-reviewed', 'graph_digest': digest(sample.knowledge)
    })
    return load_project(root)


def save_reviewed_graph(project):
    write_yaml(project.root / project.config['knowledge'], project.knowledge)
    write_yaml(project.root / 'review.yaml', {
        'status': 'partial-model-reviewed', 'graph_digest': digest(project.knowledge)
    })


def test_book_graph_needs_no_plans_or_private_sources(tmp_path, sample):
    project = book_project(tmp_path / 'textbooks/book', sample, 'book')
    assert not project.plans
    assert project.nodes
    assert not project.local.exists()
    assert inspect_bank(tmp_path)['projects']['book']['plans'] == 0


def test_origin_shape_and_resolution(tmp_path, sample):
    book = book_project(tmp_path / 'textbooks/book', sample, 'book')
    other = book_project(tmp_path / 'textbooks/other', sample, 'other')
    subject = book_project(tmp_path / 'subjects/topic', sample, 'topic')
    node = subject.knowledge['nodes'][0]
    node['origins'] = [
        {'project': p.config['id'], 'node': node['id'], 'note': 'Same bounded concept.'}
        for p in (book, other)
    ]
    save_reviewed_graph(subject)
    report = inspect_bank(tmp_path)
    assert report['overlap'][0]['books'] == ['book', 'other']
    assert report['overlap'][0]['count'] == 1
    node['origins'][0]['node'] = 'missing-node'
    save_reviewed_graph(subject)
    with pytest.raises(ProjectError, match='Unknown origin'):
        inspect_bank(tmp_path)
    node['origins'][0].pop('note')
    with pytest.raises(ProjectError, match='note'):
        validate_knowledge(subject.config, subject.knowledge)


def test_bank_rejects_ambiguous_project_identity(tmp_path, sample):
    book_project(tmp_path / 'textbooks/first', sample, 'same')
    book_project(tmp_path / 'textbooks/second', sample, 'same')
    with pytest.raises(ProjectError, match='Duplicate bank project'):
        inspect_bank(tmp_path)


def test_bank_rejects_stale_review(tmp_path, sample):
    project = book_project(tmp_path / 'textbooks/book', sample, 'book')
    project.knowledge['nodes'][0]['summary'] = 'An unreviewed replacement.'
    write_yaml(project.root / project.config['knowledge'], project.knowledge)
    with pytest.raises(ProjectError, match='Stale public review'):
        inspect_bank(tmp_path)


def test_coverage_ledger_must_follow_new_reviewed_graph(tmp_path, sample):
    project = book_project(tmp_path / 'textbooks/book', sample, 'book')
    write_yaml(project.root / 'coverage.yaml', {
        'source': 'book', 'graph_digest': digest(project.knowledge)
    })
    assert inspect_bank(tmp_path)['projects']['book']['nodes']
    project.knowledge['nodes'][0]['summary'] = 'A newly reviewed clarification.'
    save_reviewed_graph(project)
    with pytest.raises(ProjectError, match='Stale public coverage'):
        inspect_bank(tmp_path)


def test_coverage_ledger_cannot_be_copied_from_another_project(tmp_path, sample):
    project = book_project(tmp_path / 'textbooks/book', sample, 'book')
    write_yaml(project.root / 'coverage.yaml', {
        'source': 'another-book', 'graph_digest': digest(project.knowledge)
    })
    with pytest.raises(ProjectError, match='Coverage ledger names another project'):
        inspect_bank(tmp_path)


@pytest.mark.parametrize('bad_origin_owner', [True, False])
def test_bank_origins_must_target_books(tmp_path, sample, bad_origin_owner):
    book = book_project(tmp_path / 'textbooks/book', sample, 'book')
    subject = book_project(tmp_path / 'subjects/topic', sample, 'topic')
    owner, target = (book, subject) if bad_origin_owner else (subject, subject)
    owner.knowledge['nodes'][0]['origins'] = [{
        'project': target.config['id'], 'node': next(iter(target.nodes)), 'note': 'Invalid role.'
    }]
    save_reviewed_graph(owner)
    with pytest.raises(ProjectError, match='must name a textbook'):
        inspect_bank(tmp_path)


def test_reviewed_book_imports_do_not_count_as_shared_overlap(tmp_path, sample):
    book = book_project(tmp_path / 'textbooks/book', sample, 'book')
    other = book_project(tmp_path / 'textbooks/other', sample, 'other')
    third = book_project(tmp_path / 'textbooks/third', sample, 'third')
    node = book.knowledge['nodes'][0]
    node['origins'] = [
        {'project': p.config['id'], 'node': next(iter(p.nodes)),
         'note': 'An external result used here; its derivation belongs to the cited book.'}
        for p in (other, third)
    ]
    save_reviewed_graph(book)
    report = inspect_bank(tmp_path)
    assert report['overlap'] == []
    assert report['imports'] == [
        {'book': 'book', 'node': node['id'], 'origin': origin}
        for origin in node['origins']
    ]


@pytest.mark.parametrize('invalid', ['self', 'missing-node', 'duplicate'])
def test_book_imports_reject_invalid_correspondences(tmp_path, sample, invalid):
    book = book_project(tmp_path / 'textbooks/book', sample, 'book')
    other = book_project(tmp_path / 'textbooks/other', sample, 'other')
    node = book.knowledge['nodes'][0]
    origin = {'project': 'other', 'node': next(iter(other.nodes)), 'note': 'Imported result.'}
    if invalid == 'self':
        origin['project'] = 'book'
    elif invalid == 'missing-node':
        origin['node'] = 'missing-node'
    node['origins'] = (
        [origin, {**origin, 'note': 'A second description of the same origin.'}]
        if invalid == 'duplicate' else [origin]
    )
    save_reviewed_graph(book)
    with pytest.raises(ProjectError, match='another textbook|Unknown origin|Duplicate origin'):
        inspect_bank(tmp_path)


@pytest.mark.parametrize('with_plan', [True, False])
def test_bank_excludes_course_plans_and_auto_attached_sources(tmp_path, sample, with_plan):
    project = book_project(tmp_path / 'textbooks/book', sample, 'book')
    if with_plan:
        write_yaml(project.root / 'plans/foundations.yaml', sample.plans['foundations'])
    else:
        project.config['sources'][0]['public_file'] = 'sources/primer.txt'
        write_yaml(project.root / 'project.yaml', project.config)
    with pytest.raises(ProjectError, match='without plans or source files'):
        inspect_bank(tmp_path)


def test_public_graph_bank_loads_without_source_registration():
    root = Path(__file__).resolve().parents[1] / 'graphs'
    report = inspect_bank(root)
    assert report['projects']
    assert all(p['plans'] == 0 for p in report['projects'].values())
