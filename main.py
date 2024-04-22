# main imports
import asyncio

from aiogram import executor
from aiogram import Bot, Dispatcher, types
from aiogram import types
from aiogram.dispatcher.filters import Text
from vars import *
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputFile
import asyncio
from aiogram.utils.markdown import link

# dotenv
from dotenv import load_dotenv
import os

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["🇺🇦Запорожье-Болгария🇧🇬",
               "🇺🇦Украина-Кишинев🇲🇩",
               "🇺🇦Одесса-Тирасполь🇲🇩",
               "🇺🇦Одесса-Пловдив🇧🇬",
               "🇺🇦Одесса-Бухарест🇷🇴",
               "✈️Аэропорт Отопени🇷🇴",
               "🇷🇴Трансферы по Румынии",
               "🇺🇦Украина-Германия🇩🇪",
               "️🇺🇦Украина-Польша🇵🇱",
               "️🇺🇦Киев-Болгария🇧🇬",
               "️📦Посылки ЕС,США,др.",
               "️🇧🇬Трансфер по Болгарии",
               "🇺🇦Одесса-Турция🇹🇷",
               "🇬🇪Украина-Грузия",
               "🇧🇬Болгария-Стамбул🇹🇷",
               "🇧🇬Бургас-София",
               "🇺🇦Одесса-Болгария🇧🇬",
               "🇪🇺Международные перевозки ЕС",
               "📑GreenCard",
               ]
    keyboard.add(*buttons)
    await message.answer(greetings, reply_markup=keyboard, parse_mode=types.ParseMode.HTML)

@dp.message_handler(Text(equals="🇺🇦Запорожье-Болгария🇧🇬"))
async def route_01(message: types.Message):
    await message.reply(zap_tr, parse_mode=types.ParseMode.HTML)

@dp.message_handler(Text(equals="🇺🇦Украина-Кишинев🇲🇩"))
async def route_02(message: types.Message):
    await message.reply(ukr_md, parse_mode=types.ParseMode.HTML)

@dp.message_handler(Text(equals="🇺🇦Одесса-Тирасполь🇲🇩"))
async def route_03(message: types.Message):
    await message.reply(odessa_pmr, parse_mode=types.ParseMode.HTML)

@dp.message_handler(Text(equals="🇺🇦Одесса-Пловдив🇧🇬"))
async def route_04(message: types.Message):
    await message.reply(odessa_pl, parse_mode=types.ParseMode.HTML)

@dp.message_handler(Text(equals="🇺🇦Одесса-Бухарест🇷🇴"))
async def route_05(message: types.Message):
    await message.reply(odessa_buh, parse_mode=types.ParseMode.HTML)

@dp.message_handler(Text(equals="✈️Аэропорт Отопени🇷🇴"))
async def route_06(message: types.Message):
    await message.reply(otopeni, parse_mode=types.ParseMode.HTML)

@dp.message_handler(Text(equals="🇷🇴Трансферы по Румынии"))
async def route_07(message: types.Message):
    await message.reply(ro_transfer, parse_mode=types.ParseMode.HTML)

@dp.message_handler(Text(equals="🇺🇦Украина-Германия🇩🇪"))
async def route_08(message: types.Message):
    await message.reply(ua_de, parse_mode=types.ParseMode.HTML)

@dp.message_handler(Text(equals="️🇺🇦Украина-Польша🇵🇱"))
async def route_09(message: types.Message):
    await message.reply(ua_pl, parse_mode=types.ParseMode.HTML)

@dp.message_handler(Text(equals="️🇺🇦Киев-Болгария🇧🇬"))
async def route_10(message: types.Message):
    await message.reply(kiev_bg, parse_mode=types.ParseMode.HTML)

@dp.message_handler(Text(equals="️📦Посылки ЕС,США,др."))
async def route_11(message: types.Message):
    kozechko = InputFile('images/kozechko.jpeg')
    await bot.send_photo(chat_id=message.chat.id, photo=kozechko)
    await message.answer(meest, parse_mode=types.ParseMode.HTML)

@dp.message_handler(Text(equals="️🇧🇬Трансфер по Болгарии"))
async def route_12(message: types.Message):
    await message.reply(bg_transfers, parse_mode=types.ParseMode.HTML)

@dp.message_handler(Text(equals="🇺🇦Одесса-Турция🇹🇷"))
async def route_13(message: types.Message):
    await message.reply(odessa_tr, parse_mode=types.ParseMode.HTML)

@dp.message_handler(Text(equals="🇬🇪Украина-Грузия"))
async def route_14(message: types.Message):
    tursel = InputFile('images/tursel.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=tursel)
    await message.answer(georgia, parse_mode=types.ParseMode.HTML)

@dp.message_handler(Text(equals="🇧🇬Болгария-Стамбул🇹🇷"))
async def route_16(message: types.Message):
    await message.reply(bg_tr, parse_mode=types.ParseMode.HTML)

@dp.message_handler(Text(equals="🇧🇬Бургас-София"))
async def route_17(message: types.Message):
    enjoytravel = InputFile('images/enjoytravel.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=enjoytravel)
    await message.answer(burgas_sofia, parse_mode=types.ParseMode.HTML)

@dp.message_handler(Text(equals="🇺🇦Одесса-Болгария🇧🇬"))
async def route_18(message: types.Message):
    await message.reply(odessa_bg, parse_mode=types.ParseMode.HTML)

@dp.message_handler(Text(equals="🇪🇺Международные перевозки ЕС"))
async def route_19(message: types.Message):
    await message.reply(internationals, parse_mode=types.ParseMode.HTML)

@dp.message_handler(Text(equals="📑GreenCard"))
async def green_card(message: types.Message):
    await message.reply(greencard, parse_mode=types.ParseMode.HTML)

@dp.message_handler(commands="help")
async def cmd_inline_url(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Связаться", url="tg://resolve?domain=sasha_adminBG")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Напишите админу с помощью кнопки ниже👇", reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
