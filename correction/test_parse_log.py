import unittest
from .parse_log import parse_line, parse_file
import io


class TestParseLog(unittest.TestCase):
    def test_parse_line(self):
        self.assertEqual(parse_line("11:15-11:35 Break"),
                         ("Break", 20))
        self.assertEqual(parse_line("09:30-10:30 Lists and Tuples"),
                         ("Lists and tuples", 20))
        self.assertEqual(parse_line("11:15-11:45 Break"),
                         ("Break", 30))
        self.assertEqual(parse_line("11:00-11:15 Exercises"),
                         ("Exercises", 15))
        self.assertEqual(parse_line("11:35-12:30 Numbers and strings"),
                         ("Numbers and strings", 55))
        self.assertIsNone(parse_line(""))

    @unittest.skip("optional idea : compute times > 24h")
    def test_parse_line(self):
        self.assertEqual(parse_line("11:35-11:15 Break"), ("Break", -20))

    def test_parse_file(self):
        data1 = "09:20-11:00 Introduction\n"\
            "11:00-11:15 Exercises\n"\
            "11:15-11:35 Break\n"\
            "11:35-12:30 Numbers and strings\n"\
            "12:30-13:30 Lunch Break\n"
        # total : 250
        dur = {"Introduction": 100, "Exercises": 15, "Break": 20,
               "Numbers and strings": 55, "Lunch Break": 60}
        cpt = {"Introduction": 1, "Exercises": 1, "Break": 1,
               "Numbers and strings": 1, "Lunch Break": 1}

        with io.StringIO(data1) as f:
            self.assertEqual(parse_file(f), (cpt, dur))

        data2 = "09:30-10:30 Lists and Tuples\n"\
                "10:30-10:50 Break\n"\
                "10:50-12:00 Exercises\n"\
                "12:00-12:30 Solutions\n"\
                "12:30-12:45 Dictionaries\n"\
                "12:45-14:15 Lunch Break\n"\
                "14:15-16:00 Exercises\n"\
                "16:00-16:15 Solutions\n"\
                "16:15-16:30 Break\n"\
                "16:30-17:00 Functions\n"\
                "17:00-17:30 Exercises"

        dur = {"Exercises": 205, "Break": 35, "Solutions": 45,
               "Dictionaries": 15, "Lunch Break": 90, "Functions": 30,
               "Lists and Tuples": 60}
        cpt = {"Exercises": 3, "Break": 2, "Solutions": 2, "Dictionaries": 1,
               "Lunch Break": 1, "Functions": 1, "Lists and Tuples": 1}

        with io.StringIO(data2) as f:
            self.assertEqual(parse_file(f), (cpt, dur))


if __name__ == "__main__":
    unittest.main()
