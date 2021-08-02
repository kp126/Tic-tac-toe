from random import choice


def enter_name(player_number):
    """
    Функция для ввода имени игрока с проверкой корректности имени
    :param player_number: нужно ввести 1 или 2, т.к. максимум 2 игрока
    :return: "Номер игрока" : "Имя игрока"
    """
    while True:
        player = input(f'\nВведите имя игрока №{player_number}: ')
        while True:
            print(f'\nИгрок №{player_number}: {player}')
            answer = input('Верно?\nДа/Нет: ')
            if answer.title() == 'Да':
                player_name[f'player_{player_number}'] = player
                return
            elif answer.title() == 'Нет':
                print('Давай попробуем ещё раз!\n', '*' * 50)
                player = input(f'\nВведите имя игрока №{player_number}: ')
            else:
                print('Неизвестная команда!')


def game_board():
    """
    Функция для отображения игрового поля
    :return: Игровая доска
    """
    for i in place:
        i = ' '.join(i)
        print(i)
    return


def player_turn(xo):
    """
    Функция принимающая ход игрока и высталяющая ход игрока на поле, а также содержит в себе функцию victory_conditions
    для проверки условий победы. Если игрок побеждает функция вовращает win = 1 игра начинается сначала
    :param xo: требуется указать 'Х' или 'О' для выбора стороны
    :return: win = 1 - победа, 0 - ход другого игрока
    """
    global first
    while True:
        if win == 1 or win == 2:
            return win
        try:
            move = input(f'{first},твой ход (введи две цифры через пробел): ')
            move = move.split()
            if place[int(move[0])][int(move[1])] == '*':
                place[int(move[0])][int(move[1])] = xo
                game_board()
                victory_conditions(xo)
                if first == players[0]:
                    first = players[1]
                else:
                    first = players[0]
                return win
            else:
                game_board()
                print('Неверный ход! Попробуй ещё раз!')
        except (ValueError, IndexError):
            game_board()
            print('Неверный ход! Попробуй ещё раз!')


def victory_conditions(xo):
    """
    Функция проверяет стандартные условия победы игры "Крестики"
    :param xo: требуется указать 'Х' или 'О' для выбора стороны
    :return: win = 1 - победа, 0 - ход другого игрока
    """
    global win
    for w in place:
        if w.count(xo) == 3:
            print(f'У нас есть победитель! Это {first}!!!')
            win = 1
    if (place[1][1] == xo and place[2][2] == xo and place[3][3]) == xo:
        print(f'У нас есть победитель! Это {first}!!!')
        win = 1
    elif (place[1][3] == xo and place[2][2] == xo and place[3][1]) == xo:
        print(f'У нас есть победитель! Это {first}!!!')
        win = 1
    elif (place[1][1] == xo and place[2][1] == xo and place[3][1]) == xo:
        print(f'У нас есть победитель! Это {first}!!!')
        win = 1
    elif (place[1][2] == xo and place[2][2] == xo and place[3][2]) == xo:
        print(f'У нас есть победитель! Это {first}!!!')
        win = 1
    elif (place[1][3] == xo and place[2][3] == xo and place[3][3]) == xo:
        print(f'У нас есть победитель! Это {first}!!!')
        win = 1
    else:
        star_count = 0
        for w in place:
            star_count += w.count('*')
        if star_count == 0:
            win = 2
    return win


print('Крестики-нолики\n', '*' * 50)

# player_name = {'player_1': 'Коля', 'player_2': 'Лена'}
player_name = {}
while True:
    while True:
        enter_name(1)
        enter_name(2)
        print(f'\nБитва начинает! {player_name.get("player_1")} VS {player_name.get("player_2")}\n')
        players = [player_name.get('player_1'), player_name.get('player_2')]
        while True:
            print('Введи номер строки и колонки через пробел куда делаешь ход.\n'
                  'Например, 1 3 для хода третью ячейку первой строки\n')
            first = choice(players)
            print(f'Великий рандом подбрасывает монетку и первый ход делает {first}')
            win = 0
            place = [[' ', '1', '2', '3'], ['1', '*', '*', '*'], ['2', '*', '*', '*'], ['3', '*', '*', '*']]
            game_board()
            while True:
                if win == 1:
                    input('Нажми ENTER для новой игры')
                    print('*' * 50)
                    print('НОВАЯ ИГРА')
                    break
                elif win == 2:
                    print('НИЧЬЯ')
                    input('Нажми ENTER для новой игры')
                    print('*' * 50)
                    print('НОВАЯ ИГРА')
                    break
                else:
                    player_turn('Х')
                    player_turn('О')
