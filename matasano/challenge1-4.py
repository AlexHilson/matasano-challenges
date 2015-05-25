
#!/usr/bin/env python3

import json
import binary_conversions
import xor
import utilities

with open('./resources/set1-challenge4.txt') as inf:
    hexs = inf.readlines()

value = 0
for hex_in in hexs:
    xors = xor.one_char_hex_xor(hex_in.strip())
    for char in xors:
        new_value = utilities.english_check(char['decrypted'])
        if new_value > value:
            best_xor = char
            value = new_value

print(best_xor)
