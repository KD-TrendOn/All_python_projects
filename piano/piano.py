import os  # os.listdir()
import random  # random.choice(list)
import playsound    # only version 1.2.2
import keyboard  # for playing piano

buki = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
bukm = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
buci = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
k = [i for i in os.listdir()][:-2]
print(k)
octavi = [['A0.mp3', 'A#0.mp3', 'B0.mp3']] + \
         [[f'{o}{p}.mp3' for o in buci] for p in range(1, 8)] + [['C8.mp3']]
print(octavi)
vse = []
for spi in octavi:
    vse += [el for el in spi]
print(len(vse))
beli = [kl for kl in vse if '#' not in kl]
print(beli)
chaper = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 2, 2, 2, -2, -2, -2, 3, 3, -3, -3,
          4, -4, 5, -5, 6, -6, 7, -7]
print(len(chaper))
while True:
    try:
        for i in range(int(input('Введите длину песни в нотах '))):
            if not i:
                to = [int(round(random.triangular(0, 88, 70), 0)), 0]
                playsound.playsound(vse[to[0]])
                continue
            if bool(round(random.random(), 0)):
                if to[1]:
                    to = [vse.index(beli[to[0]]), 0]
                lol = random.choice(chaper)
                try:
                    if to[0] + lol <= -1:
                        raise IndexError
                    playsound.playsound(vse[to[0] + lol])
                except IndexError:
                    playsound.playsound(vse[to[0] - lol])
                    to[0] -= lol
                else:
                    to[0] += lol
            else:
                if not to[1]:
                    try:
                        to = [beli.index(vse[to[0]]), 1]
                    except ValueError:
                        if vse[to[0]] == 'A#0.mp3':
                            to = (0, 0)
                        else:
                            to = [ beli.index(vse[to[0]][0] + vse[to[0]][2] + '.mp3'), 1]
                lol = random.choice(chaper)
                try:
                    if to[0] + lol <= -1:
                        raise IndexError
                    playsound.playsound(beli[to[0] + lol])
                except IndexError:
                    playsound.playsound(beli[to[0] - lol])
                    to[0] -= lol
                else:
                    to[0] += lol
        raise BaseException
    except BaseException:
        if input('Ввести ещё раз? (да или нет)').lower() == 'да':
            pass
        else:
            break