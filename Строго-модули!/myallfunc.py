def koryen(a):
    b = 1
    c = 2
    while c ** 2 <= a:
        if a % (c ** 2) == 0:
            a = a / (c ** 2)
            b *= c
        else:
            c += +1
    return [b, a]

def drobka3(a, b, c):
    pop = 2
    while pop < a ** 2 + b ** 2 + c ** 2:
        if a % pop == 0 and b % pop == 0 and c % pop == 0:
            a /= pop
            b /= pop
            c /= pop
            continue
        else:
            pop += 1
    return [a, b, c]

def drobka2(b, c):
    pop = 2
    while pop < b ** 2 + c ** 2:
        if b % pop == 0 and c % pop == 0:
            b /= pop
            c /= pop
            continue
        else:
            pop += 1
    return [b, c]

def scrscr(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return ["not", "not", "not"]
    papa = koryen(d)
    if papa[1] == 1:
        xxx = - b - papa[0]
        xxx1 = - b + papa[0]
        kaj = drobka2(xxx, 2 * a)
        kaj1 = drobka2(xxx1, 2 * a)
        dods = "x1 = ", kaj[0], '/', kaj[1]
        dods1 = "x2 = ", kaj1[0], '/', kaj1[1]
        return [d, dods, dods1]
    else:
        prep = drobka3(-b, papa[0], 2 * a)
        yyy = "x1 = ", prep[0], '+', prep[1], "* scrd(", papa[1], ') /', prep[2]
        yyy1 = "x2 = ", prep[0], '-', prep[1], "* scrd(", papa[1], ') /', prep[2]
        return [d, yyy, yyy1]

def scrscr2(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return ["not", "not", "not"]
    papa = koryen(d)
    if papa[1] == 1:
        xxx = - b - papa[0]
        xxx1 = - b + papa[0]
        kaj = drobka2(xxx, 2 * a)
        kaj1 = drobka2(xxx1, 2 * a)
        dods = kaj[0], '/', kaj[1]
        dods1 = kaj1[0], '/', kaj1[1]
        return [d, dods, dods1]
    else:
        prep = drobka3(-b, papa[0], 2 * a)
        yyy = prep[0], '+', prep[1], "* scrt(", papa[1], ') /', prep[2]
        yyy1 = prep[0], '-', prep[1], "* scrt(", papa[1], ') /', prep[2]
        return [d, yyy, yyy1]

def delch(a):
    pop = []
    x = 1
    while x <= a:
        if a % x == 0:
            pop.append(x)
        x += 1
    return(pop)

def arisr(a):
    edit = 0
    for x in a:
        edit += x
    edit /= int(len(a))

def pyfagorka(a, b, c):
    if a == 1:
        e = b ** 2 - c ** 2
    elif a == 2:
        e = c ** 2 + b ** 2
    f = koryen(e)
    return(f)

def odjj(a, b):
    x = 1
    pop = []
    while x <= a or x <= b:
        if a % x == 0 and b % x == 0:
            pop.append(x)
        x += 1
    return(pop)

def prostmn(a):
    pop = []
    x = 1
    while x <= a:
        if a % x == 0:
            pop.append(x)
            a /= x
        x += 1
    return (pop)

def allstat2(a, b):
    pop = []
    x0 = a + b
    x1 = a * b
    x2 = a - b
    x3 = b - a
    x4 = a / b
    x5 = b / a
    x6 = a ** b
    x7 = b ** a
    x8 = a % b
    x9 = b % a
    pop.append(x0)
    pop.append(x1)
    pop.append(x2)
    pop.append(x3)
    pop.append(x4)
    pop.append(x5)
    pop.append(x6)
    pop.append(x7)
    pop.append(x8)
    pop.append(x9)
    return(pop)

def vcewar(pop, lol):
    if lol == 1:
        for a in pop:
            print(str(a))
    if lol == 2:
        for a in pop:
            for b in pop:
                print(str(a) + str(b))
    if lol == 3:
        for a in pop:
            for b in pop:
                for c in pop:
                    print(str(a) + str(b) + str(c))
    if lol == 4:
        for a in pop:
            for b in pop:
                for c in pop:
                    for d in pop:
                        print(str(a) + str(b) + str(c) + str(d))
    if lol == 5:
        for a in pop:
            for b in pop:
                for c in pop:
                    for d in pop:
                        for e in pop:
                            print(str(a) + str(b) + str(c) + str(d) + str(e))