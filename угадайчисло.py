import random

x = int(input("Сколько всего чисел будет? "))

jj = random.randint(1, x)
f = open(r"C:\Users\user\Desktop\putt.txt", "w")
f.write(str(jj) + "\n")
f.close()

pop = int(input("Введите число попыток ")) - 1

y = int(input("Введите предпологаемое число "))
sussy = 0
while sussy != 1:
    if pop == 0:
        print("Вы проиграли! (попытки закончились)")
        print(jj)
        break

    if jj != y:
        print("Неправильно, попробуйте еще раз, попыток осталось " + str(pop))
        y = int(input("Введите новое число "))
        pop -= 1
    else:
        print("Вы угадали!!!")
        break
