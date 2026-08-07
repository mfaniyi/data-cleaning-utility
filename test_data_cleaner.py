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