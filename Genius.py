gig = input()
gug = int(input())
pre = [gig[len(gig) - 1]]
print(pre)
pup = []
x = 0
while x > 0:
    x += 1
    glob = str(int(pre[0]) ** x)
    pup.append(glob[len(glob) - 1])
    for n in pup:
        garg = pup.count(n)
        if garg == 2:
            pup.remove(pup[len(pup) - 1])
            print(pup)
            break
    if garg == 2:
        break
uuu = gug % len(pup)
print("Конечное число будет заканчиваться на: ", pup[uuu])