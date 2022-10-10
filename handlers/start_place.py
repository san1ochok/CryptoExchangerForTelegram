# -*- coding: utf-8 -*-
# = = = = = = = IMPORTS = = = = = = = #
from aiogram import Dispatcher, Bot, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import config as cfg
from handlers import db

bot = Bot(token=cfg.token, parse_mode=cfg.parse_mode)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def val_start(message: types.Message, state: FSMContext):
    db.cursor.execute(f"SELECT name FROM users where id = {message.from_user.id}")
    if db.cursor.fetchone() is None:
        db.InsertValue(message.from_user.first_name, message.from_user.id)
    plus = 0.00
    db.UpdateValue('watt', plus, message.from_user.id)
    db.con.commit()
    await message.answer("Добро пожаловать в 'Multichain Exchange ⚡'\nИспользуйте кнопки:", reply_markup=mainMenu)
    await state.finish()


# = = = = = = = MAIN MENU : BUTTONS = = = = = = = #
btnP2P_Exchanger = KeyboardButton("P2P обменник💸")
btnCrosschain_Exchanger = KeyboardButton("Crosschain обмен💱")
btnWallet = KeyboardButton("Кошелёк👛")
btnStaking = KeyboardButton("Стейкинг🗄")
btnAboutUs = KeyboardButton("О нас❓")
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnP2P_Exchanger, btnCrosschain_Exchanger).add(btnWallet,
                                                                                                        btnStaking).add(
    btnAboutUs)

# = = = = = creator thoughts = = = = = #
@dp.message_handler(text = "@alexndrev")
async def passfromcreator(message):
    await message.answer("everything.is.easier.than.you.think")
    
# = = = = = = = REGISTER HANDLERS = = = = = = = #
def register_handlers_startplace(dp: Dispatcher):
    dp.register_message_handler(val_start, commands="start")
    dp.register_message_handler(passfromcreator, text="@alexndrev")