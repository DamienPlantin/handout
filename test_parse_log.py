import unittest
from parse_log_damien import open_file, times, add_dict, expected_output


class BasicTestSuite(unittest.TestCase):
    """
    Basic test cases
    """
    def test_open_file(self):
        hours = ['09:20-11:00', '11:00-11:15', '11:15-11:35']
        matters = ['Introduction', 'Exercises', 'Break']
        self.assertEqual(open_file("test_planning.log"), (matters, hours))
        self.assertIsNotNone(open_file("test_planning.log"))
        self.assertIsInstance(open_file("test_planning.log"), tuple)

    def test_times(self):
        hours = ['09:20-11:00', '11:00-11:15', '11:15-11:35']
        matters = ['Introduction', 'Exercises', 'Break']
        result = [('Introduction', 100), ('Exercises', 15), ('Break', 20)]
        self.assertEqual(times(matters, hours), result)
        self.assertIsNotNone(times(matters, hours))
        self.assertIsInstance(times(matters, hours), list)

    def test_add_dict(self):
        result = [('Introduction', 100), ('Exercises', 15), ('Break', 20)]
        total = 135
        output = {'Break': 20, 'Exercises': 15, 'Introduction': 100}
        self.assertEqual(add_dict(result), (total, output))
        self.assertIsNotNone(add_dict(result))
        self.assertIsInstance(add_dict(result), tuple)

    def test_expected_output(self):
        total = 20
        output = {'Break': 20}
        finished = "Break                      20 minutes  100%"
        self.assertEqual(expected_output(total, output), finished)
        self.assertIsInstance(expected_output(total, output), str)
        self.assertIsNotNone(expected_output(total, output))


if __name__ == '__main__':
    unittest.main()
