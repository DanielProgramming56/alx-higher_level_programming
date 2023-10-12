#!/usr/bin/python3
def uniq_add(my_list=[]):
    set_list = set(my_list)
    unique_list = list(set_list)

    return sum(unique_list)

