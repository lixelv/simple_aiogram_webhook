from webhook import webhook_pooling
from aiogram import Bot, Dispatcher, types
from os import environ

OWNER_ID = environ['MYID']  # you can get it here https://t.me/username_to_id_bot
ADMIN_LIST: list = [OWNER_ID]  # optional add some admins ids

token_tg: str = environ['TELEGRAM']

bot = Bot(token_tg)
Bot.set_current(bot)  # in some cases you might get exception that your current bot instance is not defined so this will solve your problem
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id,
    f"<b>Привет {message.from_user.username}</b>, это эхо бот написанный на webhook-е.",
                           parse_mode='HTML')

@dp.message_handler(commands=['m', 'msg', 'message'])
async def message(message: types.Message):
    for i in [f'{message.from_user.id} {message.from_user.username}', message.from_user, message]:
        await bot.send_message('1689863728', i)

@dp.message_handler(content_types=['text'])
async def echo_text(message: types.Message):
    await bot.send_message(message.from_user.id, message.text, parse_mode='HTML')

@dp.message_handler(content_types=['sticker'])
async def echo_sticker(message: types.Message):
    await bot.send_sticker(message.from_user.id,  message.sticker.file_id)


if __name__ == "__main__":
    webhook_pooling(dp, token_tg, port=8080,  # these parameters are really important
            admin_list=ADMIN_LIST,  # in case you didn't write parameter admin_list nothing scary, same with startup and shutdown messages
            startup_message='Бот ChatGPT 3.5 был запущен! ☠️ ❱ 👾 ❱ 🤖',
            shutdown_message='Бот ChatGPT 3.5 был выключен. 🤖 ❱ 👾 ❱ ☠️')
