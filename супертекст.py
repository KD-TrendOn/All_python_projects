import time
io = input()
pop = []
io = io + " "
while io != "":
    jj = io.find(" ")
    prop = io[:jj + 1]
    prop = prop.replace(" ", "")
    pop.append(prop)
    io = io.replace(io[:jj + 1], "")
for x in pop:
    print(x, end=" ")
    time.sleep(0.5)
    print('\r', end=" ")