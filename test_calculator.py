import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    ######### Partner 2
    def test_add(self): # 3 assertions
        # fill in code
        self.assertEqual(add(3,2), 5)
        self.assertEqual(add(6,2), 8)
        self.assertEqual(add(4,7), 11)


    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(5,2), 3)
        self.assertEqual(sub(6,2), 4)
        self.assertEqual(sub(8,3), 5)


    ######## Partner 1
    def test_multiply(self):# 3 assertions
        self.assertEqual(multiply(1,2),2)
        self.assertEqual(multiply(3,4),12)
        self.assertEqual(multiply(3,9),27)

    #     fill in code

    def test_divide(self): # 3 assertions
        self.assertEqual(divide(3,9),3)
        self.assertEqual(divide(3,12),4)
        self.assertEqual(divide(4,12),3)

    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     div(0, 5)

        with self.assertRaises(ZeroDivisionError):
            divide(0,5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2,2), math.log(2, 2))
        self.assertEqual(logarithm(3,3), math.log(3, 3))
        self.assertEqual(logarithm(4,4), math.log(4, 4))

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(2,0)
    #     # use same technique from test_divide_by_zero

    
    ######## Partner 1
    def test_log_invalid_argument(self):# 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0,5)
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4),5)
        self.assertEqual(hypotenuse(6,8),10)
        self.assertEqual(hypotenuse(9,12),15)
    #     fill in code

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-2)
        self.assertEqual(square_root(9),3)
        self.assertEqual(square_root(16),4)


    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()