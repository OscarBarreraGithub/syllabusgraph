from pathlib import Path

import pytest

from syllabusgraph.cli import initialize


ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def sample(tmp_path):
    return initialize(tmp_path / "course", "sampling")


@pytest.fixture
def blank(tmp_path):
    return initialize(tmp_path / "new", "blank")
