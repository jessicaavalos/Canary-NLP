For users that do not use the terminal:

1. Download spyder: https://www.spyder-ide.org/

2. Place a file called smoking_cohort.csv in the same folder as the script. The file should include the columns DocumentID,OutputCriteria from canary results

3. Run the smoking_cohort.py script by opening the script in spyder and click the green run button. This will apply the rules from the legend and generate two files: sentence_level_classification.csv & document_level_classification.csv

For terminal users: 

      python3 smoking_cohort.py input_file.csv
