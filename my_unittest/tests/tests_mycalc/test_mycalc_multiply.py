# test_mycalc_multiply.py набор тестов для метода multiply

import unittest
from myunittest.src.mycalc.mycalc import MyCalc


class MyCalcMultiplyTestSuite(unittest.TestCase):
    def setUp(self):
        self.calc = MyCalc()

    def test_multiply(self):
        """Тест дпя проверки двух положительных чисел"""
        self.assertEqual(50, self.calc.multiply(10, 5), "should bе 50")
