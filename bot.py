# -*- coding: cp1251 -*-
import g4f
import telebot
from g4f.Provider import Yqcloud
token = "996630940:AAHv4EI0yqabujOhJE7At24ejsHTfs2i5qw"

g4f.debug.logging = True # enable logging
g4f.check_version = False
print(g4f.version)

def aiASK(question):
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}],
        provider= Yqcloud,
        stream=False,
    )
    return response
        
    
 
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот с нейросетью gpt 3.5-turbo!\nЗадавайте любые вопросы!".format(message.from_user, bot.get_me()), parse_mode='html')
    
@bot.message_handler(commands=['test'])
def test(message):
    bot.send_message(message.chat.id, "Test")
    bot.edit_message_text("Новый текст сообщения", chat_id=message.chat_id, message_id=message_id)
    
@bot.message_handler(content_types=['text'])
def ask(message):
    response = aiASK(message.text)
    for messaga in response:
        print(messaga, flush=True, end='')
        bot.send_message(message.chat.id, str(messaga))

bot.polling(none_stop=True)
