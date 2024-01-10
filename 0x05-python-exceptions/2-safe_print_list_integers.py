#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    if my_list == [] or x == 0:
        print()
        return 0

    i, j = 0, 0
    while i < x:
        try:
            if i + 1 != x:
                print("{:d}".format(my_list[i]), end='')
            else:
                print("{:d}".format(my_list[i]))
        except (TypeError, ValueError):
            if i + 1 == x:
                print()
            j += 1
        i += 1
    return i - j
