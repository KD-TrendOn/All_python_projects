import requests
import re
reponse = str(requests.get('https://habr.com/ru/top/daily/').text)
reg = re.compile('{}tm-article-snippet__title-link')

