from imdb import IMDb
import telebot
import random as rd
API_KEI = '2115173979:AAGsJ592HbTNu-iy-oXrNjiu_wFRGdNL0ts'
ia = IMDb()
bot = telebot.TeleBot(API_KEI)

aboba = str(rd.randint(100000, 1000000))
print(aboba)
print(str(ia.get_movie(aboba).keys()))

def spi(d):
    r = ''
    for i in d:
        r += str(i) + ' '
    return r


def razlog(setr):
    pop = ''
    scet = 4095
    if scet > len(setr):
        pop = str(setr[:-1])
    else:
        pop = str(setr[:scet])
    return pop


def get_movie_info(id):
    movie = ia.get_movie(id)
    result = movie['title'] + ' ' + str(movie['year'])
    result += '\n' + spi(movie['genres'])
    gog = movie['plot']
    return result, gog


def get_poster(id):
    movie = ia.get_movie(id)
    return movie['full-size cover url']


@bot.message_handler(content_types=['text'])
def send_text(message):
    print(message.from_user.username, ':', message.text)
    bot.send_message(message.chat.id, get_movie_info(aboba))
    bot.send_photo(message.chat.id, get_poster(aboba))
    bot.send_message(message.chat.id, razlog(get_movie_info(aboba)[1]))
bot.polling(none_stop=True)
