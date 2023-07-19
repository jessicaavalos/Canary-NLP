"""
Author: Jessica Avalos
Date: 7/12/2023
Description: This script will remove duplicate records
"""
import pandas as pd
df = pd.read_csv('bariatric_cohort.csv')
df_unique = df.drop_duplicates()
df_unique.to_csv('bariatric_unique_recs.csv', index = False)