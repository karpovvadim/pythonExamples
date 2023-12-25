# test_myadd.py набор тестов для функции myadd

import unittest
from myunittest.src.myadd.myadd import add


class MyAddTestsuite(unittest.TestCase):
    def test_add1(self):
        """Тест для проверки сложения двух положительных чисел"""
        self.assertEqual(15, add(10, 5), "should be 15")

    def test_add2(self):
        """Тест для проверки сложения положительного и отрицательного чисел"""
        self.assertEqual(5, add(10, -5), "should Ье 5")

    def test_add3(self):
        """Тест для проверки сложения отрицательного и положительного чисел"""
        self.assertEqual(-5, add(-10, 5), "should Ье -5")

    def test_add4(self):
        """Тест для проверки сложения двух отрицательных чисел"""
        self.assertEqual(-15, add(-10, -5), "should Ье -15")


if __name__ == '__main__':
    unittest.main()
