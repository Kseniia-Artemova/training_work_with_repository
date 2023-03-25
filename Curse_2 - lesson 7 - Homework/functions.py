import json


def load_students(path) -> list:
    """
    Загружает список студентов из файла
    :param path: путь к файлу
    :return: словарь с данными студентов
    """
    with open(path, "r", encoding="UTF-8") as json_file:
        return json.load(json_file)


def load_professions(path) -> list:
    """
    Загружает список профессий из файла
    :param path: путь к файлу
    :return: словарь с профессиональными требованиями
    """
    with open(path, "r", encoding="UTF-8") as json_file:
        return json.load(json_file)


def get_student_by_pk(pk, work_list) -> dict:
    """
    Получает словарь с данными студента по его pk
    :param pk: номер студента
    :param work_list: список со студентами их данными
    :return: словарь с данными конкретного студента или False
    """
    for person in work_list:
        if person['pk'] == pk:
            return person


def get_profession_by_title(title, work_list) -> dict:
    """
    Получает словарь с инфо о профессии по названию
    :param title: название профессии
    :param work_list: список с профессиями
    :return: словарь навыков для профессии title или False
    """
    for profession in work_list:
        if profession['title'] == title:
            return profession


def check_fitness(student, profession) -> dict:
    """
    Выводит инфо о соответствии студента указанной специальности
    :param student: имя студента
    :param profession: специальность на которую претендует студент
    :return: словарь с оценкой пригодности студента
    """
    student_skills = set(student['skills'])
    profession_skills = set(profession['skills'])
    fitness = dict()
    fitness['knowledge'] = profession_skills.intersection(student_skills)
    fitness['ignorance'] = profession_skills - student_skills
    fitness['percent'] = round(len(fitness['knowledge']) / len(profession_skills) * 100)

    return fitness
