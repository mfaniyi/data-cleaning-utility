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
    try:
        remove_missing_values("Michael")
    except TypeError:
        assert True


def test_invalid_item_type():
    try:
        remove_missing_values(["Michael", 123])
    except TypeError:
        assert True