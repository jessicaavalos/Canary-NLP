# -*- coding: utf-8 -*-
"""
Author: Jessica Avalos
Date: 4/25/2023
Description: This script will add the canary start delimiter line to notes where
the delimiter tab1tab is found at the end of the record.
Expects the following format: "note" [tab]1[tab] noteID
"""

import sys

if len(sys.argv) > 1:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
else: 
    input_file = 'test.txt'
    output_file = 'testout.txt'

start_delimiter = '{}*|#*|#*|#1*|#*|#*|#\n'
end_delimiter = '\t1\t'

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
