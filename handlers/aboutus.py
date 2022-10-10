# -*- coding: utf-8 -*-
# = = = = = = = IMPORTS = = = = = = = #
from aiogram import Dispatcher, Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import config as cfg

bot = Bot(token=cfg.token, parse_mode=cfg.parse_mode)
dp = Dispatcher(bot)

btnAboutUs = InlineKeyboardButton("Multichain Exchange ⚡", callback_data="call_aboutus", url="t.me/multichain_exchange")
mainAboutUs = InlineKeyboardMarkup(resize_keyboard=True).add(btnAboutUs)


@dp.message_handler(lambda msg: msg.text.startswith('О нас❓'))
async def val_aboutus(message: types.Message):
    await message.answer("Наш оффициальный канал 👇🏻", reply_markup=mainAboutUs)


# = = = = = = = REGISTER HANDLERS = = = = = = = #
def register_handlers_aboutus(dp: Dispatcher):
    dp.register_message_handler(val_aboutus, lambda msg: msg.text.startswith('О нас❓'))
