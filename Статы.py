gig = int(input("Введите первое число: "))
gug = int(input("Введите второе число: "))
print("Сумма ваших чисел: ", gig + gug, ";")
print("Разность ваших чисел:", gig - gug, ";", gug - gig)
print("Произведение ваших чисел: ", gig * gug)
print("Частное ваших чисел: ", gig / gug, ";", gug / gig)
print("Возможный остаток после деления: ", gig % gug, ";", gug % gig)
pop = []
x = 1
while x != gig + 1:
    if gig % x == 0:
        pop.append(x)
    x += 1
print("Все делители первого числа: ", pop)
pip = []
x = 1
while x != gug + 1:
    if gug % x == 0:
        pip.append(x)
    x += 1
print("Все делители второго числа: ", pip)
pup = []
jij = []
for n in pop:
    pup.append(n)
for n in pip:
    pup.append(n)
for n in pup:
    if pup.count(n) == 2:
        jij.append(n)
        pup.remove(n)
jij.sort()
print("Все общие делители двух чисел: ", jij)
print("НОД этих чисел: ", max(jij))
x = 1
c = 1
glob = []
while x == 1:
    glob.append(gig * c)
    glob.append(gug * c)
    for n in glob:
        hihi = glob.count(n)
        if hihi == 2:
            print("НОК ваших чисел = ", n)
            break
    c += 1
    if hihi == 2:
        break
