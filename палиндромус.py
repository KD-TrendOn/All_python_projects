def palind(sok):
    if not len(sok) % 2:
        if sok[:int(len(sok)/2)] == sok[:int(len(sok)/2 - 1):-1]:
            print('палиндром')
        else:
            print('не палиндром')
    else:
        if sok[:int(len(sok)/2 - 0.5)] == sok[:int(len(sok)/2 - 0.5):-1]:
            print('палиндром')
        else:
            print('не палиндром')

palind('абобус')
palind('абоба')
palind('шалаш')
palind('мам')
palind('vffv')

def pal(a):
    if a == a[::-1]:
        print('палиндром')
    else:
        print('не палиндром')
