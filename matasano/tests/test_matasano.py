#!/usr/bin/env python3

import unittest
import matasano

class test_hex_to_base64(unittest.TestCase):

    def test_convert(self):
        test_in = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
        test_out = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
        self.assertEqual(matasano.hex2base64(test_in), test_out)
