#!/usr/bin/python3
def no_c(my_string):
    my_string_c = [ch for ch in my_string if ch != 'c' and ch != 'C']
    return my_string_c
