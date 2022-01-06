from clfgame import *

# import pyautogui
a = Igrok(100, 1)
b = Igrok(100, 2)
i = 0

while a.life > 0 and b.life > 0:
    a.life, b.life = round(a.life, 1), round(b.life, 1)
    print(f'Жизни Игрока 1: {a.life}, жизни Игрока 2: {b.life}')
    if not i % 2:
        a.udar(b.life)
        b.result += [a.samotik]
        b.result = uberinol(b.result)
        a.life = a.uron * 20 - sum(b.result)
        b.life = b.uron * 20 - sum(a.result)
    else:
        b.udar(a.life)
        a.result += [b.samotik]
        a.result = uberinol(a.result)
        b.life = b.uron * 20 - sum(a.result)
        a.life = a.uron * 20 - sum(b.result)
    i += 1
if a.life > b.life:
    print(f'Победил Игрок 1 с {a.life} жизней')
    kek = '1'
else:
    print(f'Выжил Игрок 2 с {b.life} жизней')
    kek = '2'
# my_file = open(r'C:\Users\user\Desktop\putt.txt', mode='a')
# my_file.write(kek)
# my_file.close()
# pyautogui.moveTo(1100, 150)
