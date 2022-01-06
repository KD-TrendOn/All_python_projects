gig = int(input("Введите первое число: "))
gug = int(input("Введите второе число: "))
greg = int(input("Сколько чисел всего? "))
pop = [gig, gug]
x = 2
y = 0
while x != greg:
    y = pop[len(pop) - 1] + pop[len(pop) - 2]
    pop.append(y)
    x += 1
print(pop)
pup = []
for n in pop:
    gnom = str(n)
    pup.append(len(gnom))
#print(pup)
prep = []
x = 0
while x != max(pup):
    mega = pup.count(x)
    prep.append(mega)
    x += 1
#print(prep)
#print('!', prep.count(5))
#print('!!', prep.count(4))

#itog = 0
#x = 0
#while x != len(pop) - 1:
#    z = pop[x + 1]
#    if x == 0:
#       y = pop[x]
#    else:
#        y = itog
#    itog = y + z
#    x += 1
#print(itog)


    #itig = 0
   # x = 0
    #      z = pup[x + 1]
    #    if x == 0:
    #       y = pup[x]
     #   else:
     #       y = itig
      #  itig = y + z
     #   x += 1
  #  print(itig)
   # toth =  itog / itig
   # print("Supra = ", toth)
ggaa = int(input("Число для проверки на нахождение в ряду фиббоначи"))
for x in pop:
    if ggaa == x:
        print("Ваше число ", pop.index(x) + 1, " - ое в ряду Фибоначчи")
        break