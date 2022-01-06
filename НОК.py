gig = int(input())
gug = int(input())
c = 1
glob = []
while True:
    glob.append(gig * c)
    glob.append(gug * c)
    for n in glob:
        hihi = glob.count(n)
        if hihi == 2:
            print("НОК ваших чисел = ", n)
            break
    c += 1
    if hihi == 2:
        break
