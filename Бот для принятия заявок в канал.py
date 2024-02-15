'''
Предварительные шаги: 
— создаём бота, получаем токен у @BotFather
— создаём новую пригласительную ссылку в канал, выбираем добавление только после одобрения
— назначаем бота администратором нужного канала
— получаем chat ID и ID канала у @getmyid_bot
'''


import contextlib
import asyncio

from aiogram.types import ChatJoinRequest 
from aiogram import Bot, Dispatcher, F
import logging

TOKEN = "...токен бота от @BotFather..."
CHANNEL_ID = # ...ID канала от @getmyid_bot..., число, не текст
ADMIN_ID = # ...ID канала от @getmyid_bot..., число, не текст

async def approve_request(chat_join: ChatJoinRequest, bot: Bot): 
    msg = "Добро пожаловать!"
    await bot.send_message(chat_id=chat_join.from_user.id, text=msg)
    await chat_join.approve()


async def start():
    logging.basicConfig(level=logging.DEBUG, 
                        format="%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")

    bot: Bot = Bot(token=TOKEN)                 
    dp = Dispatcher()
    dp.chat_join_request.register(approve_request, F.chat.id==CHANNEL_ID)

    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except Exception as ex:
        logging.error(f"[Exception] - {ex}", exc_info=True)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    with contextlib.suppress(KeyboardInterrupt, SystemExit):
        asyncio.run(start())