"""
Author: Jessica Avalos
Date: 8/31/2023
Description: This script will apply the smoking output criteria rules to a csv file with
canary results. The canary results file should have the columns DocumentID,OutputCriteria. 
"""
import csv
import sys
import os

# Declare files
if len(sys.argv) == 2:
    input_file = sys.argv[1]
    if not os.path.exists(input_file): 
        print('Input file does not exist.')
        sys.exit()
elif len(sys.argv) > 2:
    print('Incorrect number of arguments passed')
    print('Usage: python3 smoking_cohort.py input_file.csv')
    sys.exit() 
else: 
    print('No arguments passed, processing smoking_cohort.csv') 
    input_file = 'smoking_cohort.csv'
    if not os.path.exists(input_file): 
        print('smoking_cohort.csv file does not exist.')
        sys.exit()

# Frequency & hierarchy approach
def classify_smoking_status(criteria_list):
    freq_count = {'Current': 0, 'Past': 0, 'Non-smoker': 0, 'NA': 0}
    for criteria in criteria_list:
        if criteria in freq_count:
            freq_count[criteria] += 1
        else:
            freq_count['NA'] += 1

    # sorting based on frequency & hierarchy
    sorted_status = sorted(freq_count.items(), key=lambda x: (-x[1], ['Current', 'Past', 'Non-smoker', 'NA'].index(x[0])))
    return sorted_status[0][0] 

document_data = {}
sentence_results = []
with open(input_file, 'r') as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)[1:]
    
    for i, row in enumerate(rows):
        document_id, output_criteria = row[0], list(map(int, row[1].split(',')))

        if document_id not in document_data:
            document_data[document_id] = {'sentences': [], 'smoking_status': []}

        # Step 1 
        if 1 in output_criteria:
            if i + 1 < len(rows):
                next_row = rows[i + 1]
                next_output_criteria = list(map(int, next_row[1].split(',')))
                next_document_id = next_row[0]

                if document_id == next_document_id:
                    if any(x in next_output_criteria for x in [7, 10, 13, 17, 21, 22]):
                        output_criteria.remove(1)

        # Step 2
        if any(x in output_criteria for x in [7, 19]) and 1 in output_criteria:
            output_criteria.remove(1)
            
        # Step 3
        sentence_criteria = []
        for criteria in output_criteria:
            if criteria in [1, 2, 3, 4]:
                sentence_criteria.append('Current')
            elif criteria in list(range(5, 15)) + [20,21]:
                sentence_criteria.append('Past')
            elif criteria in list(range(15, 20)) + [22,23]:
                sentence_criteria.append('Non-smoker')
            else: 
                sentence_criteria.append('NA')

        if not sentence_criteria: 
            sentence_criteria = ['NA']

        sentence_status = classify_smoking_status(sentence_criteria)
        document_data[document_id]['sentences'].append(sentence_status)
        document_data[document_id]['smoking_status'].append(sentence_status)

        sentence_results.append([document_id, ','.join(map(str, output_criteria)), sentence_status])

# Write results
with open('sentence_level_classification.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['DocumentID', 'OutputCriteria', 'NLP Status'])
    for result in sentence_results:
        writer.writerow(result)

with open('document_level_classification.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['DocumentID', 'NLP Status'])
    for document_id, data in document_data.items():
        document_status = classify_smoking_status(data['smoking_status'])
        writer.writerow([document_id, document_status])
