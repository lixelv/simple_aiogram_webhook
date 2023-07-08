from webhook import webhook_pooling
from aiogram import Bot, Dispatcher, types
from envparse import env


env.read_envfile('.env')
OWNER_ID = env('MYID')  # you can get it here https://t.me/username_to_id_bot
ADMIN_LIST: list = [OWNER_ID]  # optional add some admins ids

token_tg: str = env('TELEGRAM')
link = env('LINK')
port = env('PORT')

bot = Bot(token_tg)
Bot.set_current(bot)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id,
    f"<b>Привет {message.from_user.username}</b>, это эхо бот написанный на webhook-е.",
                           parse_mode='HTML')


@dp.message_handler(content_types=['text'])
async def echo_text(message: types.Message):
    await bot.send_message(message.from_user.id, message.text, parse_mode='HTML')


@dp.message_handler(content_types=['sticker'])
async def echo_sticker(message: types.Message):
    await bot.send_sticker(message.from_user.id,  message.sticker.file_id)


if __name__ == "__main__":
    webhook_pooling(dp, port, link, ADMIN_LIST)
