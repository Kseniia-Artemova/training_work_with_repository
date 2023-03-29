import json
from random import shuffle
from My_Packages.Homework_8.class_Question import *


def create_pull_questions(path_file: str) -> list:
    with open(path_file, "r", encoding="utf-8") as file:
        pull_questions = json.load(file)
        shuffle(pull_questions)
    return pull_questions


def create_list_questions(length: int, data: list) -> list:
    questions = create_list_objects(length)

    for question, properties in zip(questions, data):
        for field, value in properties.items():
            setattr(question, field, value)

    return questions


def create_list_objects(length: int) -> list:
    questions = []

    for i in range(1, length + 1):
        exec(f"question_{i} = Question()")
        exec(f"questions.append(question_{i})")

    return questions


def print_statistics(questions):
    points = [question.points_awarded for question in questions if question.points_awarded]
    print(f"Вот и всё!\n"
          f"Отвечено {len(points)} вопроса из {len(questions)}\n"
          f"Набрано баллов: {sum(points)}")
