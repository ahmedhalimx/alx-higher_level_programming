#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if an object is a class instance or not.

    Args:
        obj (any): Object to check.
        a_class (type): Class to check with.
    Returns:
        If obj is an inherited instance  - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
