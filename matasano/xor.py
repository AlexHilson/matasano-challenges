#!/usr/bin/env python3

import binary_conversions
import itertools


def bin_xor(bin1, bin2):
    bin3 = []
    for byte1, byte2 in zip(bin1, bin2):
        bin3.append(byte1 ^ byte2)
    return bytearray(bin3)


def hex_xor(hex1, hex2):
    bin1 = binary_conversions.hex_to_binary(hex1)
    bin2 = binary_conversions.hex_to_binary(hex2)
    return binary_conversions.binary_to_hex(bin_xor(bin1, bin2))


def key_xor(binary, key):
    output = []
    for byte in binary:
        output.append(byte ^ key)
    return bytearray(output)


def one_char_hex_xor(hex_in):
    binary = binary_conversions.hex_to_binary(hex_in)
    xors = []
    for key in range(256):
        xors.append({'key': chr(key),
                     'decrypted': key_xor(binary, key),
                     'encrypted': hex_in })
    return xors


def repeating_key_bin_xor(bin_in, key):
    '''
    Expects bin_in and key as bytearrays.
    '''
    keys = itertools.cycle(key)
    bytes_keys = [(x, next(keys)) for x in bin_in]
    return bytearray([byte[0] ^ byte[1] for byte in bytes_keys])
