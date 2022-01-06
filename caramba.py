import time
a = int(input('Введите сумму квадратов: '))
b = int(a ** 0.5) + 1
x = 1
y = 1
print(b)
time.sleep(5)
while x != b:
    while y != b:
        if x ** 2 + y ** 2 == a:
            print('x = ' + str(x) + ', y = ' + str(y))
        y += 1
    x += 1
    y = x
