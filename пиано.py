a = [i for i in range(20)] + [i for i in range(30)]
b = int(input())
d = 0
for i in a:
    if b == i:
        c = d
        break
    d += 1
a = a[:c] + a[c + 1:]
print(a)
if b != i: