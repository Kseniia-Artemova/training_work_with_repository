# Импортируем модуль с функциями и
# модуль os для указания пути к файлу
import os
from My_Packages.Homework_8 import utils as u
from My_Packages.Homework_8.class_Question import *

PATH_TO_FILE = os.path.join("questions.json")

# Создаём пул вопросов для игры, создаём объекты класса Question
# с задаными свойствами из файла questions.json
pull_questions = u.create_pull_questions(PATH_TO_FILE)
questions = u.create_list_questions(len(pull_questions), pull_questions)

print("Игра начинается!")

# Запускаем цикл, в котором игроку задают вопросы,
# получаем и записываем ответы игрока в объекты класса Question,
# правильность ответа так же отражается на свойствах объектов
# класса Question. Выводим текст о правильности или ошибочности
# ответа
for num, question in zip(range(1, len(questions) + 1), questions):
    print()
    print(question.build_question(num))
    question.is_ask = True
    question.user_answer = input()

    if question.is_correct():
        question.points_awarded = question.get_points()

    print()
    print(question.build_feedback())

# Выводим статистику ответов игрока
u.print_statistics(questions)
