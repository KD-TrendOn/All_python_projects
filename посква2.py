def remlast(pop, a):
    pop.reverse()
    pop.remove(a)
    pop.reverse()


def vvod():
    pop = []
    c = 0
    while True:
        a = input()
        if a == '':
            break
        if c == 0:
            for i in a:
                if i == '0':
                    a = a[1:]
                    continue
                else:
                    break
            if a != '':
                for i in str(a):
                    pop.append(i)
            else:
                continue
        else:
            if a != '':
                for i in str(a):
                    pop.append(i)
            else:
                break
        c += 1
    da = pop.count('.')
    for i in range(da - 1):
        remlast(pop, ',')
    return pop


def plussmass(fop, vop):
    if '.' in fop:
        pz1 = len(fop) - fop.index('.') - 1
        dz1 = len(fop) - pz1 - 1
        fop.remove('.')
    else:
        pz1 = 0
        dz1 = len(fop)
    if '.' in vop:
        pz2 = len(vop) - vop.index('.') - 1
        dz2 = len(vop) - pz2 - 1
        vop.remove('.')
    else:
        pz2 = 0
        dz2 = len(vop)
    if pz1 >= pz2:
        vop += [0] * (pz1 - pz2)
        pz2 = pz1
    else:
        fop += [0] * (pz2 - pz1)
        pz1 = pz2
    if dz1 >= dz2:
        vop = [0] * (dz1 - dz2) + vop
        dz2 = dz1
    else:
        fop = [0] * (dz2 - dz1) + fop
        dz1 = dz2
    pop = [0] * (len(fop) + 1)
    c = 1
    while c <= len(pop):
        if c <= len(fop) and c <= len(vop):
            if int(fop[-c]) + int(vop[-c]) + pop[-c] >= 10:
                if int(fop[-c]) + int(vop[-c]) == 9:
                    pop[-c] = 0
                    pop[-c - 1] = 1
                else:
                    pop[-c] += int(str(int(fop[-c]) + int(vop[-c]) + pop[-c])[1])
                    pop[-c - 1] = 1
            else:
                pop[-c] += int(fop[-c]) + int(vop[-c])
        elif len(fop) < c <= len(vop):
            if pop[-c] + int(vop[-c]) == 10:
                pop[-c] = 0
                pop[-c - 1] = 1
            else:
                pop[-c] += int(vop[-c])
        elif len(fop) >= c > len(vop):
            if pop[-c] + int(fop[-c]) == 10:
                pop[-c] = 0
                pop[-c - 1] = 1
            else:
                pop[-c] += int(fop[-c])
        elif c > len(fop) and c > len(fop):
            break
        c += 1
    for i in pop:
        if not i:
            pop = pop[1:]
            continue
        else:
            break
    pop = pop[0:dz1] + ['.'] + pop[dz1:]
    return pop


fop = vvod()
vop = vvod()
print(plussmass(fop, vop))


def mnojobch(fop, mn):
    if mn:
        dop = fop
        while mn - 1:
            dop = plussmass(dop, fop)
            mn -= 1
    else:
        dop = [0] * len(fop)
    return dop

def mnomass(fop, vop):
    if '.' in fop:
        pz1 = len(fop) - fop.index('.') - 1
        dz1 = len(fop) - pz1 - 1
        fop.remove('.')
    else:
        pz1 = 0
        dz1 = len(fop)
    if '.' in vop:
        pz2 = len(vop) - vop.index('.') - 1
        dz2 = len(vop) - pz2 - 1
        vop.remove('.')
    else:
        pz2 = 0
        dz2 = len(vop)
    pz3 = pz1 + pz2
    c = 0

