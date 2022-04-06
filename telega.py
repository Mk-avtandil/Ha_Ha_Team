import requests
import json
from aiogram import Dispatcher, Bot, executor, types
from aiogram.utils.markdown import text, bold
from aiogram.types import ParseMode, ReplyKeyboardRemove, ReplyKeyboardMarkup, \
    KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


tg_bot = "5173934723:AAGg9SWw9CzKSRARzw9n1DN4gE4aCx3Be5s"

bot = Bot(token=tg_bot)
dp = Dispatcher(bot)

cnt = -1
f = open("news.json")
data = json.load(f)


myBtn = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton(text="Next", callback_data="Next")
)

def news():
    global cnt
    cnt += 1
    return str(data[cnt]['title']) + "\n" + \
        str("Фото: " + data[cnt]['photo']) + "\n" + \
        str("Cсылка: " + data[cnt]['link']) + "\n" + \
        str("Дата: " + data[cnt]['data'])


@dp.callback_query_handler(text='Next')
async def my_counter(callback: types.CallbackQuery):
    await callback.message.answer(news())

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(bold("Привет, пользователь 😎"), parse_mode=ParseMode.MARKDOWN)
    await message.answer(news(), reply_markup=myBtn)


if __name__ == '__main__':
    executor.start_polling(dp)