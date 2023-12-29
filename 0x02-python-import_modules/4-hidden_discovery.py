#!/usr/bin/python3
import hidden_4

if __name__ != "__main__":
    sys.exit(1)

name = dir(hidden_4)
for n in name:
    if n[0] == "_" and n[1] == "_":
        continue
    print(f"{n}")
