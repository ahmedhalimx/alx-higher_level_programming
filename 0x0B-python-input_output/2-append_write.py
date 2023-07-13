#!/usr/bin/python3
"""Defines a append write function."""


def append_write(filename="", text=""):
    """Appends a string to the end of a utf-8 endcoded file.

    Args:
        filename (str): file's path.
        text (str): The string to append to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as fd:
        return fd.write(text)
