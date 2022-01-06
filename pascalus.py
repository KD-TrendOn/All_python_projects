hm = []
for i in range(50):
    row = [1] * (i + 1)
    for j in range(i + 1):
        if j != 0 and j != i:
            if i == 0:
                row = [1]
            else:
                row[j] = hm[i - 1][j - 1] + hm[i - 1][j]
        else:
            row[j] = 1
    hm.append(row)
for r in hm:
    print(r)