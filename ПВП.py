a = int(input())
pop = []
i = 2
while i < a + 1:
    if a % i == 0:
        pop.append(i)
        a /= i
    else:
        i += 1
print(pop)
for x in pop:
    api = pop.count(x)
    if api >= 2:
        pop.remove(pop[pop.index(x)])
print(pop)