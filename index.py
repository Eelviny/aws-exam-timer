from time import sleep, gmtime, strftime

questions = 20
seconds_per_question = 90
evaluation_seconds_per_question = 30

time_per_question = strftime('%M:%S', gmtime(seconds_per_question))
evaluation_time_per_question = strftime('%M:%S', gmtime(evaluation_seconds_per_question))

total_time = strftime('%H:%M:%S', gmtime(questions * (seconds_per_question + evaluation_seconds_per_question)))
evaluation_time = strftime('%M:%S', gmtime(questions * evaluation_seconds_per_question))
print(f"Starting timer for {questions} questions, {time_per_question} minutes per question with an extra {evaluation_time} minutes ({evaluation_time_per_question} per question) reserved for review at the end.")
print(f"Total time: {total_time}\n")

sleep(5)

for q in range(1, questions + 1):
    for timer in range(seconds_per_question):
        print(f"Question {q}: {strftime('%M:%S', gmtime(timer))} / {time_per_question}", end="\r")
        sleep(1)
    print(f"Question {q}: time's up!                   ")

evaluation_seconds = questions * evaluation_seconds_per_question
evaluation_time = strftime('%M:%S', gmtime(evaluation_seconds))

for timer in range(evaluation_seconds):
    print(f"Question review time: {strftime('%M:%S', gmtime(timer))} / {evaluation_time}", end="\r")
    sleep(1)

print(f"Question review time: time's up!                \n")
print("Exam time is over, pens down.")
