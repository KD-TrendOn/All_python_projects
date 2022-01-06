import requests
di = r'D:\ppqq\libnn\sounds'
glava = r'https://theremin.music.uiowa.edu/sound%20files/MIS/Piano_Other/piano/Piano.ff.'
konc = r'.aiff'
nazv = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
for nu in range(9):
    for bu in nazv:
        for bi in (0, 1):
            if bi:
                kon = f'{bu}b{nu}'
                try:
                    kon2 = f'{nazv[nazv.index(bu) - 1]}#{nu}'
                except BaseException:
                    kon2 = f'{nazv[-1]}#{nu}'
            else:
                kon = f'{bu}{nu}'
                kon2 = kon
            try:
                zvuk = open(rf'{di}\{kon2}.aiff', 'wb')
                print(rf'{di}\{kon2}.aiff')
                vz = requests.get(rf'{glava}{kon}{konc}')
                zvuk.write(vz.content)
                zvuk.close()
                print(rf'{glava}{kon}{konc}')
            except BaseException:
                pass
