import razdelenie
a = razdelenie.dod()
a = razdelenie.preob(a)
b = razdelenie.dod()
b = razdelenie.preob(b)
if len(a)> len(b):
    print(1)
    quit()
elif len(a) < len(b):
    print(2)
    quit()
c = 0
while c <= len(a) - 2:
    if a[c] > b[c]:
        print(1)
        quit()
    elif a[c] < b[c]:
        print(2)
        quit()
    c += 1
if a[c] > b[c]:
    print(1)
    quit()
elif a[c] < b[c]:
    print(2)
    quit()
print(3)
