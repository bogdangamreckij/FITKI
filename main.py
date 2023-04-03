import telebot

from telebot import types, TeleBot

bot: TeleBot = telebot.TeleBot('6136144223:AAEVjmdG-IBYfhwzhACJx9S7YkRlqjdxGYU')


@bot.message_handler(commands=['start'])
def start(message):
    marckup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    v1 = types.InlineKeyboardButton('/send_message')
    v2 = types.InlineKeyboardButton('/start')
    marckup.add(v1, v2)
    mess = f'Вітаю {message.from_user.first_name}! \nДіма потрібно якийсь текст для привітання, пояснення або що.\n'
    bot.send_message(message.chat.id, mess, reply_markup=marckup)


@bot.message_handler(commands=['send_message'])
def send_mess(message):
    bot.send_message(message.chat.id, 'Напишіть ваше повідомлення')

    @bot.message_handler(content_types=['text'])
    def forward_message(message):
        marckup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        v1 = types.InlineKeyboardButton('/send_message')
        v2 = types.InlineKeyboardButton('/start')
        marckup.add(v1, v2)
        if message.chat.id != -1001826941425:
            bot.forward_message(chat_id=-1001826941425, from_chat_id=message.chat.id, message_id=message.message_id)
            bot.send_message(message.chat.id,
                             "Ваше повідомлення успішно відправлене, дякую.\n"
                             "Нам важлива ваша думка!")
            bot.send_message(message.chat.id, "Оберіть наступну дію", reply_markup=marckup)
        return


bot.polling(none_stop=True)
