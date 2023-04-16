from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import psycopg2
from config import  host, user, password, db_name
import db
TOKEN = 'TOKEN'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(msg: types.Message):
    await msg.reply(f'Я бот. Приятно познакомиться, {msg.from_user.first_name}')
    db.bot_id(msg.from_user.id, msg.from_user.first_name, msg.from_user.last_name)



@dp.message_handler(commands=['help'])
async def send_help(msg: types.Message):
    await msg.reply(f'Вот что я умею:')

@dp.message_handler()
async def get_text_message(msg: types.Message):
    if msg.text.lower() == 'привет':
        await msg.answer('Привет!')
    else:
        await msg.answer('Не могу понять, что нужно сделать, набери "\help" и я расскажу, что умею.')

if __name__ == '__main__':
    executor.start_polling(dp)
