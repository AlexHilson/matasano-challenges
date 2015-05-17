#!/usr/bin/env python3

def hex2base64(hex_in):
    import binascii
    return binascii.b2a_base64(binascii.unhexlify(hex_in))[:-1]
