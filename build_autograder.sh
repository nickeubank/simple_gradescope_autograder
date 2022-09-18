#!/usr/bin/env bash

exercise_name=$1
echo $exercise_name
cp run_autograder ./${exercise_name}/autograder/run_autograder
cp setup.sh ./${exercise_name}/autograder/setup.sh
echo "exercise_name=${exercise_name}" > ./${exercise_name}/autograder/exercise_name.sh
today=$(date +"%Y_%m_%d_%H_%M")
cd ./${exercise_name}/autograder/
zip autograder_${today}.zip *
mv autograder_${today}.zip ../autograder_${today}.zip
rm run_autograder setup.sh exercise_name.sh
