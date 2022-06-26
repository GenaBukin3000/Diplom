import telebot
from telebot import types
import time
import parser
import request
from transliterate import translit, get_available_language_codes
TOKEN = ''
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def hello(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('Начать поиск')
    markup.add(button)
    bot.send_message(message.chat.id,
                     'Привествую, для поиска запчастей нужно будет ввести название вашего города и номер искомой запчасти. '
                     'Нажмите на кнопку, чтобы начать работу', reply_markup=markup)
@bot.message_handler(content_types=['text'])
def start_searching(message):
    if message.text == 'Начать поиск' or message.text == 'Да':
        bot.send_message(message.chat.id, 'Введите название вашего города')
        bot.register_next_step_handler(message, user_location)
def user_location(message):
    global location
    location = message.text
    location = translit(location, language_code='ru', reversed=True)
    location = location.lower()
    print(location)
    bot.send_message(message.chat.id, 'Введите номер запчасти')
    bot.register_next_step_handler(message, user_partnumber)
def user_partnumber(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_yes = types.KeyboardButton('Да')
    button_No = types.KeyboardButton('Нет')
    markup.add(button_yes, button_No)
    partnumber = message.text
    print(partnumber)
    request.my_request(location, partnumber)
    bot.send_message(message.chat.id, 'Я нашел для вас лучшее предложение:')
    bot.send_message(message.chat.id, parser.drom_parser())
    bot.send_message(message.chat.id, 'Желаете продолжить поиск?', reply_markup=markup)
    bot.register_next_step_handler(message, continue_search)
def continue_search(message):
    print(message.text)
    if message.text == 'Нет':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_start= types.KeyboardButton('/start')
        markup.add(button_start)
        bot.send_message(message.chat.id, 'До свидания, для возобновления работы с ботом используйте команду /start', reply_markup=markup)
    elif message.text == 'Да':
        bot.register_next_step_handler(message, start_searching)



























#def starting_message(message):
    #if message.text == '/start' or message.text == 'Нет':
       # markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        #button = types.KeyboardButton('Начать поиск')
        #markup.add(button)
        #bot.send_message(message.chat.id,
                     #'Привествую, для поиска запчастей нужно будет ввести название вашего города и номер искомой запчасти. '
                     #'Нажмите на кнопку, чтобы начать работу', reply_markup = markup)
        #bot.register_next_step_handler(message, startsearch)
#@bot.message_handler(content_types=['text'])
#def startsearch(message):
    #print(message.text)
    #if message.text == 'Начать поиск' or message.text == 'Да':
        #bot.send_message(message.chat.id, 'Введите название вашего города')
        #bot.register_next_step_handler(message, userlocation)
#def userlocation(message):
    #bot.send_message(message.chat.id, 'Введите номер запчасти')
    #location = message.text
    #print((f'location = {location}'))
    #bot.register_next_step_handler(message, userpartnumber)
#def userpartnumber(message):
    #partnumber = message.text
    #rint(f'partnumber = {partnumber}')
    #bot.send_message(message.chat.id, 'Желаете продолжить поиск?')
    #bot.register_next_step_handler(message, startsearch)
    #markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #button_continue_search = types.KeyboardButton('Продолжить поиск')
    #button_stop_search = types.KeyboardButton('Прекратить поиск')
    #markup1.add(button_continue_search, button_stop_search)
#@bot.message_handler(content_types=['text'])
#def next(message):
    #if message.text == 'Да':
        #bot.register_next_step_handler(message, userlocation)
    #elif message.text == 'Нет':
        #bot.register_next_step_handler(message, starting_message)














#@bot.message_handler(commands=['start'])
#def starting_message(message):
    #bot.send_message(message.chat.id, 'Введите название вашего города')
    #bot.register_next_step_handler(message, userlocation)
#def userlocation(message):
    #location = message.text
    #print(f'location = {location}')
    #bot.send_message(message.chat.id, 'Введите номер запчасти')
    #bot.register_next_step_handler(message, userpartnumber)
#def userpartnumber(message):
    #partnumber = message.text
    #print(f'partnumber = {partnumber}')


bot.polling()
