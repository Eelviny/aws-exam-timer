# aws-exam-timer

A little python script to help you time your exam questions. There are 3 main variables that can be adjusted:

`questions` The number of questions you want to do

`seconds_per_question` The amount of time in seconds per question to reserve

`evaluation_seconds_per_question` The amount of time in seconds per question to reserve at the end. This will multiple the number of questions by the evaluation time to give a reserved time period.

For example, for the Solutions Architect Exam prep, 20 questions are provided. 2 minutes are budgeted per question, but each one should be answered within 90 seconds. 30 seconds per question is reserved at the end, totalling 10 minutes review time.
