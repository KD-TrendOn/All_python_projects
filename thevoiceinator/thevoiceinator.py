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
    charcase_ms = ['??', '??', '??']
    charcase_ts = ['??', '??']
    charcase_yc = ['??', '??', '??', '??']
    charcase_ums = ['??', '??', '??', '??', '??', '??', '??', '??', '??', '??', '??', '??', '??', '??', '??', '??']
    bu = cort[0]
    ispr = cort[1]
    aum = cort[2]
    if bu in charcase_yc:
        if ispr:
            if bu == '??':
                playsound(ye)
            elif bu == '??':
                playsound(yo)
            elif bu == '??':
                playsound(yu)
            else:
                playsound(ya)
        else:
            if bu == '??':
                playsound(e1)
            elif bu == '??':
                playsound(o1)
            elif bu == '??':
                playsound(u1)
            else:
                playsound(a1)
    elif bu in charcase_ums:
        if aum:
            if bu == '??':
                playsound(b1)
            elif bu == '??':
                playsound(v1)
            elif bu == '??':
                playsound(g1)
            elif bu == '??':
                playsound(d1)
            elif bu == '??':
                playsound(zh1)
            elif bu == '??':
                playsound(z1)
            elif bu == '??':
                playsound(k1)
            elif bu == '??':
                playsound(l1)
            elif bu == '??':
                playsound(m1)
            elif bu == '??':
                playsound(n1)
            elif bu == '??':
                playsound(p1)
            elif bu == '??':
                playsound(r1)
            elif bu == '??':
                playsound(s1)
            elif bu == '??':
                playsound(t1)
            elif bu == '??':
                playsound(f1)
            elif bu == '??':
                playsound(h1)
        else:
            if bu == '??':
                playsound(b)
            elif bu == '??':
                playsound(v)
            elif bu == '??':
                playsound(g)
            elif bu == '??':
                playsound(d)
            elif bu == '??':
                playsound(zh)
            elif bu == '??':
                playsound(z)
            elif bu == '??':
                playsound(k)
            elif bu == '??':
                playsound(l)
            elif bu == '??':
                playsound(m)
            elif bu == '??':
                playsound(n)
            elif bu == '??':
                playsound(p)
            elif bu == '??':
                playsound(r)
            elif bu == '??':
                playsound(s)
            elif bu == '??':
                playsound(t)
            elif bu == '??':
                playsound(f)
            elif bu == '??':
                playsound(h)
    elif bu in charcase_ms or charcase_ts:
        if bu == '??':
            playsound(ch1)
        elif bu == '??':
            playsound(sh1)
        elif bu == '??':
            playsound(y)
        elif bu == '??':
            playsound(sh)
        elif bu == '??':
            playsound(c)
    if bu == '??':
        playsound(a)
    elif bu == '??':
        playsound(i)
    elif bu == '??':
        playsound(o)
    elif bu == '??':
        playsound(u)
    elif bu == '??':
        playsound(yiu)
    elif bu == '??':
        playsound(e)


def voiceit(stroke):
    stroke = stroke.lower()
    charcase_pc = [' ', '??', '??', '??', '??', '??', '??', '??', '??', '??', '??', '??', '??', '??']
    charcase_mc = ['??', '??', '??', '??', '??', '??']
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