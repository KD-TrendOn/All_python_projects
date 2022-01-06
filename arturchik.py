from random import randint
alfav = 'abcdefghijklmnopqrstuvwxyz '
print(len(alfav))

def koder(x, kod):
    x = str(x).lower()
    slovo = []
    for i in x:
        if i not in alfav:
            print('Ты шо дурак? Пиши на английском!!!')
            return
        else:
            a = (int(kod[0]) + int(kod[1]) + 1) * int(kod[2])
            buk = alfav.index(i) + a
            while buk >= len(alfav):
                buk -= len(alfav)
            slovo.append(alfav[buk - 1])
    for j in range(len(x)):
        for i in range(int(kod[3])):
            slovo.insert(j * 2 + 1, alfav[randint(0, len(alfav) - 1)])
    print(''.join(slovo))


koder(input(), input())
