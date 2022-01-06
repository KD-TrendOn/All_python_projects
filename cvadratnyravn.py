import myallfunc
while True:
    a = float(input("Введите коэффициент a "))
    b = float(input("Введите коэффициент b "))
    c = float(input("Введите коэффициент c "))
    dob = myallfunc.scrscr(a, b, c)
    dib = myallfunc.scrscr2(a, b, c)
    print("D = ", dob[0])
    print(dob[1])
    print(dob[2])
    print(str(a) + "x`2 +(" + str(b) + ")x + (" + str(c) + ") =  " + str(a) + "* (x - " + str(dib[1]) + ")(x - " + str(dib[2]) + ")")
