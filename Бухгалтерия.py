zoz = 0
zaz = 0
ziz = 0
zqz = 0
while True:
    x = input("Номер участка: ")
    if x == "stop":
         break
    y = float(input("Сколько кВатт потрачено жителем: "))
    z = float(input("Сколько он заплатил: "))
    # proverka = input("Введите (ключ) чтобы удалить данные записи сверху")
    # if proverka == "ключ":
    #    continue
    print('---------------------------------------------')
    cokk = 2.49
    mystery = y * cokk
    hand = z - mystery
    magic = hand / cokk
    a = x, '| ', round(y, 2) , 'кВатт   =>' , round(y,2) , 'кВатт *' ,  cokk,2 , '=' ,   round(mystery,2) , 'руб => ' ,  round(z,2) , 'руб -' ,  round(mystery,2) , 'руб = ' ,  round(hand,2) , 'руб (' ,  round(magic,2) , 'кВатт)'
    new = open(r"C:\Users\user\Desktop\доки с рба\pychair.txt", "a")
    new.write(str(a) + "\n")

    new.close()
    zoz += round(mystery,2)
    zaz += round(z,2)
    ziz += round(hand,2)
    zqz += round(y,2)
    print(a)
    print('---------------------------------------------')
print(zoz, ",", zaz, ",", ziz, ",", zqz)