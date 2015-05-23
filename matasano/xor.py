#!/usr/bin/env python3

import binary_conversions


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
        xors.append(key_xor(binary, key))
    return xors
