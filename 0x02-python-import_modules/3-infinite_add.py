#!/usr/bin/python3
import sys
sum = 0

if __name__ != "__main__":
    sys.exit(0)

if len(sys.argv) <= 1:
    print(f"{sum}")
    sys.exit(1)

for argv in sys.argv[1:]:
    sum += int(argv)

print(f"{sum}")
