import json
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number


class TestJupyterModel(unittest.TestCase):
    def setUp(self):
        with open("saved_results.json") as json_file:
            results = json.load(json_file)
        self.results = results

    @weight(1)
    @number(1)
    def test_exercise1(self):
        val = self.results["EX1"]
        print(val)
        self.assertEqual(val, 42)

    @weight(1)
    @number(1)
    def test_exercise2(self):
        val = self.results["EX2"]
        print(val)
        self.assertEqual(val, 42)
