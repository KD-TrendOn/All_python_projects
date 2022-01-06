import requests
import html2text
s = requests.get('https://yandex.ru')
d = html2text.HTML2Text()
d.ignore_links = True
c = d.handle(s.text)
print(c)