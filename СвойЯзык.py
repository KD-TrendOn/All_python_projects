x = 3
pop = [1, 3]
while x <= 33:
    if x % 2 == 1:
        pop.append(x ** 2)
    else:
        n = int(x / 2)
        fact = 1
        while n > 1:
            fact *= n
            n -= 1
        while True:
            if fact == 328800:
                fact /= 10
            else:
                if fact % 10 == 0:
                    fact /= 10
                else:
                    break
        pop.append(int(fact))
    x += 1
print(pop)
