#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        tuple_a += (0,)
        if len(tuple_a) < 2:
            tuple_a += (0,)
    elif len(tuple_b) < 2:
        tuple_b += (0,)
        if len(tuple_b) < 2:
            tuple_b += (0,)

    i = 0
    new_tuple = ()
    while i < 2:
        x = tuple_a[i] + tuple_b[i]
        new_tuple += (x,)
        i += 1
    return new_tuple
