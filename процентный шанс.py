import random
print("Использоваться будут только положительные числа от 1 до 100 000")
lol = 0
while lol == 0:
    gg = input("Посчитать прочент делимых чисел на: ")
    yy = input("Сколько чисел брать? ")
    x = 0
    nod = 0
    while x != int(yy):
        pop = random.randint(1, 100000)
        if pop % int(gg) == 0:
            nod += 1
        x += 1
    print("Процент делимых чисел на число", gg, "=", nod / int(yy) * 100, "%")