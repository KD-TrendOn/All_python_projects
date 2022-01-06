gig = int(input("Большее число"))
gug = int(input("Меньшее число"))
x = gig - gug
pop = [gig, gug, x]
while pop[len(pop) - 1] > 0:
    x = pop[len(pop) - 2] - pop[len(pop) - 1]
    pop.append(x)
    if x < 0:
        pop.remove(x)
        a = pop[len(pop) - 1]
        b = pop[len(pop) - 2]
        pop[len(pop) - 1] = b
        pop[len(pop) - 2] = a
print(pop)
