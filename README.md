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