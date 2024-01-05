#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    n = 0
    a = ''
    for x in a_dictionary:
        if a_dictionary[x] > n:
            n = a_dictionary[x]
            a = x
    return a
