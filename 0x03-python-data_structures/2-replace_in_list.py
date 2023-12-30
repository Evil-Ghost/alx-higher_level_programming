#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list

    for index, x in enumerate(my_list):
        if index == idx:
            my_list[index] = element
            return my_list

    return my_list
