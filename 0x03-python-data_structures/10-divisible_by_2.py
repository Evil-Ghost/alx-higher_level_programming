#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list == []:
        return None
    true_false = []
    for n in my_list:
        if n % 2 == 0:
            true_false.append(True)
        else:
            true_false.append(False)
    return true_false
