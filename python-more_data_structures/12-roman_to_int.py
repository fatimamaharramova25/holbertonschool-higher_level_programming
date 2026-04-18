#!/usr/bin/python3
""" Roman to Integer module """


def roman_to_int(roman_string):
    """ Converts a Roman numeral to an integer """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    rd = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    for i in range(len(roman_string)):
        current = rd.get(roman_string[i], 0)
        next_v = rd.get(roman_string[i + 1], 0) if i + 1 < len(roman_string)             else 0
        if next_v > current:
            num -= current
        else:
            num += current
    return num
