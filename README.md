# Lab 2: ALU Transcript Generator

A Python program that reads a CSV file of course grades, validates the data, calculates the final grade and GPA, decides PASSED or FAILED, and lists the formative assignments eligible for resubmission. A Bash script archives the grades file and logs every run.

## Files

| File | Purpose |
|------|---------|
| `grade-evaluator.py` | Reads and validates the CSV, calculates the grade and GPA, and prints the result |
| `organizer.sh` | Archives `grades.csv` with a timestamp, creates a new empty `grades.csv`, and logs the action |
| `grades.csv` | Sample course grades |

## What you need

- Python 3 (only the built-in `csv`, `sys` and `os` modules are used)
- A Linux terminal. On Windows, use WSL to run the shell script.
- A `grades.csv` file in the same folder, with these columns: `assignment,group,score,weight`

## Running the Python program

From the project folder, run:

```bash
python3 grade-evaluator.py
```

Type `grades.csv` when prompted for a filename. The program then:

1. Checks that every score is between 0 and 100.
2. Checks that the weights add up to 100, with Formative at 60 and Summative at 40.
3. Calculates the final grade and the GPA using `GPA = (Total Grade / 100) * 5.0`.
4. Decides PASSED or FAILED. A student passes only with at least 50% in **both** Formative and Summative, not just overall.
5. Lists the failed Formative assignment(s) with the highest weight as eligible for resubmission. If several share that weight, all of them are listed.

Example output:

```
--- Processing Grades ---

Formative: 34.00/60 (PASS)
Summative: 26.00/40 (PASS)
Final Grade: 60.00/100
GPA: 3.00/5.0
Final Status: PASSED

Eligible for resubmission (highest-weight failed formative):
  - Group Exercise (score 40, weight 20)
  - Functions and Debugging Lab (score 45, weight 20)
```

If the data is wrong (a score outside 0 to 100, or weights that do not add up), the program prints a clear error message and stops.

## Running the shell script

```bash
bash organizer.sh
```

Or make it executable first and run it directly:

```bash
chmod +x organizer.sh
./organizer.sh
```

Each run:

1. Creates the `archive` folder if it does not exist.
2. Builds a timestamp in `YYYYMMDD-HHMMSS` format.
3. Moves `grades.csv` into `archive/`, renamed to `grades_<timestamp>.csv`.
4. Creates a new, empty `grades.csv`.
5. Adds one line to `organizer.log` with the timestamp, the original filename and the archived filename.

The log is never overwritten, so it keeps one line per run. If `grades.csv` is missing, the script prints an error and stops.

**Note:** the script empties `grades.csv`. To grade again, copy a file back from the archive, for example `cp archive/grades_<timestamp>.csv grades.csv`.

## Edge cases handled

- File not found: a clear error message.
- A row with a missing or non-numeric score or weight: a warning, and the row is skipped.
- Scores outside 0 to 100: an error message.
- Weights that do not add up correctly: an error message.
- `grades.csv` missing when running the shell script: an error message.