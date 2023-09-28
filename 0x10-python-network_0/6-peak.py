#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(int_list):
    """Finds a peak in int_list"""

    if int_list is None or int_list == []:
        return None
    low = 0
    high = len(int_list)
    mid = ((high - low) // 2) + low
    mid = int(mid)
    if high == 1:
        return int_list[0]
    if high == 2:
        return max(int_list)
    if int_list[mid] >= int_list[mid - 1] and\
            int_list[mid] >= int_list[mid + 1]:
        return int_list[mid]
    if mid > 0 and int_list[mid] < int_list[mid + 1]:
        return find_peak(int_list[mid:])
    if mid > 0 and int_list[mid] < int_list[mid - 1]:
        return find_peak(int_list[:mid])
