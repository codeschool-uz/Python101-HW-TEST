import unittest

from def01 import func_no_param1
# from def06 import func_no_param6
from def07 import func_hi1
from def08 import func_hi2
from def09 import func_pi5
from def10 import func_pi10
from def11 import func_sumdigit2
from def12 import func_multiply_digit2
from def13 import func_sumdigits
from def14 import func_multiply_digits
from def15 import func_count_even
from def16 import func_count_odd
from def17 import func_sum_even

class Test(unittest.TestCase):

    def test_func_no_param1(self):
        output = func_no_param1()
        actual = 0
        self.assertEqual(actual, output)

    # def test_func_no_param6(self):
    #     output = func_no_param6()
    #     actual = 6
    #     self.assertEqual(actual, output)

    def test_func_hi1(self):
        output = func_hi1()
        actual = "Hello, World!"
        self.assertEqual(actual, output)

    def test_func_hi2(self):
        output = func_hi2()
        actual = "codeschooluz"
        self.assertEqual(actual, output)

    def test_func_pi5(self):
        output = func_pi5()
        actual = 3.14159
        self.assertEqual(actual, output)
    
    def test_func_pi10(self):
        output = func_pi10()
        actual = 3.1415926536
        self.assertEqual(actual, output)

    def test_func_sumdigit2(self):
        output = func_sumdigit2(34)
        actual = 7
        self.assertEqual(actual, output)

    def test_func_multiply_digit2(self):
        output = func_multiply_digit2(23)
        actual = 6
        self.assertEqual(actual, output)

    def test_func_sumdigits(self):
        output = func_sumdigits(23251)
        actual = 13
        self.assertEqual(actual, output)
    
    def test_func_multiply_digits(self):
        output = func_multiply_digits(11233)
        actual = 18
        self.assertEqual(actual, output)
    
    def test_func_count_even(self):
        output = func_count_even(62134)
        actual = 3
        self.assertEqual(actual, output)

    def test_func_count_odd(self):
        output = func_count_odd(62349)
        actual = 2
        self.assertEqual(actual, output)
    
    def test_func_sum_even(self):
        output = func_sum_even(234)
        actual = 6
        self.assertEqual(actual, output)



 
  