# Data Cleaning Utility

A small typed Python utility module for cleaning missing values from datasets.

## Features

- Removes empty strings and missing values (`None`)
- Uses Python type hints
- Includes input validation and error handling
- Includes automated tests using `pytest`

## How It Works

The utility processes a list of values and removes missing entries.

The function:

1. Accepts a list containing strings and missing values.
2. Checks each item.
3. Removes empty strings and `None` values.
4. Returns a clean list containing valid strings.

## Project Structure

```text
data-cleaning-utility/
│
├── data_cleaner.py
├── test_data_cleaner.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

### Clone the repository:

```bash
git clone https://github.com/mfaniyi/data-cleaning-utility.git
```

### Navigate into the project folder

```bash
cd data-cleaning-utility
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the virtual environment

```bash
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Run the test suite

```bash
pytest
```

### Expected result

```text
- 5 passed
```

## Example Usage

```python
from data_cleaner import remove_missing_values

data = [
    "Michael",
    "",
    None,
    "Faniyi"
]

cleaned_data = remove_missing_values(data)

print(cleaned_data)
```

### Expected Outcome

```python
["Michael", "Faniyi"]
```

## Requirements

- Python 3.14 or later
- pytest

## License

This project was created as an assignment to the first week of AI/ML Transition Cohort

### Class Assessment 
This is just for the purpose of class assessment
