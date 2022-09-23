#!/usr/bin/env bash

# Get exercise name (which also determines folder name)
# from user.
exercise_name=$1
echo $exercise_name

# Copy over fresh copies of files shared by all assignments from root
# folder to the specific exercise
cp run_autograder ./${exercise_name}/autograder/run_autograder
cp setup.sh ./${exercise_name}/autograder/setup.sh
cp limit_num_submissions.py ./${exercise_name}/autograder/limit_num_submissions.py

# Add a little file with exercise name.
# This will get pulled in by the autograder
# during grading so it knows what file name to look for.
echo "exercise_name=${exercise_name}" > ./${exercise_name}/autograder/exercise_name.sh

# Zip up the package to upload to gradescope.
today=$(date +"%Y_%m_%d_%H_%M")
cd ./${exercise_name}/autograder/
zip autograder_${today}.zip *
mv autograder_${today}.zip ../autograder_${today}.zip

# delete file shared by all assignments.
rm run_autograder setup.sh exercise_name.sh limit_num_submissions.py
