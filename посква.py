n = 0
cac = []
while n <= 100:
    c = 0
    for i in range(1, n + 1):
        c += i ** 2
    cac.append(c)
    n += 1
for i in cac:
    a = cac.index(i)
    print(str(a ** 3) + ' - ' + str(a ** 3 - i) + ' = ' + str(i))