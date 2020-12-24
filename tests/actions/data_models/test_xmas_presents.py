from datetime import datetime

import pytest

from actions.data_models import XmasPresents
from tests.actions import TEST_CONNECTION


class TestXmasPresent:
    @pytest.fixture
    def instance(self) -> XmasPresents:
        return XmasPresents(TEST_CONNECTION)

    @pytest.mark.parametrize(
        "name,present", [("Diogo", "car"), ("Luke", "smartphone"), ("John", "bicycle")]
    )
    def test_add_present_success(self, instance: XmasPresents, name: str, present: str):
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
        self, instance: XmasPresents, name: str, present: str
    ):
        with pytest.raises(TypeError):
            instance.add_present(name, present)
