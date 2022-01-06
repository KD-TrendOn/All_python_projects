import math
import turtle


def prov(gbloid):
    while True:
        try:
            c = float(input(gbloid))
        except ValueError:
            print('Ошибка ввода: принимаюся только числа.')
        else:
            if c <= 0:
                print('Ошибка ввода: стороны должны быть больше нуля.')
            else:
                return c


while True:
    a = input("введите 1, если вы знаете два катета, 2- если гипотенузу и катет.")
    if a == '1':
        k1 = prov("Введите первый катет ")
        k2 = prov("Введите второй катет ")
        g = math.sqrt(k1 ** 2 + k2 ** 2)
        print("Ваша гипотенуза равна " + str(g))
        break
    elif a == "2":
        while True:
            k1 = prov("Введите известный катет ")
            g = prov("Введите гипотенузу ")
            if g > k1:
                break
            else:
                print("Гипотенуза должна быть больше катета.")
                continue
        k2 = math.sqrt(g ** 2 - k1 ** 2)
        print("Второй катет равен " + str(k2))
        break
    else:
        print("Пожалуйста, введите 1 или 2")

if k1 < k2:
    kto = 2
    if k2 > 1.8 * k1:
        koef = 1400 / k2
        k2 *= koef
        k1 *= koef
        g *= koef
    else:
        koef = 650 / k1
        k2 *= koef
        k1 *= koef
        g *= koef
elif k2 < k1:
    kto = 1
    if k1 > 1.8 * k2:
        koef = 1400 / k1
        k2 *= koef
        k1 *= koef
        g *= koef
    else:
        koef = 650 / k2
        k2 *= koef
        k1 *= koef
        g *= koef
else:
    kto = 1
    koef = 650 / k2
    k2 *= koef
    k1 *= koef
    g *= koef
tur = turtle.Turtle()
tur.speed(20)
tur.shape('turtle')
tur.penup()
tur.left(90)
tur.bk(325)
tur.left(90)
tur.fd(700)
tur.right(90)
tur.pendown()
tur.speed(1)
ug0 = 90
ug1 = math.degrees(math.acos(k1 / g))
ug2 = 90 + ug1
if kto == 1:
    ug2 = math.degrees(math.acos(k2 / g))
    ug1 = 90 + ug2
    tur.fd(k2)
    tur.right(180 - ug2)
    tur.fd(g)
    tur.right(ug1)
    tur.fd(k1)
elif kto == 2:
    ug1 = math.degrees(math.acos(k1 / g))
    ug2 = 90 + ug1
    tur.fd(k1)
    tur.right(180 - ug1)
    tur.fd(g)
    tur.right(ug2)
    tur.fd(k2)
tur.getscreen()._root.mainloop()
