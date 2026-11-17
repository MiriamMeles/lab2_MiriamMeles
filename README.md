# Lab 2: ALU Transcript Generator
## Overview

This project calculates a student's final academic standing from a CSV file of
course grades. A Python program validates the data, works out the weighted
grade and GPA, decides whether they PASSED or FAILED, and lists which assignments can be
resubmitted. A Bash script archives the grades file between batches and keeps a
log of each archive.

## Files

| File | Purpose |
|------|---------|
| `grade-evaluator.py` | Reads the CSV, validates it, calculates the grade and GPA, and prints the transcript |
| `organizer.sh` | Archives `grades.csv` with a timestamp, creates a fresh empty `grades.csv`, and logs the action |
| `grades.csv` | Sample course grades used as input |
| `README.md` | This file |

## Requirements

- Python 3 (only the built-in `csv`, `sys` and `os` modules are used, with no external libraries)
- Bash (Linux, or WSL on Windows)

## CSV format

`grades.csv` must have this header on the first line, followed by one row per assignment:

```
assignment,group,score,weight
Quiz,Formative,85,20
```

- `group` is either `Formative` or `Summative`.
- `score` is a percentage from 0 to 100.
- `weight` is how much the assignment counts toward the final grade.