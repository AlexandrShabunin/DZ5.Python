import random

random_init = random.randint(1, 100)


def random_game(w, qwerty, i):
    qwerty = int(input('У Вас будет 10 попыток, чтобы угадать, что загадал компьютер, ПОЕХАЛИ - УДАЧИ!!! '))
    if qwerty == w:
        return print('YES. YOU WIN !!!  Вы угадали загаданное число {} c {} попыток'.format(qwerty, i))
    elif i == 10:
        x = input('Ваши 10 попыток кончились, попытаете удачу еще раз? y - да или  любой символ - для выхода: ')
        if x == 'y':
            rand_init = random.randint(1, 100)
            random_game(rand_init, 0, 1)
        else:
            return
    elif qwerty > w:
        print('Вы ввели БОЛЬШЕЕ число, чем загадал компьютер', '\n')
        random_game(w, qwerty, i + 1)
    elif qwerty < w:
        print('Вы ввели МЕНЬШЕЕ число, чем загадал компьютер', '\n')
        random_game(w, qwerty, i + 1)


random_game(random_init, 0, 1)
