"""
Author: Jessica Avalos
Date: 7/12/2023
Description: This script will apply the bariatric surgery output criteria rules to a csv file with
canary results. The canary results file should have the columns DocumentID,OutputCriteria. (case sensitive)
"""
import csv

def process_criteria(criteria):
    criteria = list(map(int, criteria.split(',')))

    # Apply the rules
    if 32 in criteria:
        criteria = [c for c in criteria if c not in list(range(1, 15)) + [29,32,33]]
        if not criteria:
            return 'None'
    if 13 in criteria or 29 in criteria:
        return 'Disc'
    if any(c in criteria for c in range(2, 13)) or 14 in criteria:
        return 'Prior'
    if 1 in criteria and len(criteria) == 1:
        return 'Disc'
    if 33 in criteria and len(criteria) == 1:
        return 'Disc'
    if any(c in criteria for c in range(26,29)) and not any(c in criteria for c in range(34, 39)) and not any(c in criteria for c in list(range(2, 13)) + [14]):
        return 'Disc'
    if any(c in criteria for c in range(26,29)) and any(c in criteria for c in range(34, 39)):
        return 'None'
    if 30 in criteria and 31 in criteria and len(criteria) == 2:
        return 'None'
    if any(c in criteria for c in range(15,29)) or 1 in criteria or 30 in criteria or 33 in criteria:
        return 'Disc'
    if 30 in criteria and len(criteria) == 1:
        return 'Disc'
    return 'Uncategorized', criteria

# Read the input CSV file
with open('cohort.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    data = list(reader)

# Process the data
for row in data:
    row['NLP Status'] = process_criteria(row['OutputCriteria'])

# Write the output CSV file
with open('bariatric_cohort.csv', 'w', newline='') as f:
    fieldnames = ['DocumentID', 'OutputCriteria', 'NLP Status'] 
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    for row in data:
        writer.writerow(row)
