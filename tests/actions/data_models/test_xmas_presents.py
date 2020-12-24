"""Integration tests to XmasPresents."""
# pylint: disable=redefined-outer-name
from datetime import datetime

import pytest

from actions.data_models import XmasPresents
from tests.actions import TEST_CONNECTION


@pytest.fixture
def instance() -> XmasPresents:
    """Return XmasPresents instance with connection to an in-memory database."""
    return XmasPresents(TEST_CONNECTION)


@pytest.mark.parametrize(
    "name,present", [("Diogo", "car"), ("Luke", "smartphone"), ("John", "bicycle")]
)
def test_add_present_success(instance: XmasPresents, name: str, present: str):
    """
    Given a person name and a present,
    When adding present,
    Then name, present and created_at values are correct.

    :param instance: XmasPresents instance.
    :param name: person name.
    :param present: present name.
    """
    date_before_add = datetime.now()
    entry = instance.add_present(name, present)
    date_after_add = datetime.now()
    assert entry.name == name
    assert entry.present == present
    assert entry.created_at > date_before_add
    assert entry.created_at < date_after_add


@pytest.mark.parametrize(
    "name,present",
    [
        (1, "present"),
        ("name", 1),
        (None, "present"),
        ("name", None),
        ("", "present"),
        ("name", ""),
    ],
)
def test_add_present_argument_type_error(
        instance: XmasPresents, name: str, present: str
):
    """
    Given a person name or a present malformed,
    When adding present,
    Then raises TypeError.

    :param instance: XmasPresents instance.
    :param name: person name.
    :param present: present name.
    """
    with pytest.raises(TypeError):
        instance.add_present(name, present)
