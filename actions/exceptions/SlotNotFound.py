class SlotNotFound(Exception):
    def __init__(self, slot):
        self.slot = slot
        self.message = f"Slot {slot} not found."
        super().__init__(self.message)
