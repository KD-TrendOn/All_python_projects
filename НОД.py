gig = int(input('Число для проверки :'))
gug = int(input("Второе число: "))
x = 0
pop = []
while x != gig + 1:
    x += 1
    if gig % x == 0 and gug % x == 0:
            pop.append(x)
