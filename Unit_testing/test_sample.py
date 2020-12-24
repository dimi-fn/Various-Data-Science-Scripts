# It is a good practise the name of the file to start with "test_"

# https://github.com/CoreyMSchafer/code_snippets/tree/master/Python-Unit-Testing

import unittest

# importing the name of file script to test
import unit_test_sample

# https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug

class TestSample(unittest.TestCase):
    # it should always start with "test_"
    ## otherwise, although the test will be conducted, the number of tests shown will be 0
    def test_add(self):

        # result= unit_test_sample.add(5,3)
        # self.assertEqual(result, 8)
        ## Integrating the two above lines into one
        self.assertEqual(unit_test_sample.add(5,3), 8)

        # adding more tests
        ## It still will be considered as 1 test, but we validate it more with different test methods for the same goal
        self.assertEqual(unit_test_sample.add(5,-3), 2)
        self.assertEqual(unit_test_sample.add(-5,-3), -8)

    def test_substract(self):
        self.assertEqual(unit_test_sample.substract(5, 3), 2)
        self.assertEqual(unit_test_sample.substract(5,-3), 8)
        self.assertEqual(unit_test_sample.substract(-5,-3), -2)

    def test_multiply(self):
        self.assertEqual(unit_test_sample.multiply(5, 3), 15)
        self.assertEqual(unit_test_sample.multiply(5,-3), -15)
        self.assertEqual(unit_test_sample.multiply(-5,-3), 15)

    def test_divide(self):
        self.assertEqual(unit_test_sample.divide(10, 5), 2)
        self.assertEqual(unit_test_sample.divide(10,-5), -2)
        self.assertEqual(unit_test_sample.divide(-10,-5), 2)
        
        # testing for when dividing by zero (testing the exception)
        self.assertRaises(ValueError, unit_test_sample.divide, 10, 0)

        # another way of testing the exception:
        with self.assertRaises(ValueError):
            unit_test_sample.divide(10, 0)

# in order to run the unit test here, and not from the cmd
'''
if we run this module directly, then below we ask to run the code within
the conditional. The code within our conditional is the "unittest.main()",
and this will run the tests.
'''
if __name__ == "__main__":
    unittest.main()