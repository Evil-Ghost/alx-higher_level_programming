#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    copy_list = my_list[:]

    if idx < 0:
        return copy_list
    for index, x in enumerate(copy_list):
        if index is idx:
            copy_list[index] = element
            return copy_list
    return copy_list
