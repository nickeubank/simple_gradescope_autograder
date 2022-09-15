import pytest_utils
import json
from pytest_utils.decorators import max_score, visibility, tags

with open("submitted_answers.json") as json_file:
    submitted_answers = json.load(json_file)


@max_score(1)
def test_exercise1():
    assert submitted_answers["EX1"] == 42


def test_exercise2():
    assert submitted_answers["EX2"] == 42
