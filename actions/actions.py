from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from .data_models import XmasPresents
from .exceptions import SlotNotFound
from . import NAME_SLOT, PRESENT_SLOT


def _get_slot(tracker: Tracker, slot: str):
    slot = tracker.get_slot(slot)

    if slot is None:
        raise SlotNotFound(slot)

    return slot


class SaveXmasPresent(Action):

    def __init__(self, db_url=None):
        self.xmasPresents = XmasPresents(db_url)
        super().__init__()

    def name(self) -> Text:
        return "action_save_xmas_present"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = _get_slot(tracker, NAME_SLOT)
        present = _get_slot(tracker, PRESENT_SLOT)
        self.xmasPresents.add_present(name, present)

        return []
