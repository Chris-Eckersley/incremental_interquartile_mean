import unittest
from io import StringIO
import sys
from incremental_interquartile_mean import InterquartileMeanCalculator


class TestIncrementalInterQuartileMean(unittest.TestCase):
    def test_standard_output(self):
        """
        First test case with a small data set to encourage testing often.
        Original functionality did not print means of sets shorter than 4.
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
        print('done with test 1.')

    def test_performance(self):
        """
        The first few execution times were around 160 - 175 seconds.
        The assertion should probably be updated to a more performant max time.
        """
        calculator = InterquartileMeanCalculator()
        test_data_file = open('data.txt', 'r')
        import time
        start_time = time.time()
        for line in test_data_file:
            calculator.add_to_data(line)
            calculator.interquartile_mean()
        end_time = time.time()
        execution_time = end_time - start_time
        print('The interquartile_mean function execution time was:',
              execution_time)
        self.assertLess(execution_time, 60)


if __name__ == '__main__':
    unittest.main()
