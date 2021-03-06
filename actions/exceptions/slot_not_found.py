"""Implementation of SlotNotFound exception."""


class SlotNotFound(Exception):
    """Slot not found exception."""

    def __init__(self, slot):
        """
        Raise SlotNotFound exception.

        :param slot: slot name.
        """
        self.slot = slot
        self.message = f"Slot {slot} not found."
        super().__init__(self.message)
