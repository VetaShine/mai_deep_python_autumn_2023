"""Консольная игра Крестики-нолики"""
import random

size = int(input("Задайте размер поля: "))
board = [' ' for i in range(1, size * size + 1)]
game = int(input('Введите 1, если хотите начать игру. '
        + 'В противном случае введите любой символ и запустится игра компьютера с самим собой. '))

def draw(field):
    """Вывод игрового поля в консоль"""
    length = size + 1 + 3 * size
    print('-' * length)
    for i in range(size):
        for j in range(size):
            print('| ' + field[j + i * size], end = ' ')
        print('|')
        print('-' * length)

def moves(name):
    """Получение ввода с консоли хода игрока"""
    fidelity = False

    while not fidelity:
        move = input("Ход " + name + "? ")

        try:
            move = int(move)
        except ValueError:
            print("Некорректный ввод.")
            continue

        if 1 <= move <= size * size:
            if str(board[move - 1]) not in "XO":
                board[move - 1] = name
                fidelity = True
            else:
                print("Клетка занята.")
        else:
            print("Некорректный ввод. Введите число от 1 до квадрата размера поля.")

def check(field):
    """Проверка победы игрока"""
    win_combinations = []

    for i in range(size):
        win_combinations.append([field[i * size + j] for j in range(size)])
        win_combinations.append([field[j * size + i] for j in range(size)])

    win_combinations.append([field[i * (size + 1)] for i in range(size)])
    win_combinations.append([field[(i + 1) * (size - 1)] for i in range(size - 1, -1, -1)])

    for element in win_combinations:
        if all(item == element[0] and item in "XO" for item in element):
            return element[0]

    return False

def computer_game(field):
    """Автоматическая игра компьютером"""
    count, win = 0, False
    choice = list(range(1, size * size + 1))
    print(choice)

    while not win:
        draw(field)

        if count % 2 != 0:
            name = "O"
        else:
            name = "X"

        random_element = random.choice(choice)
        choice.remove(random_element)
        field[int(random_element - 1)] = name
        count += 1

        if count > size + 1:
            control = check(field)

            if control:
                print(control, "победил")
                win = True
                break
        if count == size * size:
            print("Ничья")
            break
    draw(field)

def main(field):
    """Главная функция"""
    count, win = 0, False

    while not win:
        draw(field)

        if count % 2 != 0:
            moves("O")
        else:
            moves("X")

        count += 1

        if count > size:
            control = check(field)

            if control:
                print(control, "победил")
                win = True
                break
        if count == size * size:
            print("Ничья")
            break
    draw(field)

if game == 1:
    main(board)
else:
    computer_game(board)
