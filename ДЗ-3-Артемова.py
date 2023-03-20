# Списки вопросов и ответов, счетчик правильных ответов
questions = ["My name ___  Vova.", "I ___ a coder.", "I live ___ Moscow."]
answers = ["is", "am", "in"]
counter_right_answers = 0         # правильные ответы
points = 0          # подсчет баллов
total = ""          # итоговая переменная для учета верного окончания слова

# Приветствие игрока, просим ввести ключевое слово для начала
print("""Привет! 
Предлагаю проверить свои знания английского! 
Наберите "ready", чтобы начать!""", end="\n\n")
start_answer = input("Готовы?\n").lower()

# Если пользователь ввел верное слово для старта, начинаем задавать
# вопросы из списка и сравнивать полученный ответ с соответствующим значением списка ответов
if start_answer != "ready":
    print("\nКажется, вы не хотите играть. Очень жаль.")
    exit()


    for number, question in enumerate(questions):
        print(f"\n{number+1}. {question}")
        counter_lives = 3  # счетчик попыток

        while counter_lives > 0:
            user_answer = input("\nПропущеное слово: ").lower()
            if user_answer == answers[number]:
                print("\nОтвет верный!")
                counter_right_answers += 1
                break
            counter_lives -= 1
            if counter_lives > 0:
                print(f"\nОсталось попыток: {counter_lives}, попробуйте еще раз!.")
        else:
            print(f"\nУвы, но нет. Верный ответ: {answers[number]}.")

        points += counter_lives

        if points > 4 or points == 0:
            total = str(points) + " баллов"
        elif points == 1:
            total = str(points) + " балл"
        else:
            total = str(points) + " балла"

    print(f"\nВот и всё! Вы ответили на {counter_right_answers} вопросов "
          f"из {len(answers)} верно, вы набрали {total}.")


