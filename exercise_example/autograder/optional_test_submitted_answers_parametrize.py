import pytest_utils
import pytest
import json
import numpy as np
from pytest_utils.decorators import max_score, visibility, tags

with open("solutions.json") as json_file:
    solutions = json.load(json_file)

exec(open("submission_script.py").read())

keys = list(solutions.keys())
keys.sort()
pairs = [pytest.param(results[i], solutions[i], id=i) for i in keys]


@pytest.mark.parametrize(("submission", "solution"), pairs)
@max_score(1)
def test_grading(submission, solution):
    if not np.isclose(submission, solution):
        raise IncorrectAnswer("Answer not correct")


class IncorrectAnswer(Exception):
    """Raised when student fails."""
