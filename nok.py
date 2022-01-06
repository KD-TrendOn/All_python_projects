a = int(input())
c = int(input())
if c < a:
    b = a
elif c == a:
    print('НОК ваших чисел это: ' + str(a))
    quit()
else:
    b = c
while True:
    if (not b % a) and (not b % c):
        print(b)
        quit()
    b += 1