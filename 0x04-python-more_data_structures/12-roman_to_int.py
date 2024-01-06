#!/usr/bin/python3

def roman_to_int(roman_string):
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    if roman_string is None and type(roman_string) is not str:
        return num

    prev = 0
    for x in roman_string:
        if x in rom:
            if rom[x] > prev and num != 0:
                num = (num + rom[x]) - (prev * 2)
            else:
                num += rom[x]
            prev = rom[x]

    return num
