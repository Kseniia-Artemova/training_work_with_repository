import json
from random import shuffle
from My_Packages.Homework_8.class_Question import *


def create_pull_questions(path_file: str) -> list:
    """
    Функция переводит данные о вопросах из файла JSON
    в формат Python

    :param path_file: путь к файлу с вопросами

    :return: список словарей с данными о вопросах
    """
    with open(path_file, "r", encoding="utf-8") as file:
        pull_questions = json.load(file)
        shuffle(pull_questions)
    return pull_questions


def create_list_questions(length: int, data: list) -> list:
    """
    Функция создаёт список объектов класса Question и записывает
    переданные ей свойства вопросов в эти объекты

    :param length: нужное количество объектов для создания
    :param data: данные о вопросах, свойства для записи в объект

    :return: список объектов класса Question
    """
    questions = [Question() for _ in range(length)]

    for question, properties in zip(questions, data):
        for field, value in properties.items():
            setattr(question, field, value)

    return questions


def print_statistics(questions):
    """
    Функция выводит на экран статистику ответов игрока и количество
    набранных баллов на основании списка с объектами вопросов

    :param questions: список объектов класса Question с записанными результатами
    """
    points = [question.points_awarded for question in questions if question.points_awarded]
    print(f"\nВот и всё!\n"
          f"Отвечено {len(points)} вопроса из {len(questions)}\n"
          f"Набрано баллов: {sum(points)}")
