#!/usr/bin/env python3


def english_check(binary_in):
    with open('./resources/letter_frequencies.json') as inf:
        letter_frequencies = json.load(inf)
    value = 0
    for byte in binary_in:
        char = chr(byte).upper()
        try:
            value += letter_frequencies[char]
        except KeyError:
            pass
    return value
