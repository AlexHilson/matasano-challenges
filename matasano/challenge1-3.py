#!/usr/bin/env python3

import json
import binary_conversions
import xor
import utilities


hex_in = b'1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
xors = xor.one_char_hex_xor(hex_in)
print(sorted(xors, key=utilities.english_check, reverse=True)[0])
