#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None

    n = 0
    for x in my_list:
        if x > n:
            n = x
    return n
