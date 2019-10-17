#!/usr/bin/python3
import json
import sys
import os.path

to_json = __import__('7-save_to_json_file').save_to_json_file
from_json = __import__('8-load_from_json_file').load_from_json_file
a_list = []
filename = "add_item.json"

if os.path.exists(filename):
    a_list = from_json(filename)

for arg in sys.argv[1:]:
    a_list.append(arg)

to_json(a_list, filename)
