import random


def get_random_words(amount):
    """
    Функция получает столько случайных слов из файла,
    сколько требуется для работы.

    Параметры:
    amount: требуемое количество слов

    Возвращает: список случайных слов в заданном количестве
    """
    with open("words.txt", "r") as file:
        pool_words = [line.strip() for line in file]
    return random.sample(pool_words, amount)


def shuffle_letters(word):
    """
    Функция перемешивает буквы в слове.

    Параметры:
    word: слово для обработки

    Возвращает: слово с переставленными в случайном порядке буквами
    """
    new_word = list(word)
    random.shuffle(new_word)
    return "".join(new_word)


def record_result(name, points):
    """
    Функция записывает результаты в файл

    Параметры:
    name: имя игрока
    points: количество набранных очков
    """
    with open("history.txt", "a", encoding="utf-8") as file:
        file.write(f"{name} {str(points)}\n")


def anagram_game():
    """
    Функция для проведения заданного числа раундов игры,
    выводит на экран анаграммы слов и сравнивает загаданное слово
    с ответом игрока. При правильном ответе начисляет 10 очков.
    Записывает результат и имя игрока в файл.
    """
    ROUNDS = 5    # Количество раундов игры
    counter_points = 0

    user_name = input("Введите ваше имя:\n").title()

    game_words = get_random_words(ROUNDS)

    for word in game_words:
        print(f"\nУгадайте слово: {shuffle_letters(word)}")
        # в помощь, потом удалить
        print(word)
        user_answer = input().lower()
        if user_answer == word:
            print("\nВерно! Вы получаете 10 очков.")
            counter_points += 10
        else:
            print(f"\nНеверно! Верный ответ – {word}.")

    print(f"\n{user_name}, вы заработали {counter_points} очков!\n")
    record_result(user_name, counter_points)


def print_statistics():
    """
    Функция выводит на экран статистику прошлых игр:
    - количество игр
    - наилучший результат
    """
    with open("history.txt", "r", encoding="utf-8") as file:
        points = [int(line.strip().split()[1]) for line in file]

    games = len(points)
    max_points = max(points)

    print(f"Всего игр сыграно: {games}\n"
          f"Максимальный рекорд: {max_points}")


def main():
    anagram_game()
    print_statistics()


if __name__ == "__main__":
    main()





