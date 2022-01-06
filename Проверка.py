import os
kekcik = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
lalka = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
troll = [1, 2, 3, 4, 5]
aha = input("Введите пароль: ")
for n in troll:
    if n == 1:
        for a in kekcik:
            joj = str(a)
            if str(joj) == str(aha):
                abama = joj
                break
    if n == 2:
        for a in kekcik:
            if str(joj) == str(aha):
                abama = joj
                break
            for b in kekcik:
                joj = str(a) + str(b)
                if str(joj) == str(aha):
                    abama = joj
                    break
    if n == 3:
        for a in kekcik:
            if str(joj) == str(aha):
                abama = joj
                break
            for b in kekcik:
                if str(joj) == str(aha):
                    abama = joj
                    break
                for c in kekcik:
                    joj = str(a) + str(b) + str(c)
                    if str(joj) == str(aha):
                        abama = joj
                        break
    if n == 4:
        for a in kekcik:
            if str(joj) == str(aha):
                abama = joj
                break
            for b in kekcik:
                if str(joj) == str(aha):
                    abama = joj
                    break
                for c in kekcik:
                    if str(joj) == str(aha):
                        abama = joj
                        break
                    for d in kekcik:
                        joj = str(a) + str(b) + str(c) + str(d)
                        if str(joj) == str(aha):
                            abama = joj
                            break
    if n == 5:
        for a in kekcik:
            if str(joj) == str(aha):
                abama = joj
                break
            for b in kekcik:
                if str(joj) == str(aha):
                    abama = joj
                    break
                for c in kekcik:
                    if str(joj) == str(aha):
                        abama = joj
                        break
                    for d in kekcik:
                        if str(joj) == str(aha):
                            abama = joj
                            break
                        for e in kekcik:
                            joj = str(a) + str(b) + str(c) + str(d) + str(e)
                            if str(joj) == str(aha):
                                abama = joj
                                break
print(abama)