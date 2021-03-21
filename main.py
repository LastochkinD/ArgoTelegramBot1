import telebot
import settings
import os

from classes import UserData
from data_provider import DataProvider

users_data = []


def find_user_data(user_id):
    for user in users_data:
        if user.user_id == user_id:
            return user


bot = telebot.TeleBot('1666463831:AAFLoOhsJH0JLuLbdf63NuWrfZTTNW7j_0k')
dp = DataProvider()

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Да', 'Нет')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     'Привет. Я Telegram бот Ауди Центра Самара. Для того чтобы загрузить фото и видео к заказ-наряду, необхоидмо ввести номер заказ-наряда.')
    if find_user_data(message.chat.id) is None:
        users_data.append(UserData(message.chat.id))


@bot.message_handler(content_types=['text'])
def send_text(message):
    user = find_user_data(message.chat.id)
    if len(message.text.lower()) == 7:
        bot.send_message(message.chat.id, 'Вы ввели номер заказ-наряда ' + message.text.lower())
        s = dp.get_zn_data(message.text.lower())
        print(s)
        if s != "":
            bot.send_message(message.chat.id,
                             "Это заказ-наряд на " + str(s[6]) + " " + str(s[4]) + " " + str(s[5]) + " Правильно?",
                             reply_markup=keyboard1)
            user.set_user_status(1)
        else:
            bot.send_message(message.chat.id, "Такого заказ-наряда нет. Попробуйте ещё раз.")


@bot.message_handler(content_types=['video'])
def catch_video(message):
    file_id = message.video.file_id
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    with open(settings.arch_path + file_info.file_id, 'wb') as new_file:
        new_file.write(downloaded_file)


bot.polling()
