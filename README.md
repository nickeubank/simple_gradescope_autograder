# A Simple Gradescope Auto Grader

This folder is designed to hold multiple exercises, then build autograders for each exercise separately. 

In the root are the two main files required for all autograders: `run_autograder` and `setup.sh`. Since these don't have to change from exercise to exercise, a single copy of these files lives in the root directory.

Each exercise is then placed in a subfolder. Within that folder is a Solution notebook and an `autograder` folder. The Solution notebook should store all solutions in a JSON file that gets put into `autograder` as `solutions.json` with variable names as keys and solutions as values.

Any adjustments to required packages can be made to the `environment.yml` file.

And finally tests should be placed in `test_submitted_answers.py`. This file will run the code in the submitted notebook prior to tests being run, so any variables defined in the submitted notebook will be visible to the tests.

When you're ready to build an autograder, simply use the `build_autograder.sh` script in the root directory with the name of the exercise (e.g., `bash build_autograder.sh exercise_example`. That will:

- Copy the `run_autograder` and `setup.py` files into the exercise's autograder folder, 
- add a little helper file with the name of the exercise to be sourced by the `run_autograder` file, 
- zip the contents,
- erase the copies of `run_autograder` and `setup.py` (so we only have to worry about one canonical version of each).

Then just submit the zipped file to Gradescope!.com

## Two grading models 

Note there are two models of the test file. One has explicit tests (`test_submitted_answers.py`), and one has parametrized tests that just cycle over the dict keys from the solutions file (currently `optional_test_submitted_answers_parametrize.py`). The former allows for different scoring per question and more informative error messages, while the latter is just easier. :)

## Directions to students

What I've given students on these:

### Gradescope Autograding

This assignment will be autograded using a NEW autograder I've setup on gradescope. Unlike the last autograder we tried—where you had to put your answers in a special notebook—this autograder will accept any jupyter notebook, with the only requirements being, for this assignment: 

- you only import pandas and numpy
- you import data **from a URL** (since the autograder in the cloud won't see your file system)
- you name your notebook file `exercise_missing.ipynb`
- you store your solutions in a dictionary called `results` with answers tied to the keys provided in the prompts below.

Your notebook will be executed by the autograder and the value of identified variables will then be checked against solution values. And that's it for the autograder, though be aware TAs will _also_ review your notebooks for answers to other questions and styling.

You can check that you have answers for all questions in your `results` dictionary with this code:

```python
assert set(results.keys()) == {
 'EX2_AVG_INCOME',
 'EX3_SHARE_MAKING_9999999',
 'EX3_SHARE_MAKING_ZERO',
 'EX5_AVG_INCOME',
 'EX8_AVG_INCOME_BLACK',
 'EX8_AVG_INCOME_WHITE',
 'EX8_RACIAL_DIFFERENCE',
 'EX9_AVG_INCOME_BLACK',
 'EX9_AVG_INCOME_WHITE',
 'EX10_WAGE_GAP'}
 ```

#### Submission Limits

There is one other significant change from the old autograder, however; namely you are **only allowed three submissions to the autograder.** Your last submission (if you submit 3 or fewer times), or your third submission (if you submit more than 3 times) will determine your grade. 

Why?

In software development, we can run our test suite as many times as we want. Indeed, we are encouraged to do so with Continuous Integration tools. But in Data Science, we generally never know if our answer is actually *right*. Instead, we have to learn to think carefully as we write our code and make sure that our intermediate results make sense, because the whole point of generating a new result is that it's something we didn't know before!

In this class, however, I would also like to provide the opportunity to learn from your mistakes and iterate, and so I'd like to try using this "three submission" model as a compromise.
