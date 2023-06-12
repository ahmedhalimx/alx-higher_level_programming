#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx > range(my_list):
        return None
    for i in range(my_list):
        if idx == i:
            return my_list[i]
