import telebot

from telebot import types, TeleBot

bot: TeleBot = telebot.TeleBot('6136144223:AAEVjmdG-IBYfhwzhACJx9S7YkRlqjdxGYU')


@bot.message_handler(commands=['start'])
def start(message):
    marckup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    v2 = types.InlineKeyboardButton('/send_message')
    v1 = types.InlineKeyboardButton('/start')
    marckup.add(v1, v2)
    mess = f'Вітаю {message.from_user.first_name}! Ви звернулися до студенської ради ФІТКІ.\nОбирійть функцію.'
    bot.send_message(message.chat.id, mess, reply_markup=marckup)


@bot.message_handler(commands=['send_message'])
def send_mess(message):
    marckup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    skarga = types.InlineKeyboardButton('/skarga')
    propozytsiya = types.InlineKeyboardButton('/propozytsiya')
    marckup1.add(skarga, propozytsiya)
    bot.send_message(message.chat.id, 'Оберіть тип повідомлення.', reply_markup=marckup1)


@bot.message_handler(commands=['skarga'])
def send_mess(message):
    bot.send_message(message.chat.id, 'Опишіть вашу скаргу')
    marckup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    v2 = types.InlineKeyboardButton('/send_message')
    v1 = types.InlineKeyboardButton('/start')
    marckup.add(v1, v2)
    bot.send_message(-1001826941425, "Знову скарга...")
    
    @bot.message_handler(content_types=['text'])
    def forward_message(message):
        if message.chat.id != -1001826941425:
            bot.forward_message(chat_id=-1001826941425, from_chat_id=message.chat.id, message_id=message.message_id)
            bot.send_message(message.chat.id,
                             "Ваше повідомлення успішно відправлене, дякую.\n"
                             "Нам важлива ваша думка!")
            bot.send_message(message.chat.id, "Оберіть наступну дію", reply_markup=marckup)
        return


@bot.message_handler(commands=['propozytsiya'])
def send_mess(message):
    bot.send_message(message.chat.id, 'Опишіть вашу пропозицію')
    marckup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    v2 = types.InlineKeyboardButton('/send_message')
    v1 = types.InlineKeyboardButton('/start')
    marckup.add(v1, v2)
    bot.send_message(-1001826941425, "Ще одна пропозиція!!!")

    @bot.message_handler(content_types=['text'])
    def forward_propozytsiya(message):
        if message.chat.id != -1001826941425:
            bot.forward_message(chat_id=-1001826941425, from_chat_id=message.chat.id, message_id=message.message_id)
            bot.send_message(message.chat.id,
                             "Ваше повідомлення успішно відправлене, дякую." )
            bot.send_message(message.chat.id, "Виберіть наступну дію", reply_markup=marckup)
        return


bot.polling(none_stop=True)