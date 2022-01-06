import time
def factyeah(n):
    m = 1
    for i in range(1, n + 1):
        m *= i
    return m

tool = True
while tool:
    c = input('Введите число без одинаковых цифр: ')
    try:
        bobo = int(c)
    except ValueError:
        print('Ошибка, неверный формат.', end='')
        time.sleep(.5)
        print('\r', end='')
    else:
        p = []
        for i in c:
            p += [c.count(i)]
        if not sum(p) - len(p):
            tool = False
        else:
            print("Ошибка, есть одинаковые цифры.", end='')
            time.sleep(.5)
            print('\r', end='')
# noinspection PyUnboundLocalVariable
o = 0
d = [int(x) for x in c]
while len(d) - o > 0:
    b = 0
    while len(d) - b - o - 1 > 0:
        if d[b] > d[b + 1]:
            d[b], d[b + 1] = d[b + 1], d[b]
        b += 1
    o += 1
e = []
kok = 0
for i in d:
    e += [(kok, i)]
    kok += 1
d = []
for i in c:
    for boob in e:
        if int(i) == boob[1]:
            d += [boob[0]]
a = 0
g = 0
j = len(d)
while True:
    b = d[0]
    g += b * factyeah(len(d) - 1)
    d = d[1:]
    bob = 0
    for i in d:
        if i > b:
            d[bob] -= 1
        bob += 1
    a += 1
    if j < a + 1:
        break
g += 1
krok = []
a = 0
