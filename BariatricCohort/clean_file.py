"""
Author: Jessica Avalos
Date: 7/13/2023
Description: This script is part of a pipeline and it will isolate the records to use for analysis into a file called unique.csv.
The remainder of the records will be moved to a file called removed.csv.
1. Removes records with 'None' in the NLP Status column
2. If there is a 'Prior' record, keep one of them and remove all others
3. If there is no 'Prior' but 'Disc', keep one 'Disc' record
"""
import pandas as pd


df = pd.read_csv('bariatric_unique_recs.csv')
removed_df = pd.DataFrame(columns=df.columns)

# Write the records with 'None' to removed_df and remove them from df 
none_df = df[df['NLP Status'] == 'None'] 
removed_df = pd.concat([removed_df, none_df]) 
df = df[df['NLP Status'] != 'None']

# Process duplicate records
dup_notes = df[df.duplicated('DocumentID', keep=False)]['DocumentID'].unique() 
for note in dup_notes:
    note_df = df[df['DocumentID'] == note]

    if 'Prior' in note_df['NLP Status'].values:
        keep_index = note_df[note_df['NLP Status'] == 'Prior'].index[0]
    elif 'Disc' in note_df['NLP Status'].values:
        keep_index = note_df[note_df['NLP Status'] == 'Disc'].index[0]

    drop_indexes = set(note_df.index) - {keep_index}
    # Add to removed_df
    removed_df = pd.concat([removed_df, df.loc[drop_indexes]])  
    df.drop(drop_indexes, inplace=True)

# Write the remaining records to unique.csv 
df.to_csv('unique.csv', index=False)

# Write the removed records to removed.csv 
removed_df.to_csv('removed.csv', index=False)
