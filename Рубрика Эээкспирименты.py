gig = int(input("Min"))
gug = int(input("Max"))
gog = input("Type")
pop = []
x = 0
y = ""
while x != gig:
    pop.append(gog)
    x += 1
while x != gug + 1:
    y = ""
    for n in pop:
        y += n
    pop.append(gog)
    print(y)
    x += 1
while x != gig:
    y -= gog
    x -= 1
    print(y)