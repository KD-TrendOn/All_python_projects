import math
import turtle


def prov(x):
    while True:
        try:
            c = float(input(x))
        except ValueError:
            print('Ошибка ввода')
        else:
            if c <= 0:
                print('Ошибка ввода')
            else:
                return c


def prov2(a):
    while True:
        try:
            g = float(input(a))
        except ValueError:
            print('Ошибка ввода')
        else:
            if g <= 0:
                print('Ошибка ввода')
            else:
                return a


a = input("введите 1, если вы знаете два катета, 2- если гипотенузу и катет.")
if a == '1':
    k1 = prov("Введите первый катет")
    k2 = prov("Введите второй катет")
    g = math.sqrt(k1**2 + k2**2)
    gs = str(g)
    gl = gs[len(gs) - 1]
    gpl = gs[len(gs) - 2]
    if gpl + gl == ".0":
        g = int(g)
    print("Ваша гипотенуза равна " + str(g))
elif a == "2":
    k1 = prov2("Введите известный катет")
    g = prov2("Введите гипотенузу")
    k2 = math.sqrt(g**2 - k1**2)
    k2s = str(k2)
    k2sl = k2s[len(k2s) - 1]
    k2spl = k2s[len(k2s) - 2]
    if k2spl + k2sl == ".0":
        k2 = int(k2)
    print("Второй катет равен " + str(k2))
else:
    print("Пожалуйста, введите 1 или 2")
