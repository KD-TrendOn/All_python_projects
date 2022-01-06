def vvod():
    pop = []
    c = 0
    while True:
        a = input()
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
                break
        else:
            if a != '':
                for i in str(a):
                    pop.append(i)
            else:
                break
        c += 1
    return pop


def plussmass(fop, vop):
    if len(fop) >= len(vop):
        pop = [0] * (len(fop) + 1)
    else:
        pop = [0] * (len(vop) + 1)
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
    return pop
