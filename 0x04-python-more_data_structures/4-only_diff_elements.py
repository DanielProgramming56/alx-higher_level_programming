#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    difference_1 = set_1 - set_2
    difference_2 = set_2 - set_1
    result_set = difference_1.union(difference_2)
    return result_set
