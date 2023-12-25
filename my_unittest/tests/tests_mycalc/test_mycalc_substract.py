# test_mycalc_subtract.py набор тестов для метода subtract

import unittest
from myunittest.src.mycalc.mycalc import MyCalc


class MyCalcSubtractTestsuite(unittest.TestCase):
    def setUp(self):
        self.calc = MyCalc()

    def test_subtract(self):
        """Тест для проверки двух положительных чисел"""
        self.assertEqual(5, self.calc.subtract(10, 5), "should bе 5")
