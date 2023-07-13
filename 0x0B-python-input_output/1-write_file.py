#!/usr/bin/python3
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """Write a string to a utf-8 encoded file.

    Args:
        filename (str): The path to the file.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as fd:
        return fd.write(text)
