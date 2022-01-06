x = 3
mega = []
cyber = []
while x != 11999:
    pop = x ** 2
    prep = pop / 2 - 0.5
    print("----------------")
    print(x)
    print(pop)
    print(prep)
    i = 2
    pip = prep
    while i < pip:
        if pip % i == 0:
            print(i)
            pip /= i
        else:
            i += 1
    print(pip)
    if x / 2 > pip:
        print("low")
        mega.append("pablo")
    else:
        print("high")
        cyber.append(len(mega))
        mega = []
    x += 2
print(cyber)