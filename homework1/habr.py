from bs4 import BeautifulSoup
from requests import get

href = get(r'https://habr.com/ru/').text
soup = BeautifulSoup(href, 'html.parser')

news = soup.find_all('h2', class_='post_title')
result = []
for tit in news:
    title = tit.find('a').get_text()
    sur = tit.a.get('href')
    result.append({
        'title': title,
        'link': sur
    })
print(result)