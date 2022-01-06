from random import *


def suprachance(c):
    d = random() * 100
    if d > c:
        return False
    return True


def uberinol(f):
    if 0 in f:
        if not f[-1]:
            f = f[:len(f) - 1]
    return f


def boomer():
    while True:
        try:
            c = int(input('Игрок, для броска бумеранга введите 1, если же вы не хотите бросать, введите 0: '))
        except ValueError:
            pass
        else:
            if c == 0 or c == 1:
                break
    return c


def ourvvod():
    while True:
        try:
            c = float(input('Введите шанс удара: '))
        except ValueError:
            exec
        else:
            break
    if not c % 100:
        c = 100
    else:
        c %= 100
    return c


def sluchfraz():
    j = ["Промах!", "Упс, не попал!", "Опять промазал(", "Мазила ахаха"]
    return j[randint(0, len(j) - 1)]


class Artefacto(object):
    """ОСНОВНЫЕ МЕТОДЫ АРТЕФАКТОВ"""

    def __init__(self, nomee):
        number = int(input(f'''Набор Игрока {nomee}:
1 - Ярость битвы: После успешного удара, дает шанс получить дополнительный ход.
2 - ЯД: Каждый ход наносит сопернику небольшое кол-во урона
3 - Бумеранг: Раз в три хода, вы можете нанести урон себе и увеличенный урон сопернику:
'''))
        if number == 1:
            self.art = 1
        elif number == 2:
            self.art = 2
        elif number == 3:
            self.art = 3
        else:
            self.art = -1


class Igrok(object):
    """Сдесь будет описание класса игрок"""

    def __init__(self, life, nom):
        self.life, self.uron = life, life / 20
        self.nomer = nom
        self.obj = Artefacto(nom)
        self.result = []
        self.djeb = 1
        self.yarishave, self.yadishave, self.boomerishave = False, False, False
        if self.obj.art == 1:
            self.yarishave = True
        elif self.obj.art == 2:
            self.yadishave = True
        elif self.obj.art == 3:
            self.boomerishave = True
        self.xod = 0

    def artefacti(func):
        def wrapofy(self, lofe):
            print(f'Ходит Игрок {self.nomer}')
            self.samotik = 0
            if self.yarishave:
                self.seychac = [1]
                c = 0
                while True:
                    if not c:
                        self.seychac.clear()
                    if lofe - sum(self.seychac) > 0:
                        print(f'Жизни жертвы: {lofe - sum(self.seychac)}')
                        func(self)
                        if not self.tekudr:
                            break
                        self.result += [self.tekudr]
                        self.seychac += [self.tekudr]
                        if not suprachance(100 - self.poslsh):
                            if lofe - sum(self.seychac) <= 0:
                                break
                            break
                        print(f'Игрок {self.nomer} В ярости! он получает доп. ход!')
                        c += 1
            elif self.yadishave:
                func(self)
                self.result += [self.tekudr]
                self.result += [round(self.uron / 5 * 2.7, 1)]
            elif self.boomerishave:
                if self.xod < 2:
                    self.xod += 1
                    func(self)
                    self.result += [self.tekudr]
                else:
                    if boomer():
                        self.djeb = 2.7
                        func(self)
                        print(f'Вы получили {self.tekudr} повреждений и нанесли противнику в 2.7 раз больше урона')
                        self.result += [self.tekudr * 2.7]
                        self.samotik = self.tekudr
                        self.djeb = 2.7
                        self.xod = 0

                    else:
                        func(self)
                        self.result += [self.tekudr]
        return wrapofy


    def crut(self, c):
        return round(self.uron * 100 / c, 1)

    @artefacti
    def udar(self):
        c = ourvvod()
        self.poslsh = c
        print(f'Вы собираетесь нанести {self.crut(c)} * {self.djeb} урона!')
        if not suprachance(c):
            print(sluchfraz())
            self.tekudr = 0
        else:
            print(f"Попадание, нанесено {self.crut(c)} * {self.djeb}")
            self.tekudr = self.crut(c)

a = Igrok(100, 1)
b = Igrok(100, 2)
i = 0

while a.life > 0 and b.life > 0:
    a.life, b.life = round(a.life, 1), round(b.life, 1)
    print('------------------------------')
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
