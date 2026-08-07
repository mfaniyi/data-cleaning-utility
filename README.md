# Data Cleaning Utility

A small typed Python utility module for cleaning missing values from datasets.

## Features

- Removes empty strings and missing values (`None`)
- Uses Python type hints
- Includes input validation and error handling
- Includes automated tests using pytest

## Project Structure

data-cleaning-utility/
│
├── data_cleaner.py
├── test_data_cleaner.py
├── requirements.txt
├── README.md
└── .gitignore

## Installation

Clone the repository:

- '''bash
git clone <repository.url>

## Create a virtual environment

- python -m venv .venv

## Activate the svirtual environment

- .venv\Scripts\activate

## Install depencies

- pip install -r requirements.txt

## Run

- pytest

Expected result

- 5 passed

## Example Usage

from data_cleaner import remove_missing_values

data = [
    "Michael",
    "",
    None,
    "Faniyi"
]

cleaned_data = remove_missing_values(data)

print(cleaned_data)


## Example Usage

[
    "Michael",
    "Faniyi"
]


