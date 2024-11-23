import telebot
import os, random
from model import get_class

bot = telebot.TeleBot('7489032162:AAEy-cQzR9ZgA9w-EyKjarsBxv-iwLqf2GM')


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, """Привет! """)


@bot.message_handler(commands=['command'])
def command(message):
    fact_list = ['1', '2', '3']
    bot.send_message(message.chat.id, random.choice(fact_list))


@bot.message_handler(commands=['fact'])
def fact_command(message):
    bot.send_message(message.chat.id, "fact")


@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    if not message.photo:
        return bot.send_message(message.chat.id, "Вы забыли загрузить картинку :(")
    

    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1]


    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)

    result = get_class(model_path="keras_model.h5", labels_path="labels.txt", image_path=file_name)
    bot.send_message(message.chat.id, result)

bot.polling()
