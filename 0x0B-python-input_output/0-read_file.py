#!/usr/bin/python3
"""Defines a useless read function."""


def read_file(filename=""):
    """Reads and prints the contents of a utf-8 encoded file to stdout."""
    with open(filename, encoding="utf-8") as fd:
        print(fd.read(), end="")
