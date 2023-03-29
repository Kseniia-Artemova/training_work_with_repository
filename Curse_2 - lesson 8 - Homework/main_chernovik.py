import os
from random import shuffle
from My_Packages.Homework_8 import utils as u

PATH_TO_FILE = os.path.join("questions.json")
questions = []
pull_questions = u.create_pull_questions(PATH_TO_FILE)
#
# print("Игра начинается!")
#
# objects = ["question_" + str(i) for i in range(1, len(pull_questions) + 1)]
# print(objects)
# print(pull_questions)
#
#
# shuffle(pull_questions)
# for object, question in zip(objects, pull_questions):
#     print(object, question)
#     create = f"{object} = u.Question()"
#     exec(create)
#     for field, value in question.items():
#         setattr(object, field, value)
#
#
# print(u.Question.__dict__)


# импортируем все нужные модули
# выводим на экран "давай играть"
# при помощи функции create_pull_questions создаём пулл вопросов
# создаем цикл задавания вопросов и приёма ответов == количеству вопросов
# в цикле:
# записываем вопрос в переменную?
# даём сам вопрос и его сложность
# просим ответ
# записываем ответ в объекты класса
# выдаём фидбэк
# выдаём количество баллов
# записываем вопрос в список questions
# после всех вопросов выводим статистику


