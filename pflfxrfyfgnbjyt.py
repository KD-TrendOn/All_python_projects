n = int(input())
a = 1
c = int(input())
d = int(input())
l = ''
while a <= n - c:
    a += c
    l += "a"
while a != n:
    if a < n - c + 1:
        a += c
        l += "a"
    else:
        a -= d
        l += "b"
print(l)


