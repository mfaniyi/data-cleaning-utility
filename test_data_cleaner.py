import pytest
from data_cleaner import remove_missing_values

def test_remove_missing_values():
    data = [
        "Michael",
        "",
        None,
        "Faniyi"
    ]

    result = remove_missing_values(data)

    assert result == [
        "Michael",
        "Faniyi"        
    ]


def test_empty_list():
    assert remove_missing_values([]) == []


def test_all_missing_values():
    data = ["", None, ""]
    assert remove_missing_values(data) == []


def test_invalid_input_type():
    with pytest.raises(TypeError):
        remove_missing_values("Michael")


def test_invalid_item_type():
    with pytest.raises(TypeError):
        remove_missing_values(["Michael", 123])