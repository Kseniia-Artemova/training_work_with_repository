import os
import functions as fs


def main():
    # Константы, содержащие путь к файлам
    PATH_TO_DATA = os.path.abspath("data")
    PATH_TO_STUDENTS = os.path.join(PATH_TO_DATA, "students.json")
    PATH_TO_PROFESSION = os.path.join(PATH_TO_DATA, "professions.json")

    # Получаем списки студентов и профессий
    students = fs.load_students(PATH_TO_STUDENTS)
    professions = fs.load_professions(PATH_TO_PROFESSION)

    # Поиск информации о студенте по введенному номеру.
    # В случае ввода несуществующего номера завершаем программу.
    student_number = int(input("Введите номер студента:\n"))
    student_data = fs.get_student_by_pk(student_number, students)

    if not student_data:
        print("У нас нет такого студента")
        return

    student_name = student_data['full_name']
    student_skills = student_data['skills']
    print(f"Студент {student_name}")
    print(f"Знает {', '.join(student_skills)}\n")

    # Выводим варианты для ввода специальности,
    # получаем от пользователя специальность
    options_choise = ", ".join([i['title'] for i in professions])
    print(f"Выберите специальность для оценки студента {student_data['full_name']}.")
    profession = input(f"Возможные варианты: {options_choise}\n").title()

    # Получаем список навыков необходимых для конкретной специальности
    student_profession = fs.get_profession_by_title(profession, professions)

    if not student_profession:
        print("У нас нет такой специальности")
        return

    # Выводим данные о пригодности студента к введенной специальности:
    # каков процент совпадения навыков, что знает и чего не знает
    fitness = fs.check_fitness(student_data, student_profession)
    print(f"\nПригодность {fitness['percent']}%")
    if fitness['knowledge']:
        print(f"{student_name} знает {', '.join(fitness['knowledge'])}")
    else:
        print(f"{student_name} совсем не имеет требуемых навыков")
    if fitness['ignorance']:
        print(f"{student_name} не знает {', '.join(fitness['ignorance'])}")
    else:
        print(f"{student_name} имеет все требуемые навыки")


if __name__ == "__main__":
    main()