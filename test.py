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


if __name__ == '__main__':
    unittest.main()
