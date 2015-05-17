#!/usr/bin/env python3

'''
Wrapper around binascii for binary/ascii conversions.
Not much wrapping done, but the syntax is easier + challenge 1 calls for it.
'''


import binascii


def hex2base64(hex_in):
    return binascii.b2a_base64(binascii.unhexlify(hex_in))[:-1]


def hex_to_binary(hex_in):
    return binascii.a2b_hex(hex_in)


def binary_to_hex(bin_in):
    return binascii.b2a_hex(bin_in)


def base64_to_binary(base_in):
    return binascii.a2b_base64(base_in)


def binary_to_base64(bin_in):
    # binascii base64 encoding returns an additional new line
    return binascii.b2a_base64(bin_in)[:-1]


def hex_to_base64(hex_in):
    return binary_to_base64(hex_to_binary(hex_in))


def base64_to_hex(base_in):
    return binary_to_hex(base64_to_binary(base_in))
