import json

def load_students(path):
    """
    Загружает список студентов из файла
    :param path: путь к файлу
    :return: словарь с данными студентов
    """
    with open(path, "r") as json_file:
        return json.load(json_file)


def load_professions(path):
    """
    Загружает список профессий из файла
    :param path: путь к файлу
    :return: словарь с профессиональными требованиями
    """
    with open(path, "r") as json_file:
        return json.load(json_file)


def get_student_by_pk(pk, work_list):
    """
    Получает словарь с данными студента по его pk
    :param pk: номер студента
    :param work_list: список со студентами их данными
    :return: словарь с данными конкретного студента или False
    """
    for person in work_list:
        if person['pk'] == pk:
            return person
    return False


def get_profession_by_title(title, work_list):
    """
    Получает словарь с инфо о профессии по названию
    :param title: название профессии
    :param work_list: список с профессиями
    :return: словарь навыков для профессии title или False
    """
    for profession in work_list:
        if profession['title'] == title:
            return profession
    return False


def check_fitness(student, profession):
    """
    Выводит инфо о соответствии студента указанной специальности
    :param student: имя студента
    :param profession: специальность на которую претендует студент
    :return: словарь с оценкой пригодности студента
    """
    student_skills = set(student['skills'])
    profession_skills = set(profession['skills'])
    student_knowledge = profession_skills.intersection(student_skills)
    student_ignorance = profession_skills - student_skills
    percent = round(len(student_knowledge) / len(profession_skills) * 100)
    fitness = {
        'percent': percent,
        'knowledge': student_knowledge,
        'ignorance': student_ignorance
    }
    return fitness

