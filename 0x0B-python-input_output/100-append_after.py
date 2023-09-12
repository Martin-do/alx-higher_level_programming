#!/usr/bin/python3


def append_after(filename="", search_string="", new_string=""):
    """ function that inserts a line of text to a file,
    after each line containing a specific string

    Args:
        filename (str): file to be updated. Defaults to "".
        search_string (str): the string after which to insert
        the line of text. Defaults to "".
        new_string (str): the new string to insert. Defaults to "".
    """
    lines = []
    with open(filename, 'r', encoding="UTF-8") as f:
        for line in f:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)

    with open(filename, 'w', encoding="UTF-8") as f:
        for line in lines:
            f.write(line)
