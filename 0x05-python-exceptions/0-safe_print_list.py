#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list == [] or my_list is None or x == 0:
        print()
        return 0

    i = 0
    while i < x:
        try:
            if (i + 1) != x:
                print("{}".format(my_list[i]), end='')
            else:
                print("{}".format(my_list[i]))
            i += 1
        except IndexError:
            print()
            break
    return i
