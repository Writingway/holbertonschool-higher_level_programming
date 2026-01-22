#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    roman_dictionary = {
            "X": 10,
            "I": 1,
            "V": 5,
            "L": 50,
            "C": 100,
            "D": 500,
    }
    total = 0
    for i in range(len(roman_string)):
        current = roman_dictionary[roman_string[i]]
        if i + 1 < len(roman_string) and \
           current < roman_dictionary[roman_string[i + 1]]:
            current = -current
            total += current
        else:
            total += current
    return total
