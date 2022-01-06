import math
a = input('Ввндите 1 или 2')
if a == '1':
    while True:
        g = float(input('Введите гипотенузу: '))
        k2 = float(input('Введите катет: '))
        if g > 0 and 0 < k2 < g:
            break
        print("Числа меньше нуля" if g <= 0 or k2 <= 0 else 'Катет больше гипотенузы')
     = math.sqrt(k1**2 + k2**2)
if a == '2':
    while True:
        k1 = float(input('Введите катет 1: '))
        k2 = float(input('Введите катет: '))
        if k2 > 0 and k1 > 0:
            break
        print("Числа меньше нуля" if g <= 0 or k2 <= 0 else 'Катет больше гипотенузы')
    g = math.sqrt(k1**2 + k2**2)
