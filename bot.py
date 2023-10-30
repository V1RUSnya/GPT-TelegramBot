# -*- coding: cp1251 -*-
import g4f
import telebot
from time import sleep
from g4f.Provider import Yqcloud
token = "996630940:AAHv4EI0yqabujOhJE7At24ejsHTfs2i5qw"

g4f.debug.logging = True # enable logging
g4f.check_version = False
print(g4f.version)

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот с нейросетью gpt 3.5-turbo!\nЗадавайте любые вопросы!".format(message.from_user, bot.get_me()), parse_mode='html')
    
    
@bot.message_handler(content_types=['text'])
def ask(message):
    try:
        print("\n\nВопрос: {0}, от пользователя {1.first_name}\n".format(message.text, message.from_user))
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message.text}],
            provider= Yqcloud,
            stream=True,
        )
        textCloud = ""
        sent_message = bot.send_message(message.chat.id, "Ответ: ") 
        for messaga in response:
            print(messaga, flush=True, end='')
            textCloud += messaga
            bot.edit_message_text(textCloud, message.chat.id, sent_message.message_id) 
    except telebot.apihelper.ApiTelegramException as e:
        print(f"Ошибка: {e}! Ожидание 5 секунд")
        sleep(5)
bot.polling(none_stop=True)
