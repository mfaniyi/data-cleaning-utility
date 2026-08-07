def remove_missing_values(data: list[str | None]) -> list[str]:
    if not isinstance(data, list):
        raise TypeError("Input data must be a list.")

    cleaned_data = []

    for item in data:
        if item is not None and item != "":
            if not isinstance(item, str):
                raise TypeError("All items must be strings")

            cleaned_data.append(item)

    return cleaned_data

if __name__ == "__main__":
    sample_data = [
        "Michael",
        "",
        None,
        "Faniyi"
    ]

    result = remove_missing_values(sample_data)

    print(result)