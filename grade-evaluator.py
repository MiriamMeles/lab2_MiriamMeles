
import csv
import sys
import os

def load_csv_data():
    """
    Prompts the user for a filename, checks if it exists,
    and extracts all fields into a list of dictionaries.
    """
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")

    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found. Nothing to grade")
        sys.exit(1)

    assignments = []

    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert numeric fields to floats for calculations
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
                
        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)
    
def evaluate_grades(data):
    """
    Implement your logic here.
    'data' is a list of dictionaries containing the assignment records.
    """
    print("\n--- Processing Grades ---")

     # a) Check if all scores are percentage based (0-100)
    for item in data:
        if item['score'] < 0 or item['score'] > 100:
            print(f"Error: '{item['assignment']}' has a score of {item['score']:g}. "
                  f"Scores must be between 0 and 100.")
            return


    # b) Validate total weights (Total=100, Summative=40, Formative=60)
    total_weight = 0
    formative_weight = 0
    summative_weight = 0

    for item in data:
        total_weight = total_weight + item['weight']
        if item['group'] == 'Formative':
            formative_weight = formative_weight + item['weight']
        elif item['group'] == 'Summative':
            summative_weight = summative_weight + item['weight']

    if total_weight != 100:
        print(f"Error: Total weight is {total_weight}. It must be exactly 100.")
        return
    if formative_weight != 60:
        print(f"Error: Formative weight is {formative_weight}. It must be exactly 60.")
        return
    if summative_weight != 40:
        print(f"Error: Summative weight is {summative_weight}. It must be exactly 40.")
        return

    
    # c) Calculate the Final Grade and GPA
    formative_score = 0
    summative_score = 0

    for item in data:
        points = item['score'] * item['weight'] / 100
        if item['group'] == 'Formative':
            formative_score = formative_score + points
        elif item['group'] == 'Summative':
            summative_score = summative_score + points

    total_grade = formative_score + summative_score
    GPA = (total_grade / 100) * 5.0


    # d) Determine Pass/Fail status (>= 50% in BOTH categories)
    formative_pass = formative_score >= 0.5 * formative_weight
    summative_pass = summative_score >= 0.5 * summative_weight

    if formative_pass and summative_pass:
        status = "PASSED"
    else:
        status = "FAILED"


    # e) Check for failed formative assignments (< 50%) and determine which one(s) have the highest weight for resubmission.
    failed_formatives = []
    for item in data:
        if item['group'] == 'Formative' and item['score'] < 50:
            failed_formatives.append(item)

    # Among those, keep the ones with the highest weight (ties all count)
    resubmit = []
    if len(failed_formatives) > 0:
        highest_weight = failed_formatives[0]['weight']
        for item in failed_formatives:
            if item['weight'] > highest_weight:
                highest_weight = item['weight']
        for item in failed_formatives:
            if item['weight'] == highest_weight:
                resubmit.append(item)


    # f) Print the final decision (PASSED / FAILED) and resubmission options
    print(f"\nFormative: {formative_score:.2f}/{formative_weight} "
          f"({'PASS' if formative_pass else 'FAIL'})")
    print(f"Summative: {summative_score:.2f}/{summative_weight} "
          f"({'PASS' if summative_pass else 'FAIL'})")
    print(f"Final Grade: {total_grade:.2f}/100")
    print(f"GPA: {GPA:.2f}/5.0")
    print(f"Final Status: {status}")

    if len(resubmit) > 0:
        print("\nEligible for resubmission (highest-weight failed formative):")
        for item in resubmit:
            print(f"  - {item['assignment']} (score {item['score']}, weight {item['weight']:g})")
    else:
        print("\nNo failed formative assignments. Nothing to resubmit.")



if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()

    # 2. Process the features
    evaluate_grades(course_data)