#!/usr/bin/env python3

import json


def english_check(binary_in):
    with open('./resources/letter_frequencies.json') as inf:
        letter_frequencies = json.load(inf)
    value = 0
    for byte in binary_in:
        char = chr(byte).lower()
        try:
            value += letter_frequencies[char]
        except KeyError:
            pass
    return value


def hamming_distance(str1, str2):
    #http://stackoverflow.com/q/16926130
    bin1 = [format(ord(char), '#010b') for char in str1]
    bin2 = [format(ord(char), '#010b') for char in str2]

    dist = 0
    for byte1, byte2 in zip(bin1, bin2):
        dist += sum(bit1 != bit2 for bit1, bit2 in zip(byte1, byte2))
    return dist
