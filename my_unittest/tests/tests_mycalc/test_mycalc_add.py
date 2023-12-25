# test_mycalc_add.py набор тестов для метода add

import unittest
from myunittest.src.mycalc.mycalc import MyCalc


class MyCalcAddTestsuite(unittest.TestCase):
    def setUp(self):
        self.calc = MyCalc()

    def test_add(self):
        """Тест для проверки двух положительных чисел"""
        self.assertEqual(15, self.calc.add_num(10, 5), "should bе 15")
