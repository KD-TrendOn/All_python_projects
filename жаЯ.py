gc = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
gn = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
def ceasar(stroke, sdvig):
    stroke = stroke.lower()
    ban = ''
    for i in stroke:
        if not i in gc:
            ban += i
        else:
            ban += str(gc[(gc.index(i) + sdvig) % 33])
    print(ban)
ceasar('', -1)