while True:
    a1 = input("Введите знак идентификации клиента:  ").lower()
    a2 = float(input("Последняя потраченная им сумма:  "))
    a3 = input("Введенные данные верны? Для завершения введите любое число и нажмите Enter. Если да, то просто нажмите Enter: ")
    if a3 != "":
        exit(0)
    ror = open(r"C:\Users\user\Desktop\доки с рба\bobobaba.txt", "r")
    sos = []
    sama = 0
    for x in ror:
        sos.append(x.replace('\n', ""))
    ror.close()
    for x in sos:
        if a1 in str(x):
            dod = int(x.find(a1) + len(a1))
            did = int(x.find(" %"))
            abc = x[dod:did]
            ggg = float(abc)
            if ggg + a2 >= 30000:
                a2 = a2 / 100 * 95
                ggg += a2
                troll = 5
            else:
                if ggg + a2 >= 10000:
                    a2 = a2 / 100 * 97
                    ggg += a2
                    troll = 3
                else:
                    ggg += a2
                    troll = 0
            jojo = x.replace(abc, " " + str(ggg))
            jaja = jojo.replace(jojo[jojo.find(" %") + 2:], str(troll))
            tr = sos.index(x)
            sos.pop(tr)
            sos.insert(tr, jaja)
            sama += 1
    ror = open(r"C:\Users\user\Desktop\доки с рба\bobobaba.txt", "w")
    troubles = bool(sama)
    for x in sos:
        ror.write(str(x) + "\n")
    ror.close()
    if not troubles:
        if a2 >= 30000:
            a2 = a2 / 100 * 95
            troll = 5
        else:
            if a2 >= 10000:
                a2 = a2 / 100 * 97
                troll = 3
            else:
                troll = 0
        ror = open(r"C:\Users\user\Desktop\доки с рба\bobobaba.txt", "a")
        triple = str(str(a1) + " " + str(a2) + " %" + str(troll))
        ror.write(str(triple) + "\n")
        ror.close()
    print("Текущая скидка равна - " + str(troll))
    print("Сумма покупки с учеом скидки - " + str(a2))
    if troubles:
        print("Общая сумма покупок у данного клиента - " + str(ggg))
    print("-----------------------------------------------------")
