import random
import time
from tkinter import *


def shifu(x):
    we = str(format(x, 'b'))
    st = []
    for poop in we:
        st.append(poop)
    n = 0
    for i in st:
        if n % 2:
            if int(st[n]):
                st[n] = 0
            else:
                st[n] = 1
        n += 1
    we = ''
    for i in st:
        we += str(i)
    lol = 0
    ui = 0
    for i in we[::-1]:
        ui += (2 ** lol) * int(i)
        lol += 1
    return ui


vhod = False
sos = []


def confirmate_first_fazus():
    global stroka
    global sos
    global vhod
    login = logid.get()
    password = logpass.get()
    si = 0
    try:
        password = int(password)
    except ValueError:
        si = 1
    if ' ' in login or si:
        hidentxt.configure(text='*Неверно введены данные, попробуйте еще раз.')
        return
    ror = open(r'C:\Users\user\Desktop\joker.txt', 'r')
    sos = []
    for x in ror:
        sos.append(x.replace('\n', ""))
    ror.close()
    for x in sos:
        if login in str(x):
            dod = int(x.find(login) + len(login))
            did = int(x.rfind(' '))
            abc = int(x[dod:did])
            if shifu(abc) != int(password):
                hidentxt.configure(text='*Неверно введены данные, попробуйте еще раз.')
                return
            else:
                vhod = True
                gotofaza = True
                dengi = x[did + 1:]
                print(dengi)
    if not gotofaza:
        stroka = f'{login} {shifu(password)} 5000'
        dengi = 5000
        gotofaza = True
    window.destroy()


window = Tk()
window.title("Вход и регистрация")
window.geometry('720x400')
instr = Label(window, text='''Приветствуем вас в нашей игре Черный Джонс!
Введите Имя и Пароль для входа
Если вы хотите зарегистрироваться, введите новое Имя и Пароль.''', font=('Arial Bold', 17))
instr.grid(column=0, row=0)
logid = Entry(window, width=20, font=('Arial Bold', 17))
logid.grid(column=0, row=1)
logpass = Entry(window, width=20, font=('Arial Bold', 17))
logpass.grid(column=0, row=2)
hidentxt = Label(window, font=('Calibry', 12))
hidentxt.grid(column=0, row=3)
confbutt = Button(window, text='Подтвердить', command=confirmate_first_fazus)
confbutt.grid(column=0, row=4)
window.mainloop()
