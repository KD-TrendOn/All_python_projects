a = float(input())
b = int(input('Сколько знаков:  '))
c = 0
d = ''
f = ''
while c <= b:
    pop = []
    if c == 1:
        d += '.'
    f = d
    for i in range(10):
        f += str(i)
        if float(f) ** 2 <= a:
            pop.append(int(f[-1]))
        f = f[0:len(f) -1]
    d += str(pop[-1])
    c += 1
    print(d)
