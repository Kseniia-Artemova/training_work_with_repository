import os
from My_Packages.Homework_8 import utils as u

PATH_TO_FILE = os.path.join("questions.json")

pull_questions = u.create_pull_questions(PATH_TO_FILE)
questions = u.create_list_questions(len(pull_questions), pull_questions)

print("Игра начинается!")

for num, question in zip(range(1, len(questions) + 1), questions):
    print(question.build_question(num))
    question.is_ask = True
    question.user_answer = input()

    if question.is_correct():
        question.points_awarded = question.get_points()
        print(question.build_feedback(True))
    else:
        print(question.build_feedback(False))

u.print_statistics(questions)