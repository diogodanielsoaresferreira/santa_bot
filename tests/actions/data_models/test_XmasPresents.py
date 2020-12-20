from datetime import datetime

from actions.data_models import XmasPresents

TEST_CONNECTION = 'sqlite:///:memory:'

instance = XmasPresents(TEST_CONNECTION)


def test_add_present():
    date_before_add = datetime.now()
    entry = instance.add_present("name", "present")
    date_after_add = datetime.now()
    assert entry.name == "name"
    assert entry.present == "present"
    assert entry.created_at > date_before_add
    assert entry.created_at < date_after_add

