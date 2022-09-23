import pytest_utils
import json
from pytest_utils.decorators import max_score, visibility, tags

with open("solutions.json") as json_file:
    solutions = json.load(json_file)

exec(open("submission_script.py").read())


@max_score(1)
def test_exercise1():
    if EX1 != solutions["EX1"]:
        raise IncorrectAnswer("Exercise 1 is incorrect.")


@max_score(1)
def test_exercise2():
    if EX2 != solutions["EX2"]:
        raise IncorrectAnswer("Exercise 2 is incorrect.")


class IncorrectAnswer(Exception):
    """Raised when student fails."""
