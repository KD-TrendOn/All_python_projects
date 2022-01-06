def is_prime(a):
    if a < 2:
        print('некорректно')
        return
    if a == 2:
        print('prime')
    else:
        b = 2
        while b <= a ** 0.5 + 1:
            if not a % b:
                print('составное число')
                return
            b += 1
        print('простое число')
is_prime(68)
