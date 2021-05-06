import os
import sys
import unittest
import parse_log2
# import parse_log


arg = sys.argv[1]


class BasicTestSuite(unittest.TestCase):
    """
    Basic test cases
    """
    # def test_open_file(self, arg):
    #     self.assertNotEqual(parse_log2.open_file(arg), None)
    def test_input_output(self):
        self.assertEqual(
            "09:20-11:00 Introduction",
            "Introduction              100 minutes   75%")
        self.assertEqual(
            "11:00-11:15 Exercises",
            "Exercices                  15 minutes   11%")
        self.assertEqual(
            "11:15-11:35 Break",
            "Break                      20 minutes   15%")

    def test_times(self, hours):
        self.assertEqual(parse_log2.times("09:20-11:00"), 100)



if __name__ == '__main__':
    unittest.main()
