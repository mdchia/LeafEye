#!/usr/bin/env python3

"""
tests.py: unit tests
"""

import unittest
import scripts.static_process as static_process

class numerical_tests(unittest.TestCase):

    def test_pixel_to_temp(self):
        test_pixel_range=(0,255)
        test_temp_range=(20,30)
        input=100
        expected_output=23.92157
        actual_output=static_process.pixel_to_temp(test_temp_range,
                                                   test_pixel_range,input)
        self.assertAlmostEqual(actual_output, expected_output, places=5)

if __name__ == '__main__':
    unittest.main()