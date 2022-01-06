from playsound import *
import time


def opzvbu(cort):
    a = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\a.wav'
    b = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\b.wav'
    v = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\v.wav'
    g = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\g.wav'
    d = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\d.wav'
    ye = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\ye.wav'
    yo = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\yo.wav'
    zh = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\zh.wav'
    z = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\z.wav'
    i = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\i.wav'
    y = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\y.wav'
    k = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\k.wav'
    l = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\l.wav'
    m = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\m.wav'
    n = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\n.wav'
    o = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\o.wav'
    p = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\p.wav'
    r = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\r.wav'
    s = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\s.wav'
    t = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\t.wav'
    u = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\u.wav'
    f = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\f.wav'
    h = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\h.wav'
    c = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\c.wav'
    ch1 = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\ch`.wav'
    sh = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\sh.wav'
    sh1 = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\sh`.wav'
    yiu = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\yiu.wav'
    e = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\e.wav'
    yu = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\yu.wav'
    ya = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\ya.wav'
    a1 = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\`a.wav'
    b1 = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\b`.wav'
    v1 = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\v`.wav'
    g1 = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\g`.wav'
    d1 = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\d`.wav'
    e1 = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\`e.wav'
    o1 = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\`o.wav'
    zh1 = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\zh`.wav'
    z1 = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\z`.wav'
    k1 = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\k`.wav'
    l1 = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\l`.wav'
    m1 = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\m`.wav'
    n1 = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\n`.wav'
    p1 = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\p`.wav'
    r1 = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\r`.wav'
    s1 = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\s`.wav'
    t1 = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\t`.wav'
    u1 = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\`u.wav'
    f1 = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\f`.wav'
    h1 = r'D:\ppqq\libnn\myprojs\thevoiceinator\wavchars\h`.wav'
    charcase_ms = ['ч', 'щ', 'й']
    charcase_ts = ['ц', 'ш']
    charcase_yc = ['е', 'ё', 'ю', 'я']
    charcase_ums = ['б', 'в', 'г', 'д', 'ж', 'з', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х']
    bu = cort[0]
    ispr = cort[1]
    aum = cort[2]
    if bu in charcase_yc:
        if ispr:
            if bu == 'е':
                playsound(ye)
            elif bu == 'ё':
                playsound(yo)
            elif bu == 'ю':
                playsound(yu)
            else:
                playsound(ya)
        else:
            if bu == 'е':
                playsound(e1)
            elif bu == 'ё':
                playsound(o1)
            elif bu == 'ю':
                playsound(u1)
            else:
                playsound(a1)
    elif bu in charcase_ums:
        if aum:
            if bu == 'б':
                playsound(b1)
            elif bu == 'в':
                playsound(v1)
            elif bu == 'г':
                playsound(g1)
            elif bu == 'д':
                playsound(d1)
            elif bu == 'ж':
                playsound(zh1)
            elif bu == 'з':
                playsound(z1)
            elif bu == 'к':
                playsound(k1)
            elif bu == 'л':
                playsound(l1)
            elif bu == 'м':
                playsound(m1)
            elif bu == 'н':
                playsound(n1)
            elif bu == 'п':
                playsound(p1)
            elif bu == 'р':
                playsound(r1)
            elif bu == 'с':
                playsound(s1)
            elif bu == 'т':
                playsound(t1)
            elif bu == 'ф':
                playsound(f1)
            elif bu == 'х':
                playsound(h1)
        else:
            if bu == 'б':
                playsound(b)
            elif bu == 'в':
                playsound(v)
            elif bu == 'г':
                playsound(g)
            elif bu == 'д':
                playsound(d)
            elif bu == 'ж':
                playsound(zh)
            elif bu == 'з':
                playsound(z)
            elif bu == 'к':
                playsound(k)
            elif bu == 'л':
                playsound(l)
            elif bu == 'м':
                playsound(m)
            elif bu == 'н':
                playsound(n)
            elif bu == 'п':
                playsound(p)
            elif bu == 'р':
                playsound(r)
            elif bu == 'с':
                playsound(s)
            elif bu == 'т':
                playsound(t)
            elif bu == 'ф':
                playsound(f)
            elif bu == 'х':
                playsound(h)
    elif bu in charcase_ms or charcase_ts:
        if bu == 'ч':
            playsound(ch1)
        elif bu == 'щ':
            playsound(sh1)
        elif bu == 'й':
            playsound(y)
        elif bu == 'ш':
            playsound(sh)
        elif bu == 'ц':
            playsound(c)
    if bu == 'а':
        playsound(a)
    elif bu == 'и':
        playsound(i)
    elif bu == 'о':
        playsound(o)
    elif bu == 'у':
        playsound(u)
    elif bu == 'ы':
        playsound(yiu)
    elif bu == 'э':
        playsound(e)


def voiceit(stroke):
    stroke = stroke.lower()
    charcase_pc = [' ', 'ь', 'ъ', 'а', 'е', 'ё', 'и', 'й', 'о', 'у', 'э', 'ю', 'я', 'ы']
    charcase_mc = ['ь', 'и', 'е', 'ё', 'ю', 'я']
    scet = 0
    for char in stroke:
        cort = [char]
        if not scet:
            cort += [True]
            if scet + 1 >= len(stroke):
                cort += [False]
            else:
                if stroke[scet + 1] in charcase_mc:
                    cort += [True]
                else:
                    cort += [False]
        else:
            if char ==' ':
                time.sleep(.5)
            if stroke[scet - 1] in charcase_pc:
                cort += [True]
            else:
                cort += [False]
            if scet + 1 >= len(stroke):
                cort += [False]
            else:
                if stroke[scet + 1] in charcase_mc:
                    cort += [True]
                else:
                    cort += [False]
        opzvbu(cort)
        scet += 1

bet = input()
while bet != '':
    voiceit(bet)
    bet = input()