import random
from colorama import init, Fore
from colorama import Back
from colorama import Style

words = ['собака', 'дом','квартира']
spaces = []
init(autoreset=True)

def wordle():
    print('                                  Wordle by Kita v.1.0.0')
    print('''Приветствую! Эта игра вордли. Расскажу правила:
    1.Вы должны ввести слово.
    2.Сверху указано сколько там букв(в |_|  одна буква)
    3.Потом все буквы подсветятся одним из следующих цветов:
    Зелёный - буква стоит в правильном месте
    Жёлтый - буква в слове есть, но стоит не на своём месте(если букв несколько то они показывают на одну точку)
    Красный - буквы в слове нет''')
    letter = ''
    guessed_word = words[random.randint(0, len(words) - 1)]
    for i in range(len(guessed_word)):
        spaces.append('|_|')


    while True:
        print(Fore.RESET)
        letter = ''
        for k in range(len(guessed_word)):
            print(spaces[k], end='')
        while len(letter) != len(guessed_word):
            print()
            print('Введи слово.')
            print('_' * len(guessed_word))
            letter = list(input().lower())
            if len(letter) != len(guessed_word):
                print(f'Слово должно быть длиной в {len(guessed_word)} букв!')

        for g in range(len(letter)):
            if letter[g] == list(guessed_word)[g]:
                spaces[g] = Back.GREEN + f'|{letter[g]}|'


            else:
                if letter[g] in list(guessed_word):
                    spaces[g] = Back.YELLOW + f'|{letter[g]}|'

                else:
                    spaces[g] = Back.RED + f'|{letter[g]}|'
        if list(letter) == list(guessed_word):
            print('Ты угадал!')
            break






wordle()
