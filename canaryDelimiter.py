# -*- coding: utf-8 -*-
"""
Author: Jessica Avalos
Date: 4/25/2023
Description: This script will add the canary start delimiter line to notes where
the delimiter tab1tab is found at the end of the record.
Expects the following format: "note" [tab]1[tab] noteID
"""

import sys
import os

# Declare files
if len(sys.argv) == 3:
    input_file = sys.argv[1]
    if not os.path.exists(input_file): 
        print('Input file does not exist.')
        sys.exit()
    output_file = sys.argv[2]
elif len(sys.argv) == 2:
    print('Incorrect number of arguments passed')
    print('Usage: python3 canaryDelimiter.py in.txt out.txt')
    sys.exit() 
else: 
    print('No arguments passed, processing test.txt') 
    input_file = 'test.txt'
    if not os.path.exists(input_file): 
        print('test.txt file does not exist.')
        sys.exit()
    output_file = 'testout.txt'

# Declare delimiter
start_delimiter = '{}*|#*|#*|#1*|#*|#*|#\n'
end_delimiter = '\t1\t'

# Open files
with open(input_file, 'r', encoding="utf8") as f_in, open(output_file, 'w', encoding="utf8") as f_out:
    record_count = 1
    record_lines = []
    for line in f_in:
        # Check if this line ends the current record
        if end_delimiter in line:
            # Add the line to the record lines and write out the complete record
            record_lines.append(line)
            f_out.write(start_delimiter.format('{:03d}'.format(record_count)))
            f_out.writelines(record_lines)
            record_count += 1
            record_lines = []
        else:
            # Add the line to the current record lines
            record_lines.append(line)
