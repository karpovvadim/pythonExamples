import unittest
from test_mycalc_add import MyCalcAddTestsuite
from test_mycalc_substract import MyCalcSubtractTestsuite
from test_mycalc_multiply import MyCalcMultiplyTestSuite
from test_mycalc_divide import MyCalcDivideTestSuite


def run_mytests():
    test_classes = [MyCalcAddTestsuite, MyCalcSubtractTestsuite,
                    MyCalcMultiplyTestSuite, MyCalcDivideTestSuite]
    loader = unittest.TestLoader()
    test_suites = []
    for t_class in test_classes:
        suite = loader.loadTestsFromTestCase(t_class)
        test_suites.append(suite)
    final_suite = unittest.TestSuite(test_suites)
    runner = unittest.TextTestRunner()
    results = runner.run(final_suite)
    print(results)


if __name__ == '__main__':
    run_mytests()
