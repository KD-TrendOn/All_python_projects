xax = int(input("Число в десятеричной системе: "))
xox = int(input("Система исчисления: "))
xix = 1
pop = []
sus = 1
theme = 0
wiw = '`'
troubles = True
while troubles:
    if xax >= xox ** xix:
        xix += 1
    else:
        troubles = False
while xix != 0:
    theme = xax % (xox ** sus)
    theme = str(theme) + "`"
    pop.append(theme)
    xax //= (xox ** sus)
    xix -= 1
j3 = pop[::-1]
j1 = len(j3)
for x in j3:
    wiw += str(x)
print(wiw)