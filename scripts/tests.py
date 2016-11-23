#!/usr/bin/env python3

"""
tests.py: unit tests
"""

import unittest
import scripts.static_process as static_process
import scripts.thermal as thermal
import scripts.imaging as imaging
import numpy as np

class numerical_tests(unittest.TestCase):

    def test_pixel_to_temp(self):
        test_pixel_range=(0,255)
        test_temp_range=(20,30)
        input=100
        expected_output=23.92157
        actual_output=thermal.pixel_to_temp(test_temp_range,
                                                   test_pixel_range,input)
        self.assertAlmostEqual(actual_output, expected_output, places=5)

    def test_crop1(self):
        test_image=np.array([[1,2],[3,4]])
        test_params=(1,1,1,1)
        expected_cropped_image=np.array([[4]])
        actual_cropped_image=imaging.crop(test_params,test_image)
        result=np.array_equal(actual_cropped_image, expected_cropped_image)
        self.assertTrue(result)

    def test_crop2(self):
        test_image=np.array([[1,2],[3,4]])
        test_params=(0,0,2,1)
        expected_cropped_image=np.array([[1,2]])
        actual_cropped_image=imaging.crop(test_params,test_image)
        result=np.array_equal(actual_cropped_image, expected_cropped_image)
        self.assertTrue(result)

    def test_crop3(self):
        test_image=np.array([[1,2],[3,4]])
        test_params=(0,0,2,1)
        expected_cropped_image=np.array([[1]])
        actual_cropped_image=imaging.crop(test_params,test_image)
        result=np.array_equal(actual_cropped_image, expected_cropped_image)
        self.assertFalse(result)

    def test_verify_mask1(self):
        test_image=np.array([[1,2],[3,4]])
        test_mask=np.array([[True,False],[False,False]])
        result=imaging.verify_mask(test_image,test_mask)
        self.assertTrue(result)

    def test_verify_mask2(self):
        test_image=np.array([[1,2],[3,4]])
        test_mask=np.array([[True],[False,False]])
        result=imaging.verify_mask(test_image,test_mask)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()