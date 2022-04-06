import requests
import json
from aiogram import Dispatcher, Bot, executor, types
from aiogram.utils.markdown import text, bold
from aiogram.types import ParseMode, ReplyKeyboardRemove, ReplyKeyboardMarkup, \
    KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


tg_bot = "5173934723:AAGg9SWw9CzKSRARzw9n1DN4gE4aCx3Be5s"

bot = Bot(token=tg_bot)
dp = Dispatcher(bot)

cnt = 0
f = open("news.json")
data = json.load(f)

next = KeyboardButton('Next')
prev = KeyboardButton('Previous')
markup = ReplyKeyboardMarkup(resize_keyboard=True).add(prev, next)

def my_cnt(operator):
    global cnt
    if operator == '+':
        cnt += 1
    else:
        if cnt >= 1:
            cnt -= 1
    return cnt

def news():
    return str(data[cnt]['title']) + "\n" + \
        str("Фото: " + data[cnt]['photo']) + "\n" + \
        str("Cсылка: " + data[cnt]['link']) + "\n" + \
        str("Дата: " + data[cnt]['data'])


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply(bold(
        'Добро пожаловать, пользователь \n Я Kloopnews, бот созданный группой "Ha Ha Team 😎"'),
        parse_mode=ParseMode.MARKDOWN)
    await message.answer("Напишите команду /news и кайфуйте", reply_markup=markup)


@dp.message_handler(commands=['news'])
async def my_news(message: types.Message):
    await message.answer(news(), reply=my_cnt('+'))


@dp.message_handler(text='Next')
async def btn_next(message: types.Message):
    await message.answer(news(), reply=my_cnt('+'))

@dp.message_handler(text='Previous')
async def btn_next(message: types.Message):
    await message.answer(news(), reply=my_cnt('-'))


if __name__ == '__main__':
    executor.start_polling(dp)