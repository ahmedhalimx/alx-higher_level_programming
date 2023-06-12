#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    truth_set = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            truth_set.append(True)
        else:
            truth_set.append(False)
    return (truth_set)
