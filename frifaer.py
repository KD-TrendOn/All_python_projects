x = float(input("Введите сумму: "))
x1 = int(input("Введите срок в единицах времени: "))
x2 = float(input("Процент: "))
x3 = int(input("Цикл процентажа в единицах времени: "))
x4 = float(input("Сумма внесения ежецикленно (0 если отсутствует): "))
y = 0
coc = x
am = 0
while y < x1:
    print("--------------")
    zaz = coc / 100 * x2
    coc += zaz + x4
    print("+", zaz)
    print("+", x4)
    print(coc)
    y += x3
    print("Текущий срок:", y, "единиц")
    am += 1
print("--------------")
print("ИТОГ")
print("Ваша сумма выросла с", str(x), "до", str(coc), "за", x1,"единиц времени")
print("Дополнительно внесено было", am * x4)
print(int(coc) / int(x))
