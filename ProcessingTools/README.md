Script that adds the canary delimiter to input files.
canaryDelimiter.py adds the record number as the documentID
noteID_delimiter.py adds the noteid as the documentID

Usage: python3 canaryDelimiter.py in.txt out.txt.

Expects the following input file format (utf8 encoding): "note" [tab]1[tab] noteID
