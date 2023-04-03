from utils import load_random_word, get_ending
from Player import Player


def main():
    # Объявляем константы: путь к внешнему ресурсу с JSON-файлом
    # и слово, у которого планируем изменять окончание для вывода
    # в конце программы
    LINK_TO_WORDS = "https://api.npoint.io/fa38747fc7269e16d8be"
    MODIFIED_WORD = "слов"

    # Создаем объект класса BasicWord для игры с такими атрибутами как:
    # исходное слово и список вариантов слов, составленных из исходного
    game_word = load_random_word(LINK_TO_WORDS)

    # Выводим сообщение о начале игры, создаём объект класса Player,
    # которому присваивается введённое имя игрока
    print("Давай поиграем!\nВвведите имя игрока:")
    player = Player(input())

    # Создаём переменные для вывода сообщения о правилах игры
    name = player.user_name
    count_words = game_word.get_count_words()
    word = game_word.word.upper()
    min_letters = len(min(game_word.subwords, key=len))

    print(f"\nПривет, {name}!\n"
          f"Составьте {count_words} слов из слова \"{word}\".\n"
          f"Слова должны быть не короче {min_letters} букв.\n"
          f"Чтобы закончить игру, угадайте все слова или напишите 'stop'.\n"
          f"\nПоехали, ваше первое слово?")

    # Цикл, принимающий ответы игрока и проверяющий их на соответствие
    # требованиям игры. При вводе игроком слов 'стоп' или 'stop'
    # цикл прерывается
    while True:

        user_answer = input().lower()
        repeat = player.check_repeat(user_answer)

        if user_answer in ['стоп', 'stop']:
            break
        elif len(user_answer) < min_letters:
            print("Слишком короткое слово.\n\nЕщё попытка:")
            continue
        elif not game_word.check_word(user_answer):
            print("Неверно!\n\nЕщё попытка:")
            continue
        elif repeat:
            print("Это слово уже было.\n\nЕщё попытка:")
            continue
        else:
            player.add_word(user_answer)
            print("Верно!\n\nСледующее слово:")

        if player.get_count_words() == game_word.get_count_words:
            print("Вы отгадали все слова!")
            break

    # Вывод сообщения об отгаданных словах, окончание 'слов' изменяется
    # в зависимости от количества, для грамматически корректного вывода
    ending_word = get_ending(player.get_count_words(), MODIFIED_WORD)
    print(f"\nИгра завершена, вы угадали {player.get_count_words()} {ending_word}!")


if __name__ == "__main__":
    main()