def dod():
    b = []
    while True:
        a = input()
        if a == "":
            break
        for i in a:
            b.append(i)
    return b


def preob(a):
    c = 0
    for i in a:
        a[c] = int(a[c])
        c += 1
    return a

