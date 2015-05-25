
#!/usr/bin/env python3

import xor
import utilities


with open('./resources/set1-challenge4.txt') as inf:
    hexs = inf.readlines()

decrypted = []
for hex_in in hexs:
    xors = xor.one_char_hex_xor(hex_in.strip())
    decrypted += xors

print(sorted(decrypted, key = lambda key: utilities.english_check(key['decrypted']))[-1])
