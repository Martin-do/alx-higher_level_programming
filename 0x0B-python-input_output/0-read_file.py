#!/usr/bin/python3


def read_file(filename=""):
    """function that reads txt files and prints
    them out to stdout

    Args:
        filename (str, optional): the filename to be
        read and printed. Defaults to "".
    """
    with open(filename, 'r', encoding="UTF-8") as f:
        read_data = f.read()
    print(read_data)
