def remove_missing_values(data: list[str | None]) -> list[str]:
    cleaned_data = []

    for item in data:
        if item is not None and item != "":
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