echoes = 1
a = echoes
b = 0
while echoes < 99:
    a = echoes
    while a != 1:
        if a % 2 == 0:
            a /= 2
            b += 1
        else:
            a = 3 * a + 1
            b += 1
    print(b + 1 , " ходов при ", echoes)
    echoes += 1
    b = 0