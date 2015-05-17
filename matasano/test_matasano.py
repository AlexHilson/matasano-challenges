#!/usr/bin/env python3

import unittest
import binary_conversions
import xor


class test_hex_to_base64(unittest.TestCase):
    '''Challenge 1, Set 1'''

    def test_convert_success(self):
        test_in = b'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
        test_out = b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
        self.assertEqual(binary_conversions.hex_to_base64(test_in), test_out)

    def test_convert_failure(self):
        test_in = b'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
        test_out = b'SSdt'
        self.assertNotEqual(binary_conversions.hex_to_base64(test_in), test_out)


class test_xor(unittest.TestCase):
    '''Challenge 1, Set 2'''

    def test_fixed_xor_success(self):
        hex1 = b'1c0111001f010100061a024b53535009181c'
        hex2 = b'686974207468652062756c6c277320657965'
        expected = b'746865206b696420646f6e277420706c6179'
        self.assertEqual(xor.hex_xor(hex1, hex2), expected)

    def test_fixed_xor_failure(self):
        hex1 = b'1c0111001f010100061a024b53535009181c'
        hex2 = b'686974207468652062756c6c277320657965'
        expected = b'179'
        self.assertNotEqual(xor.hex_xor(hex1, hex2), expected)


if __name__ == '__main__':
    unittest.main()