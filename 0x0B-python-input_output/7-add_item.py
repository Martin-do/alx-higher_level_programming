#!/usr/bin/python3
"""adds all arguments to a Python list,
and then save them to a file"""
import json
import sys
import os


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


def main():
    f_name = "add_items.json"
    args = len(sys.argv)

    if not os.path.isfile(f_name):
        with open(f_name, 'w', encoding='utf-8') as f:
            f.write('[]')

    if args > 1:
        data = load_from_json_file(f_name)
        for arg in range(1, len(sys.argv)):
            data.append(sys.argv[arg])
        save_to_json_file(data, f_name)


main()
