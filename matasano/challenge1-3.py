#!/usr/bin/env python3

import json
import binary_conversions
import xor


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

hex_in = b'1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
xors = xor.one_char_hex_xor(hex_in)
print(sorted(xors, key=english_check, reverse=True)[0])
