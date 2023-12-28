#!/usr/bin/python3
import sys

if __name__ != "__main__":
    sys.exit(1)

if len(sys.argv) <= 1:
    print("{} arguments.".format(len(sys.argv) - 1))
    sys.exit(0)

if (len(sys.argv) == 2):
    print("{} argument:".format(len(sys.argv) - 1))
else:
    print("{} arguments:".format(len(sys.argv) - 1))

for index, argv in enumerate(sys.argv[1:]):
    print("{}: {}".format(index + 1, argv))
