import time

x = int(input("Кол-во секунд: "))
y = 0
print("Осталось")
while y <= x:
    print(x - y, "ceк    ",y,'прошло сек    ', y * 0.07, "Ватт     ",  y * 0.07 / 1000 * 3.93, "рублей" ,end=" ")
    time.sleep(1)
    print("\r", end=" ")
    y += 1