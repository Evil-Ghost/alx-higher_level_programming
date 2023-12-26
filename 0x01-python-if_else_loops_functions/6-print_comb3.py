#!/usr/bin/python3
for i in range(0, 10):
    j = i + 1
    while (j < 10):
        if (i != 8 or j != 9):
            print("{}{}".format(i, j), end=', ')
        else:
            print("{}{}".format(i, j))
        j += 1
