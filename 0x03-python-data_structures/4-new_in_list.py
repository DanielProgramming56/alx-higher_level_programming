#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpy_list = my_list.copy()
    if idx < 0:
        return my_list
    if idx > len(my_list):
        return my_list
    for i in range(len(cpy_list)):
        if i == idx:
            cpy_list[i] = element
    return cpy_list
