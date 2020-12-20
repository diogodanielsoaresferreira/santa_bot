from typing import Dict

import pytest
from rasa_sdk import Tracker, Action

from actions import NAME_SLOT, PRESENT_SLOT
from actions.actions import SaveXmasPresent
from actions.exceptions import SlotNotFound
from tests.actions import TEST_CONNECTION


class TestSaveXmasPresentAction:

    @pytest.fixture
    def action(self):
        return SaveXmasPresent(TEST_CONNECTION)

    def test_run_success(self, action: Action):
        result = action.run(None,
                   Tracker.from_dict({
                       "sender_id": "1",
                       "slots": {NAME_SLOT: "name", PRESENT_SLOT: "present"}}
                   ),
                   None)

        assert result == []

    @pytest.mark.parametrize("slots", [
        {NAME_SLOT: "name"},
        {PRESENT_SLOT: "present"}
    ])
    def test_run_slot_not_found_error(self, action: Action, slots: Dict[str, str]):
        with pytest.raises(SlotNotFound):
            action.run(None,
                       Tracker.from_dict({
                           "sender_id": "1",
                           "slots": slots}
                       ),
                       None)
