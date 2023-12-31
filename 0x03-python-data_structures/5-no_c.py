#!/usr/bin/python3

def no_c(my_string):
    if my_string is None:
        return

    new_string = ''
    for index, s in enumerate(my_string):
        if ord(s) != 99 and ord(s) != 67:
            new_string += s
    return new_string
