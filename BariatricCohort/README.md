For users that do not use the terminal:
1. Download spyder: https://www.spyder-ide.org/
2. Place a file called cohort.csv in the same folder as these scripts. The file should include the columns DocumentID,OutputCriteria (case sensitive) from canary results
3. Run the bariatric_cohort.py script by opening the script in spyder and click the green run button. This will apply the rules from  the legend and generate a file called bariatric_cohort.csv
5. Open the remove_duplicates.py script in spyder and run it, this script will remove duplicate records from bariatric_cohort.csv and will create a file called bariatric_unique_recs.csv
6. Open the classify_bariatric.py script in spyder and run it, this script will generate two files: unique.csv & removed.csv. unique.csv records should be used for analysis, the rest were removed (None, dupes)
