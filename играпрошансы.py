import random
a = int(input('Введите количество жизней игроков: '))
b = a
x = 0
while a > 0 and b > 0:
    print(f'Игрок 1: {a} . Игрок 2: {b}')
    if (x + 1) % 2:
        print('Ход игрока 1:')
        c = float(input('Введите шанс удара: '))
        if not c % 100:
            c = 100
        else:
            c %= 100
        print(f'Вы хотите нанести {round(100/c, 1)} урона')
        d = random.random() * 100
        if d > c:
            e = 0
            print('Вы промахнулись и нанесли 0 урона!')
        else:
            e = round(100/c, 1)
            print(f'Попадание! нанесено {e} урона!')
            b -= e
            b = round(b, 1)
            f = random.random() * 100
            if f < 100 - c:
                print('Игрок 1 вошел в раж, он получает доп. ход!')
                continue
    else:
        print('Ход игрока 2:')
        c = float(input('Введите шанс удара: '))
        if not c % 100:
            c = 100
        else:
            c %= 100
        print(f'Вы хотите нанести {round(100 / c, 1)} урона')
        d = random.random() * 100
        if d > c:
            e = 0
            print('Вы промахнулись и нанесли 0 урона!')
        else:
            e = round(100 / c, 1)
            print(f'Попадание! нанесено {e} урона!')
            a -= e
            a = round(a, 1)
            f = random.random() * 100
            if f < 100 - c:
                print('Игрок 2 в ярости, он получает доп. ход!')
                continue
    x += 1
if a > b:
    print(f"Выжил Игрок 1 со здоровьем {a}")
else:
    print(f'Победил Игрок 2 со здоровьем {b}')
