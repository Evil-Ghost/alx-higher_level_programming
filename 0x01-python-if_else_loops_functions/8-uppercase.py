#!/usr/bin/python3
def uppercase(str):
    for s in str:
        s = ord(s)
        if (s >= 97 and s <= 122):
            s = (s - 97) + 65
        print("{:c}".format(s), end='')
    print()
