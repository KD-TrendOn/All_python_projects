def modul(a):
    if a >= 0:
        return a
    return 0 - a


s = int(input())
e = int(input())
n = int(input())
pop = []
for m in range(n):
    pop.append(int(input()))
poop = []
for i in pop:
    poop += [i - s]
go = 0
for i in poop:
    poop[go] = modul(i)
    go += 1
go = min(poop)
tok = max(poop)
for i in pop:
    if modul(e - i) < tok:
        tok = modul(e - i)
print(go + 1 + tok)