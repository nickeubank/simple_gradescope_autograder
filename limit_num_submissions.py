import json
import re

SUBMISSION_LIMIT = 3

#############
# Count Past Submissions.
#############

with open("/autograder/submission_metadata.json") as json_file:
    meta = json.load(json_file)

# Get submissions and filter out events where autograder failed
submissions = []
for s in meta["previous_submissions"]:
    if not re.match("The autograder failed", str(s["results"]["output"])):
        submissions.append(s)

# Len is just PREVIOUS submissions,
# so add 1 to get total submissions
# including current.
count = len(submissions) + 1

#############
# Print status
#############

valid_submission_message = f"""
*********************************************
Including this submission, you have submitted a 
total of {count} of your {SUBMISSION_LIMIT} allowed
submissions.

Note that submissions where the autograder
fails will not be counted against your 
submission count.
*********************************************
"""

invalid_submission_message = f"""
*********************************************
Including this submission, you have submitted a 
total of {count} submissions.

You are only allowed {SUBMISSION_LIMIT} submissions. 

You will be graded on the basis of your last valid 
submission, output for which you will see now.
*********************************************
"""

# Print Message and, if above limit, save last valid

if count <= SUBMISSION_LIMIT:
    print(valid_submission_message)
else:
    print(invalid_submission_message)
    last_valid_result = submissions[SUBMISSION_LIMIT - 1]["results"]
    last_valid_result["output"]
    with open("/autograder/results/results.json", "w") as json_results:
        json_results.write(json.dumps(last_valid_result, indent=4))
