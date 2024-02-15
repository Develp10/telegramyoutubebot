'''
— создаём бота и получаем токен — @BotFather 
— добавляем бота админом в нужные каналы
— получаем ID этих каналов — @getmyid_bot
'''

import telebot 
from telebot import types 

bot = telebot.TeleBot("...токен бота от @BotFather...")

def start_markup():
    markup = types.InlineKeyboardMarkup(row_width=True)
    link_keyboard1 = types.InlineKeyboardButton(text="1 канал", url="...ссылка на 1 канал...")
    link_keyboard2 = types.InlineKeyboardButton(text="2 канал", url="...ссылка на 2 канал...")
    link_keyboard3 = types.InlineKeyboardButton(text="3 канал", url="...ссылка на 3 канал...")

    check_keyboard = types.InlineKeyboardButton(text="Проверить", callback_data="check")
    markup.add(link_keyboard1, link_keyboard2, link_keyboard3, check_keyboard)

    return markup 


@bot.message_handler(commands=["start"])    
def start(message):
    chat_id = message.chat.id
    first_name = message.chat.first_name
    bot.send_message(chat_id, f"Привет {first_name}", reply_markup=start_markup())


def check(call, chat_id):
    st = bot.get_chat_member(chat_id, user_id=call.message.chat.id).status
    return st in ["creator", "administrator", "member"]


def check_channels(call): 
    if check(call, "...ID канала от @getmyid_bot...") and check(call, "...ID канала от @getmyid_bot...") and check(call, "...ID канала от @getmyid_bot..."):
        bot.send_message(call.message.chat.id, "Спасибо за подписку ✨")
    else:
        bot.send_message(call.message.chat.id, "Подпишись на каналы", reply_markup=start_markup())


@bot.callback_query_handler(func=lambda call: True)
def callback(call): 
    if call.data == "check": 
        check_channels(call)


if __name__ == "__main__": 
    bot.polling(none_stop=True)