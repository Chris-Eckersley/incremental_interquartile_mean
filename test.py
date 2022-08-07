import unittest
from io import StringIO
import sys
from incremental_interquartile_mean import interquartile_mean


class TestIncrementalInterQuartileMean(unittest.TestCase):
    def test_standard_output(self):
        test_data_file = open('test_data/sm_data_set.txt', 'r')
        old_stdout = sys.stdout
        sys.stdout = capturedOutput = StringIO()
        interquartile_mean(test_data_file)
        sys.stdout = old_stdout  # Reset redirect.
        sm_data_expectations = open('test_data/sm_expectation.txt', 'r')
        expect_string = ''
        for line in sm_data_expectations:
            expect_string += line
        self.assertEqual(capturedOutput.getvalue(), expect_string)

    def test_performance(self):
        from timeit import timeit
        setup = "from incremental_interquartile_mean import interquartile_mean;" \
                " test_data_file = open('data.txt', 'r')"
        execution_time = timeit(stmt="interquartile_mean(test_data_file)",
                                setup=setup, number=5)
        print('The interquartile_mean function execution time was:',
              execution_time)
        # The last few executions were around 160 - 175 seconds.
        self.assertLess(execution_time, 200)


if __name__ == '__main__':
    unittest.main()
