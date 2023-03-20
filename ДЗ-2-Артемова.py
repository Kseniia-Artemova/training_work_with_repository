# Создаём счетчики для баллов за ответ и количества правильных ответов
points_for_answer = 0
number_right_answers = 0

# Выводим приветственные реплики и сохраняем имя пользователя
print("Привет! Предлагаю проверить свои знания английского!")
name_student = input("Напиши, как тебя зовут.\n")
print(f"\nПривет, {name_student}, начинаем тренировку!")

# Создаем словарь с вопросами и надлежащими ответами
questions_and_answers = {"Вопрос 1: My name ___ Vova.": "is",
                         "Вопрос 2: I ___ a coder.": "am",
                         "Вопрос 3: I live ___ Moscow.": "in"}

# Создаем цикл для выдачи вопроса и сравнения ответа пользователя с правильным.
# Вопросы и правильные ответы берем из словаря.
for key, value in questions_and_answers.items():
    print("\n", key, sep="")
    answer = input("Введите ответ: ").lower()
    if answer == value:
        print("\nОтвет верный!\nВы получаете 10 баллов!")
        number_right_answers += 1
        points_for_answer += 10
    else:
        print(f"\nНеправильно.\nПравильный ответ: {value}")

# Вычисляем процент правильных ответов
percent_right_answers = round(number_right_answers / len(questions_and_answers) * 100, 1)

# Выводим итоговый результат
print(f"""\nВот и всё, {name_student }!
Вы ответили на {number_right_answers} вопросов из {len(questions_and_answers)} верно.
Вы заработали {points_for_answer} баллов.
Это {percent_right_answers} процентов.""")
