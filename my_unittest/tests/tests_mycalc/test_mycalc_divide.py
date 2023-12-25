# test_mycalc_divide.py набор тестов дпя метода divide

import unittest
from myunittest.src.mycalc.mycalc import MyCalc


class MyCalcDivideTestSuite(unittest.TestCase):
    def setUp(self):
        self.calc = MyCalc()

    def test_divide(self):
        """тест дпя проверки двух положительных чисел"""
        self.assertEqual(2, self.calc.divide(10, 5), "should bе 2")
