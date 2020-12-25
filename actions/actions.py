"""Rasa actions to be called by the Rasa Server."""
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker  # type: ignore
from rasa_sdk.executor import CollectingDispatcher  # type: ignore

from . import NAME_SLOT, PRESENT_SLOT
from .data_models import XmasPresents
from .exceptions import SlotNotFound


def _get_slot(tracker: Tracker, slot: str) -> str:
    """
    Extract slot value from a tracker.

    :param tracker: conversation tracker.
    :param slot: slot key.
    :raise SlotNotFound: thrown if slot key is not in tracker.
    :return: slot value.
    """
    slot = tracker.get_slot(slot)

    if slot is None:
        raise SlotNotFound(slot)

    return slot


class SaveXmasPresent(Action):
    """Rasa action to save a christmas present wish of a user to the database."""

    def __init__(self, db_url=None):
        """
        Rasa action to save a christmas present wish of a user to the database.

        :param db_url: connection to the database.
        """
        self.xmas_presents = XmasPresents(db_url)
        super().__init__()

    def name(self) -> Text:
        """
        Get action name.

        :return: action name.
        """
        return "action_save_xmas_present"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        """
        Run the action and store the christmas present in the database.

        :param dispatcher: rasa dispatcher.
        :param tracker: conversation tracker.
        :param domain: conversation domain.
        :return: list of actions to be performed.
        """
        name = _get_slot(tracker, NAME_SLOT)
        present = _get_slot(tracker, PRESENT_SLOT)
        self.xmas_presents.add_present(name, present)

        return []
