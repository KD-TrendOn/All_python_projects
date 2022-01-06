x = int(input())
y = int(input())
n = int(input())
a = n//(x + y)
if not n % (x + y):
    print(2 * a)
else:
    if y < n - a < (x + y):
        print(2 * a + 2)
    else:
        print(2 * a + 1)