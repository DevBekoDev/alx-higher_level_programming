#!/usr/bin/python3
"""
a script that adds all arguments to a Python list, and then save to a file
"""


import json
import sys
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


my_list = []
filename = "add_item.json"

if os.path.exists(filename):
    my_list = load_from_json_file(filename)

for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])

save_to_json_file(my_list, filename)
