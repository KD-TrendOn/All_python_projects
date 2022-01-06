def kok(vasxz):
    pi = 0
    if not vasxz[0]:
        pi += 1
        for ad in vasxz:
            if not ad:
                pi += 1
            else:
                f = 0
                for i in vasxz[pi:]:
                    if i - f - pi > 0:
                        return True
                    f += 1
                return False
    else:
        return True


n = int(input())
d = int(input())
pop = []
for i in range(n):
    pop.append(int(input()))
poop = []
for i in pop:
    poop.append(i // d)
go = 1
for i in poop:
    print('fgkadl')
    if kok(poop[:go:-1]):
        go += 1
    else:
        break
print(go)