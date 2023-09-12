#!/usr/bin/python3
"""appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """append a string and returns number of characters added

    Args:
        filename (str, optional): file to write to.
        Defaults to "".
        text (str, optional): text to be written to file.
        Defaults to "".

    Returns:
        int: number of charactes
    """
    count = 0
    with open(filename, 'a', encoding="UTF-8") as f:
        count += f.write(text)
    return count
