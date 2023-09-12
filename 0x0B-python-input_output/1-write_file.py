#!/usr/bin/python3
"""function that writes to a file"""


def write_file(filename="", text=""):
    """writes a string and returns number of characters written

    Args:
        filename (str, optional): file to write to.
        Defaults to "".
        text (str, optional): text to be written to file.
        Defaults to "".

    Returns:
        int: number of charactes
    """
    count = 0
    with open(filename, 'w', encoding="UTF-8") as f:
        count += f.write(text)
    return count
