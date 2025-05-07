import unittest
import importlib

class TestAssignmentSeven(unittest.TestCase):
    def test_01(self):
        self.assertEqual(answers.answer_01(1, 2, 3), [False, True, True])
        self.assertEqual(answers.answer_01(4, 5, 6), [False, True, False])
        self.assertEqual(answers.answer_01(7, 11, 13, 17, 19), [True, True, True, True, True])
        self.assertEqual(answers.answer_01(20, 21, 22, 24, 25, 26, 27), [False, False, False, False, False, False, False])
    def test_02(self):
        self.assertEqual(answers.answer_02(1, 5), [2, 3, 5])
        self.assertEqual(answers.answer_02(6, 10), [7])
        self.assertEqual(answers.answer_02(11, 15), [11, 13])
    def test_03(self):
        self.assertEqual(answers.answer_03(5), [2, 3, 5, 7, 11])
        self.assertEqual(answers.answer_03(10), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
        self.assertEqual(answers.answer_03(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113])
    def test_04(self):
        self.assertEqual(answers.answer_04(-3, -2, -1, 0, 1, 2, 3), [9, 4, 1])
        self.assertEqual(answers.answer_04(-3, 0, 1, 2, 3, -2, -1), [9, 4, 1])
        self.assertEqual(answers.answer_04(0, 1, 2, 3, -1, -2, -3), [1, 4, 9])
    def test_05(self):
        self.assertEqual(answers.answer_05(tw="twn"), {'TW': 'TWN'})
        self.assertEqual(answers.answer_05(tw="twn", jp="jpn"), {'TW': 'TWN', 'JP': 'JPN'})
        self.assertEqual(answers.answer_05(tw="twn", jp="jpn", lt="ltu"), {'TW': 'TWN', 'JP': 'JPN', 'LT': 'LTU'})

chapter_name = "使用函數組織程式碼"
answers = importlib.import_module("answers")
suite = unittest.TestLoader().loadTestsFromTestCase(TestAssignmentSeven)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print(f"您在「{chapter_name}」章節的 {number_of_test_runs} 道練習題中答對了 {number_of_successes} 題。")