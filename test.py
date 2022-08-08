import unittest
from io import StringIO
import sys
import time
import csv
from statistics import mean
from incremental_interquartile_mean import InterquartileMeanCalculator


class TestIQMStandardOut(unittest.TestCase):
    def test_standard_output(self):
        """
        First test case with a small data set to encourage testing often.
        Original functionality did not print IQ means of sets shorter than 4.
        """
        calculator = InterquartileMeanCalculator()
        test_data_file = open('test_data/sm_data_set.txt', 'r')
        old_stdout = sys.stdout
        sys.stdout = capturedOutput = StringIO()
        for line in test_data_file:
            calculator.add_to_data(line)
            if len(calculator.data) > 3:
                print("%d: %.2f" % (
                    len(calculator.data),
                    calculator.interquartile_mean()))
        sys.stdout = old_stdout  # Reset redirect.
        sm_data_expectations = open('test_data/sm_expectation.txt', 'r')
        expect_string = ''
        for line in sm_data_expectations:
            expect_string += line
        self.assertEqual(capturedOutput.getvalue(), expect_string)
        test_data_file.close()
        sm_data_expectations.close()


class TestIQMPerfromance(unittest.TestCase):
    def test_performance(self):
        """
        The first few execution times were around 160 - 175 seconds.
        The assertion should probably be updated to a more performant max time.
        """
        calculator = InterquartileMeanCalculator()
        test_data_file = open('data.txt', 'r')
        start_time = time.time()
        for line in test_data_file:
            calculator.add_to_data(line)
            calculator.interquartile_mean()
        end_time = time.time()
        execution_time = end_time - start_time
        print('The interquartile_mean function execution time was:',
              execution_time)
        self.assertLess(execution_time, 60)
        test_data_file.close()


class TestInterface(unittest.TestCase):
    def test_interface(self):
        calculator = InterquartileMeanCalculator()
        calculator.add_to_data(300)
        self.assertEqual(len(calculator.data), 1)
        self.assertEqual(calculator.data[0], 300)


class TestInsertInPlace(unittest.TestCase):
    def test_interface(self):
        test_data = [299, 3, 0, 600, 4, 5, 0, 83]
        calculator = InterquartileMeanCalculator()
        for number in test_data:
            calculator.add_to_data(number)
        expectation = [0, 0, 3, 4, 5, 83, 299, 600]
        self.assertEqual(calculator.data, expectation)


class TestIQMDataFileResults(unittest.TestCase):
    """
    The original output skipped the first 3 outputs
    so I decided to take that step 2 literally.
    """
    def test_output(self):
        expectation_file = open('test_data/main_data_expect.csv', 'r')
        csv_reader = csv.reader(expectation_file, delimiter=',')
        data_txt_file = open('data.txt', 'r')
        calculator = InterquartileMeanCalculator()
        for line in data_txt_file:
            calculator.add_to_data(line)
            expectation = next(csv_reader)
            if len(calculator.data) > 3:
                self.assertEqual(
                    [len(calculator.data), calculator.interquartile_mean()],
                    [int(expectation[0]), float(expectation[1])]
                )
        expectation_file.close()
        data_txt_file.close()


class TestDataSetLessThanFour(unittest.TestCase):
    def test_output(self):
        test_data = [224, 213, 190, 199]
        expectations = iter([
            mean(test_data[:1]),
            mean(test_data[:2]),
            mean(test_data[:3]),
            206.0
        ])
        calculator = InterquartileMeanCalculator()
        for number in test_data:
            with self.subTest(line=number):
                calculator.add_to_data(number)
                self.assertEqual(
                    next(expectations),
                    calculator.interquartile_mean()
                )


class TestIQMWithZeros(unittest.TestCase):
    def test_output(self):
        test_data = [0, 0, 0, 0, 0, 0, 10, 11]
        expectations = iter([
            mean(test_data[:1]),
            mean(test_data[:2]),
            mean(test_data[:3]),
            0,
            0,
            0,
            0,
            0
        ])
        calculator = InterquartileMeanCalculator()
        for number in test_data:
            with self.subTest(line=number):
                calculator.add_to_data(number)
                self.assertEqual(
                    next(expectations),
                    calculator.interquartile_mean()
                )


class TestIQRToSixHundred(unittest.TestCase):
    def test_output(self):
        with open('test_data/data_set_0-600.txt', 'r') as data_txt_file:
            calculator = InterquartileMeanCalculator()
            for line in data_txt_file:
                calculator.add_to_data(line)
            self.assertEqual(calculator.interquartile_mean(), 358.2574)


if __name__ == '__main__':
    unittest.main()
