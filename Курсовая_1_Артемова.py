import random


def get_word(words):
    """
    Функция выбирает и возвращает случайное слово из передаваемого ей массива
    данных, удаляя его из списка, чтобы избежать повторов.

    Параметры:
      words (list): список со словами или выражениями для шифрования
    """
    # print(len(words))
    word = random.choice(words)
    # print(len(words))
    return word


def morse_encode(word, code):
    """
    Функция принимает слово и по буквам переводит его в символы
    в соответствии со словарём.

    Параметры:
      word (str): кодируемое слово
      code (dict): словарь символов для шифровки
    """
    translation = ""
    for letter in word:
        translation += code[letter] + " "
    return translation


def print_statistics(answers):
    """
    Функция принимает список правильных и неправильных ответов игрока
    в формате True/False, вычисляет и выводит на экран статистику.

    Параметры:
      answers (list): список со значениями True/False для вычисления статистики
      attempts (int): количество задач для дешифровки
    """
    right_answers = answers.count(True)
    wrong_answers = answers.count(False)

    print(f"\nВсего задачек: {len(answers)}\n"
          f"Отвечено верно: {right_answers}\n"
          f"Отвечено неверно: {wrong_answers}\n")


def main():
    """
    Функция предлагает сыграть, выводит зашифрованные при помощи азбуки Морзе
    слова заданное количество раз, сообщает верный ли ответ и печатает
    статистику игрока
    """
    # Словарь с азбукой Морзе
    morse_code = {
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        ".": ".-.-.-",
        ",": "--..--",
        "?": "..--..",
        "!": "-.-.--",
        "-": "-....-",
        "/": "-..-.",
        "@": ".--.-.",
        "(": "-.--.",
        ")": "-.--.-"
    }

    # Список слов для случайной выдачи и последующего шифрования
    output_words = ["people", "family", "woman", "man", "girl", "name", "head",
                    "face", "hand", "life", "hour", "week", "day", "sos", "time",
                    "world", "sun", "animal", "tree", "water", "food", "fire"]

    attempts = 5    # Количество задач для дешифровки

    answers = []    # Список для учета верных и неверных ответов

    welcome = input("Сегодня мы потренируемся расшифровывать азбуку Морзе.\n"
                    "Нажмите Enter и начнём.\n"
                    "Если не хотите играть, введите \"No\"\n").lower()
    if welcome == "no":
        print("Не хотите - как хотите :)")
        return

    for i in range(attempts):
        word = get_word(random.sample(output_words, attempts))
        # print(word)
        translation = morse_encode(word, morse_code)
        user_answer = input(
            f"\nСлово {i + 1} - \n\n{translation.strip()}\n\n").lower()
        if user_answer == word:
            print(f"\nВерно, {word.title()}!")
        else:
            print(f"\nНеверно, {word.title()}!")
        answers.append(user_answer == word)

    print_statistics(answers)


if __name__ == "__main__":
    main()
