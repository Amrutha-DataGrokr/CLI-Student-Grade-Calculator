# CLI Student Grade Calculator

## Overview

The **CLI Student Grade Calculator** is a Python-based command-line application that reads student marks from a CSV file, calculates performance statistics, assigns grades, and generates a formatted student grade report.

The application displays the report in the terminal and saves it as a text file (`grades_report.txt`).

## Features

- **CSV File Handling:** Reads student records using Python's `csv` module.
- **Data Conversion:** Converts subject marks into integers.
- **Statistics Calculation:** Calculates total, average, highest, and lowest marks for each student.
- **Grade Assignment:** Assigns grades based on the student's average.
- **Pass/Fail Classification:** Determines whether a student has passed or failed.
- **Formatted Report:** Displays a structured student grade report in the terminal.
- **Report Generation:** Saves student results and class summary to a `.txt` file.
- **Exception Handling:** Handles missing files, invalid marks, and file access errors.
- **CLI Input:** Accepts a custom CSV file path or uses the default input file.

## Project Structure

```text
CLI-Student-Grade-Calculator/
│
├── students_input.csv
├── grade_calculator.py
├── grades_report.txt
├── invalid_marks.csv
├── missing_column.csv
└── README.md
```

## Input Format

The application expects a CSV file containing the following columns:

| Name | Math | Science | English | History | PE |
|---|---:|---:|---:|---:|---:|
| Alice | 92 | 88 | 95 | 90 | 85 |
| Bob | 75 | 82 | 78 | 80 | 72 |

The CSV file must contain student names and numeric marks for all five subjects.

## Grading Criteria

Grades are assigned based on the student's average marks.

| Average | Grade | Status |
|---|---|---|
| 90 and above | A | Pass |
| 80–89.99 | B | Pass |
| 70–79.99 | C | Pass |
| 60–69.99 | D | Pass |
| Below 60 | F | Fail |

## How to Run

### Prerequisites

- Python 3.x
- No external libraries required. The application uses Python standard library modules.

### Steps

1. Clone the repository:

```bash
git clone https://github.com/Amrutha-DataGrokr/CLI-Student-Grade-Calculator.git
```

2. Navigate to the project directory:

```bash
cd CLI-Student-Grade-Calculator
```

3. Run the Python program:

```bash
python grade_calculator.py
```

4. Enter the CSV file path when prompted.

```text
Enter input file path (default: students_input.csv):
```

Press Enter to use the default file or provide a custom CSV file path.

## Output

The application generates two outputs:

**1. Terminal Report**

Displays each student's:
- Name
- Average
- Grade
- Pass/Fail status

**2. Text Report (`grades_report.txt`)**

Saves the formatted student report along with a class summary containing:
- Total number of students
- Class average
- Highest student average
- Lowest student average
- Number of students passed
- Number of students failed

The output file is created in the current working directory.

## Error Handling

The application handles the following scenarios:

- Input CSV file not found.
- Non-numeric marks in the CSV file.
- Empty score lists during statistics calculation.
- Permission errors while saving the report.
- Other file system errors.

## Concepts Practiced

- Python functions and modular programming
- Lists and dictionaries
- List comprehensions
- File handling
- CSV processing
- Exception handling
- Conditional statements and loops
- String formatting
- Command-line input
- Working with file paths using `os`

