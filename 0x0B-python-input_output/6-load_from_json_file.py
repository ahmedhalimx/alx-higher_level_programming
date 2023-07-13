#!/usr/bin/python3
"""Defines a JSON object to Python object function."""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON object."""
    with open(filename) as fd:
        return json.load(fd)
