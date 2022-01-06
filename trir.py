import random
a = 0
for i in range(100000):
    b = int(round(random.triangular(0, 88, 132616), 0))
    a += b
print(a/100000)