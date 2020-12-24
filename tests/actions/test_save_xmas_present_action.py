"""Integration tests to SaveXmasPresentAction."""
# pylint: disable=redefined-outer-name
from typing import Dict

import pytest
from rasa_sdk import Action, Tracker

from actions import NAME_SLOT, PRESENT_SLOT
from actions.actions import SaveXmasPresent
from actions.exceptions import SlotNotFound
from tests.actions import TEST_CONNECTION


@pytest.fixture
def action():
    """Return SaveXmasPresent instance with a connection to a in-memory database."""
    return SaveXmasPresent(TEST_CONNECTION)


def test_run_success(action: Action):
    """
    Given a slot with name and present,
    When run action,
    Then no error.

    :param action: SaveXmasPresent action instance.
    """
    result = action.run(
        None,
        Tracker.from_dict(
            {
                "sender_id": "1",
                "slots": {NAME_SLOT: "name", PRESENT_SLOT: "present"},
            }
        ),
        None,
    )

    assert result == []


@pytest.mark.parametrize("slots", [{NAME_SLOT: "name"}, {PRESENT_SLOT: "present"}])
def test_run_slot_not_found_error(action: Action, slots: Dict[str, str]):
    """
    Given a slot without name or present,
    When run action,
    Then raise SlotNotFound error.

    :param action: SaveXmasPresent action instance.
    :param slots: slot.
    """
    with pytest.raises(SlotNotFound):
        action.run(None, Tracker.from_dict({"sender_id": "1", "slots": slots}), None)
