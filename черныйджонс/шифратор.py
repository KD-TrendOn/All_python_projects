def shifu():
    try:
        x = int(input('Enter the password: '))
    except ValueError:
        while 1:
            try:
                x = int(input('Wrong type. Write again: '))
            except ValueError:
                pass
            else:
                break
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
print(shifu())