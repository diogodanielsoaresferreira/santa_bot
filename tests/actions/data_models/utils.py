import pytest

from actions.data_models import XmasPresents

TEST_CONNECTION = 'sqlite:///:memory:'


@pytest.fixture
def instance() -> XmasPresents:
    return XmasPresents(TEST_CONNECTION)
