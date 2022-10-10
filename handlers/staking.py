# -*- coding: utf-8 -*-
# = = = = = = = IMPORTS = = = = = = = #
from aiogram import Dispatcher, Bot, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import config
from handlers import start_place as st
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from handlers import db
import asyncio
import time
import datetime

bot = Bot(token=config.token, parse_mode=config.parse_mode)
dp = Dispatcher(bot)


# = = = = = = = FSM.STATES : USDT = = = = = = = #
class FormSTUSDT(StatesGroup):
    number = State()
    comfirm = State()


# = = = = = = = FSM.STATES : TRON = = = = = = = #
class FormSTTRON(StatesGroup):
    number = State()
    comfirm = State()


# = = = = = = = FSM.STATES : SOLANA = = = = = = = #
class FormSTSOLANA(StatesGroup):
    number = State()
    comfirm = State()


# = = = = = = = FSM.STATES : POLKADOT = = = = = = = #
class FormSTPOLKADOT(StatesGroup):
    number = State()
    comfirm = State()


# = = = = = = = FSM.STATES : BNB = = = = = = = #
class FormSTBNB(StatesGroup):
    number = State()
    comfirm = State()


# = = = = = = = STAKING STABLE CALLBACK.QUERY BUTTONS = = = = = = = #
btnSTUSDT = InlineKeyboardButton("USDT", callback_data="call_stusdt")
btnSTTron = InlineKeyboardButton("Tron", callback_data="call_sttron")
btnSTSolana = InlineKeyboardButton("Solana", callback_data="call_stsolana")
btnSTPolkadot = InlineKeyboardButton("Polkadot", callback_data="call_stpolkadot")
btnSTBNB = InlineKeyboardButton("BNB", callback_data="call_stbnb")

# = = = = = = = P2P BUTTONS : COMFIRM = = = = = = = #
btnAgree = KeyboardButton("Подтверждаю")

# = = = = = = = P2P BUTTON : CANCEL = = = = = = = #
btnCancel = KeyboardButton("Отмена 🔴")

menuConfirm = ReplyKeyboardMarkup(resize_keyboard=True).add(btnAgree).add(btnCancel)
menuCancel = ReplyKeyboardMarkup(resize_keyboard=True).add(btnCancel)
mainST = InlineKeyboardMarkup(resize_keyboard=True).add(btnSTUSDT, btnSTTron, btnSTSolana).add(btnSTPolkadot, btnSTBNB)


@dp.message_handler(lambda msg: msg.text.startswith('Стейкинг🗄'))
async def val_staking(message: types.Message):
    await message.answer(
        "*Стейкинг* – cервис для инвестиций криптовалюты. Фиксированная прибыль *6%* ежемесячно прямо на ваш кошелёк\nВы *получаете доход предоставляя нам криптовалюту* в пулы ликвидности. Криптовалюта спишется с вашего баланса и доход будет поступать *ежемесячно* пока ваши средства у нас в пуле. Вывод средств откроется после *первого зачисления* средств в пул",
        reply_markup=types.ReplyKeyboardRemove())
    await message.answer("Выберите криптовалюту:", reply_markup=mainST)


@dp.message_handler(lambda msg: msg.text.startswith("Отмена 🔴"))
async def val_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


# = = = = = = = USDT = = = = = = = #
@dp.callback_query_handler(text="call_stusdt")
async def call_stusdt(call: types.CallbackQuery, state: FSMContext):
    for row in db.cursor.execute(f"SELECT * FROM users where id={call.from_user.id}"):
        timeUSDT = row[2]
        if timeUSDT == 0:
            await call.message.delete()
            await FormSTUSDT.number.set()
            await call.message.answer("Введите сумму:", reply_markup=menuCancel)
        elif timeUSDT == 1:
            await state.finish()
            await call.message.answer("Действие недоступно. Средсва уже у нас на пуле. Вы вернулись в главное меню",
                                      reply_markup=st.mainMenu)
        else:
            await state.finish()
            await call.message.answer("Действие недоступно. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormSTUSDT.number)
async def process_numberstusdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            data['number'] = message.text
            if data['number'] == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            if float(data['number']) <= row[6]:
                await FormSTUSDT.next()
                await message.answer("Подтвердите ваши действия", reply_markup=menuConfirm)
            elif float(data['number']) > row[6]:
                await state.finish()
                await message.answer("На вашем балансе в боте, недостаточно средств, для выполнения данного действия",
                                     reply_markup=st.mainMenu)


@dp.message_handler(state=FormSTUSDT.comfirm)
async def process_comfirmstusdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)

            db.cursor.execute(f"SELECT name FROM users where id = {message.from_user.id}")
            if db.cursor.fetchone() is None:
                db.InsertValue(message.from_user.first_name, message.from_user.id)
            minus = -num
            plus = num
            timevaltrue = 1
            db.UpdateValue('usdt', minus, message.from_user.id)
            db.UpdateValue('STusdt', plus, message.from_user.id)
            db.UpdateValue('timeUSDT', timevaltrue, message.from_user.id)
            db.con.commit()
            for row in db.cursor.execute(f"SELECT usdt FROM users where id={message.from_user.id}"):
                await message.reply(f"Остаток на вашем балансе: `{'{:0.4f}'.format(row[0])}`")
            await bot.send_message(config.admin_id,
                                   f"_#STAKING_\n\n📄 *Чек пользователя:*\n*Поставлено на Пул:* `{'{:0.4f}'.format(plus)}` *USDT*\n*ID пользователя:* `{message.from_user.id}`")
            await state.finish()
            await message.answer("Средства офорлены и отправлены нам на пул", reply_markup=st.mainMenu)
            while timevaltrue == 1:
                for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
                    starttime = datetime.datetime.now()
                    await asyncio.sleep(60 * 60 * 24 * 30)
                    timevaltrue = -1
                    plus = plus * 0.06
                    minus = -plus
                    db.UpdateValue('usdt', plus, message.from_user.id)
                    db.UpdateValue('STusdt', minus, message.from_user.id)
                    db.UpdateValue('timeUSDT', timevaltrue, message.from_user.id)
                    await message.answer(
                        f"*Начисления с пула:* `{'{:0.4f}'.format(row[6] - (row[6] - plus))}` *USDT*\n*Начало*: `{starttime}`\n\n_Средства автоматически были зачислены на ваш баланс_")
                    await bot.send_message(config.admin_id,
                                           f"_#STAKING_\n\n📄 *Чек пользователя:*\n\n*Автоматически было зачислено:* `{'{:0.4f}'.format(row[6] - plus)}` *USDT*\n*ID пользователя:* `{message.from_user.id}`")
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = TRON = = = = = = = #
@dp.callback_query_handler(text="call_sttron")
async def call_sttron(call: types.CallbackQuery, state: FSMContext):
    for row in db.cursor.execute(f"SELECT * FROM users where id={call.from_user.id}"):
        timeTRON = row[20]
        if timeTRON == 0:
            await call.message.delete()
            await FormSTTRON.number.set()
            await call.message.answer("Введите сумму:", reply_markup=menuCancel)
        elif timeTRON == 1:
            await state.finish()
            await call.message.answer("Действие недоступно. Средсва уже у нас на пуле. Вы вернулись в главное меню",
                                      reply_markup=st.mainMenu)
        else:
            await state.finish()
            await call.message.answer("Действие недоступно. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormSTTRON.number)
async def process_numbersttron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            data['number'] = message.text
            if data['number'] == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            if float(data['number']) <= row[10]:
                await FormSTTRON.next()
                await message.answer("Подтвердите ваши действия", reply_markup=menuConfirm)
            elif float(data['number']) > row[10]:
                await state.finish()
                await message.answer("На вашем балансе в боте, недостаточно средств, для выполнения данного действия",
                                     reply_markup=st.mainMenu)


@dp.message_handler(state=FormSTTRON.comfirm)
async def process_comfirmsttron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)

            db.cursor.execute(f"SELECT name FROM users where id = {message.from_user.id}")
            if db.cursor.fetchone() is None:
                db.InsertValue(message.from_user.first_name, message.from_user.id)
            minus = -num
            plus = num
            timevaltrue = 1
            db.UpdateValue('tron', minus, message.from_user.id)
            db.UpdateValue('STtron', plus, message.from_user.id)
            db.UpdateValue('timeTRON', timevaltrue, message.from_user.id)
            db.con.commit()
            for row in db.cursor.execute(f"SELECT tron FROM users where id={message.from_user.id}"):
                await message.reply(f"Остаток на вашем балансе: `{'{:0.4f}'.format(row[0])}`")
            await bot.send_message(config.admin_id,
                                   f"_#STAKING_\n\n📄 *Чек пользователя:*\n*Поставлено на Пул:* `{'{:0.4f}'.format(plus)}` *TRON*\n*ID пользователя:* `{message.from_user.id}`")
            await state.finish()
            await message.answer("Средства офорлены и отправлены нам на пул", reply_markup=st.mainMenu)
            while timevaltrue == 1:
                for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
                    starttime = datetime.datetime.now()
                    await asyncio.sleep(60 * 60 * 24 * 30)
                    timevaltrue = -1
                    plus = plus * 0.06
                    minus = -plus
                    db.UpdateValue('tron', plus, message.from_user.id)
                    db.UpdateValue('STtron', minus, message.from_user.id)
                    db.UpdateValue('timeTRON', timevaltrue, message.from_user.id)
                    await message.answer(
                        f"*Начисления с пула:* `{'{:0.4f}'.format(row[10] - (row[10] - plus))}` *TRON*\n*Текущий баланс:* `{'{:0.4f}'.format(row[10])}` *TRON*\n*Начало*: `{starttime}`\n\n_Средства автоматически были зачислены на ваш баланс_")
                    await bot.send_message(config.admin_id,
                                           f"_#STAKING_\n\n📄 *Чек пользователя:*\n\n*Автоматически было зачислено:* `{'{:0.4f}'.format(row[10] - plus)}` *TRON*\n*ID пользователя:* `{message.from_user.id}`")
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = SOLANA = = = = = = = #
@dp.callback_query_handler(text="call_stsolana")
async def call_stsolana(call: types.CallbackQuery, state: FSMContext):
    for row in db.cursor.execute(f"SELECT * FROM users where id={call.from_user.id}"):
        timeSOLANA = row[21]
        if timeSOLANA == 0:
            await call.message.delete()
            await FormSTSOLANA.number.set()
            await call.message.answer("Введите сумму:", reply_markup=menuCancel)
        elif timeSOLANA == 1:
            await state.finish()
            await call.message.answer("Действие недоступно. Средсва уже у нас на пуле. Вы вернулись в главное меню",
                                      reply_markup=st.mainMenu)
        else:
            await state.finish()
            await call.message.answer("Действие недоступно. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormSTSOLANA.number)
async def process_numberstsolana(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            data['number'] = message.text
            if data['number'] == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            if float(data['number']) <= row[5]:
                await FormSTSOLANA.next()
                await message.answer("Подтвердите ваши действия", reply_markup=menuConfirm)
            elif float(data['number']) > row[5]:
                await state.finish()
                await message.answer("На вашем балансе в боте, недостаточно средств, для выполнения данного действия",
                                     reply_markup=st.mainMenu)


@dp.message_handler(state=FormSTSOLANA.comfirm)
async def process_comfirmstsolana(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)

            db.cursor.execute(f"SELECT name FROM users where id = {message.from_user.id}")
            if db.cursor.fetchone() is None:
                db.InsertValue(message.from_user.first_name, message.from_user.id)
            minus = -num
            plus = num
            timevaltrue = 1
            db.UpdateValue('solana', minus, message.from_user.id)
            db.UpdateValue('STsolana', plus, message.from_user.id)
            db.UpdateValue('timeSOLANA', timevaltrue, message.from_user.id)
            db.con.commit()
            for row in db.cursor.execute(f"SELECT solana FROM users where id={message.from_user.id}"):
                await message.reply(f"Остаток на вашем балансе: `{'{:0.4f}'.format(row[0])}`")
            await bot.send_message(config.admin_id,
                                   f"_#STAKING_\n\n📄 *Чек пользователя:*\n*Поставлено на Пул:* `{'{:0.4f}'.format(plus)}` *SOLANA*\n*ID пользователя:* `{message.from_user.id}`")
            await state.finish()
            await message.answer("Средства офорлены и отправлены нам на пул", reply_markup=st.mainMenu)
            while timevaltrue == 1:
                for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
                    starttime = datetime.datetime.now()
                    await asyncio.sleep(60 * 60 * 24 * 30)
                    timevaltrue = -1
                    plus = plus * 0.06
                    minus = -plus
                    db.UpdateValue('solana', plus, message.from_user.id)
                    db.UpdateValue('STsolana', minus, message.from_user.id)
                    db.UpdateValue('timeSOLANA', timevaltrue, message.from_user.id)
                    await message.answer(
                        f"*Начисления с пула:* `{'{:0.4f}'.format(row[5] - (row[5] - plus))}` *SOLANA*\n*Текущий баланс:* `{'{:0.4f}'.format(row[5])}` *SOLANA*\n*Начало*: `{starttime}`\n\n_Средства автоматически были зачислены на ваш баланс_")
                    await bot.send_message(config.admin_id,
                                           f"_#STAKING_\n\n📄 *Чек пользователя:*\n\n*Автоматически было зачислено:* `{'{:0.4f}'.format(row[5] - plus)}` *SOLANA*\n*ID пользователя:* `{message.from_user.id}`")
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = POLKADOT = = = = = = = #
@dp.callback_query_handler(text="call_stpolkadot")
async def call_stpolkadot(call: types.CallbackQuery, state: FSMContext):
    for row in db.cursor.execute(f"SELECT * FROM users where id={call.from_user.id}"):
        timePOLKADOT = row[22]
        if timePOLKADOT == 0:
            await call.message.delete()
            await FormSTPOLKADOT.number.set()
            await call.message.answer("Введите сумму:", reply_markup=menuCancel)
        elif timePOLKADOT == 1:
            await state.finish()
            await call.message.answer("Действие недоступно. Средсва уже у нас на пуле. Вы вернулись в главное меню",
                                      reply_markup=st.mainMenu)
        else:
            await state.finish()
            await call.message.answer("Действие недоступно. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormSTPOLKADOT.number)
async def process_numberstpolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            data['number'] = message.text
            if data['number'] == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            if float(data['number']) <= row[11]:
                await FormSTPOLKADOT.next()
                await message.answer("Подтвердите ваши действия", reply_markup=menuConfirm)
            elif float(data['number']) > row[11]:
                await state.finish()
                await message.answer("На вашем балансе в боте, недостаточно средств, для выполнения данного действия",
                                     reply_markup=st.mainMenu)


@dp.message_handler(state=FormSTPOLKADOT.comfirm)
async def process_comfirmstpolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)

            db.cursor.execute(f"SELECT name FROM users where id = {message.from_user.id}")
            if db.cursor.fetchone() is None:
                db.InsertValue(message.from_user.first_name, message.from_user.id)
            minus = -num
            plus = num
            timevaltrue = 1
            db.UpdateValue('polkadot', minus, message.from_user.id)
            db.UpdateValue('STpolkadot', plus, message.from_user.id)
            db.UpdateValue('timePOLKADOT', timevaltrue, message.from_user.id)
            db.con.commit()
            for row in db.cursor.execute(f"SELECT polkadot FROM users where id={message.from_user.id}"):
                await message.reply(f"Остаток на вашем балансе: `{'{:0.4f}'.format(row[0])}`")
            await bot.send_message(config.admin_id,
                                   f"_#STAKING_\n\n📄 *Чек пользователя:*\n*Поставлено на Пул:* `{'{:0.4f}'.format(plus)}` *POLKADOT*\n*ID пользователя:* `{message.from_user.id}`")
            await state.finish()
            await message.answer("Средства офорлены и отправлены нам на пул", reply_markup=st.mainMenu)
            while timevaltrue == 1:
                for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
                    starttime = datetime.datetime.now()
                    await asyncio.sleep(60 * 60 * 24 * 30)
                    timevaltrue = -1
                    plus = plus * 0.06
                    minus = -plus
                    db.UpdateValue('polkadot', plus, message.from_user.id)
                    db.UpdateValue('STpolkadot', minus, message.from_user.id)
                    db.UpdateValue('timePOLKADOT', timevaltrue, message.from_user.id)
                    await message.answer(
                        f"*Начисления с пула:* `{'{:0.4f}'.format(row[11] - (row[11] - plus))}` *POLKADOT*\n*Текущий баланс:* `{'{:0.4f}'.format(row[11])}` *POLKADOT*\n*Начало*: `{starttime}`\n\n_Средства автоматически были зачислены на ваш баланс_")
                    await bot.send_message(config.admin_id,
                                           f"_#STAKING_\n\n📄 *Чек пользователя:*\n\n*Автоматически было зачислено:* `{'{:0.4f}'.format(row[11] - plus)}` *POLKADOT*\n*ID пользователя:* `{message.from_user.id}`")
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = BNB = = = = = = = #
@dp.callback_query_handler(text="call_stbnb")
async def call_stbnb(call: types.CallbackQuery, state: FSMContext):
    for row in db.cursor.execute(f"SELECT * FROM users where id={call.from_user.id}"):
        timeBNB = row[23]
        if timeBNB == 0:
            await call.message.delete()
            await FormSTBNB.number.set()
            await call.message.answer("Введите сумму:", reply_markup=menuCancel)
        elif timeBNB == 1:
            await state.finish()
            await call.message.answer("Действие недоступно. Средсва уже у нас на пуле. Вы вернулись в главное меню",
                                      reply_markup=st.mainMenu)
        else:
            await state.finish()
            await call.message.answer("Действие недоступно. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormSTBNB.number)
async def process_numberstbnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            data['number'] = message.text
            if data['number'] == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            if float(data['number']) <= row[7]:
                await FormSTBNB.next()
                await message.answer("Подтвердите ваши действия", reply_markup=menuConfirm)
            elif float(data['number']) > row[7]:
                await state.finish()
                await message.answer("На вашем балансе в боте, недостаточно средств, для выполнения данного действия",
                                     reply_markup=st.mainMenu)


@dp.message_handler(state=FormSTBNB.comfirm)
async def process_comfirmstbnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)

            db.cursor.execute(f"SELECT name FROM users where id = {message.from_user.id}")
            if db.cursor.fetchone() is None:
                db.InsertValue(message.from_user.first_name, message.from_user.id)
            minus = -num
            plus = num
            timevaltrue = 1
            db.UpdateValue('bnb', minus, message.from_user.id)
            db.UpdateValue('STbnb', plus, message.from_user.id)
            db.UpdateValue('timeBNB', timevaltrue, message.from_user.id)
            db.con.commit()
            for row in db.cursor.execute(f"SELECT bnb FROM users where id={message.from_user.id}"):
                await message.reply(f"Остаток на вашем балансе: `{'{:0.4f}'.format(row[0])}`")
            await bot.send_message(config.admin_id,
                                   f"_#STAKING_\n\n📄 *Чек пользователя:*\n*Поставлено на Пул:* `{'{:0.4f}'.format(plus)}` *BNB*\n*ID пользователя:* `{message.from_user.id}`")
            await state.finish()
            await message.answer("Средства офорлены и отправлены нам на пул", reply_markup=st.mainMenu)
            while timevaltrue == 1:
                for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
                    starttime = datetime.datetime.now()
                    await asyncio.sleep(60 * 60 * 24 * 30)
                    timevaltrue = -1
                    plus = plus * 0.06
                    minus = -plus
                    db.UpdateValue('bnb', plus, message.from_user.id)
                    db.UpdateValue('STbnb', minus, message.from_user.id)
                    db.UpdateValue('timeBNB', timevaltrue, message.from_user.id)
                    await message.answer(
                        f"*Начисления с пула:* `{'{:0.4f}'.format(row[7] - (row[7] - plus))}` *BNB*\n*Текущий баланс:* `{'{:0.4f}'.format(row[7])}` *BNB*\n*Начало*: `{starttime}`\n\n_Средства автоматически были зачислены на ваш баланс_")
                    await bot.send_message(config.admin_id,
                                           f"_#STAKING_\n\n📄 *Чек пользователя:*\n\n*Автоматически было зачислено:* `{'{:0.4f}'.format(row[7] - plus)}` *BNB*\n*ID пользователя:* `{message.from_user.id}`")
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = REGISTER HANDLERS = = = = = = = #
def register_handlers_staking(dp: Dispatcher):
    # = = = = = = STAKING ACTIVE  = = = = = = #
    dp.register_message_handler(val_cancel, lambda msg: msg.text.startswith("Отмена 🔴"))
    dp.register_message_handler(val_staking, lambda msg: msg.text.startswith('Стейкинг🗄'))

    # = = = = = STAKING MENU : USDT = = = = = #
    dp.register_callback_query_handler(call_stusdt, text="call_stusdt")
    dp.register_callback_query_handler(process_numberstusdt, state=FormSTUSDT.number)
    dp.register_message_handler(process_numberstusdt, state=FormSTUSDT.number)
    dp.register_message_handler(process_comfirmstusdt, state=FormSTUSDT.comfirm)

    # = = = = = STAKING MENU : TRON = = = = = #
    dp.register_callback_query_handler(call_sttron, text="call_sttron")
    dp.register_callback_query_handler(process_numbersttron, state=FormSTTRON.number)
    dp.register_message_handler(process_numbersttron, state=FormSTTRON.number)
    dp.register_message_handler(process_comfirmsttron, state=FormSTTRON.comfirm)

    # = = = = = STAKING MENU : SOLANA = = = = = #
    dp.register_callback_query_handler(call_stsolana, text="call_stsolana")
    dp.register_callback_query_handler(process_numberstsolana, state=FormSTSOLANA.number)
    dp.register_message_handler(process_numberstsolana, state=FormSTSOLANA.number)
    dp.register_message_handler(process_comfirmstsolana, state=FormSTSOLANA.comfirm)

    # = = = = = STAKING MENU : POLKADOT = = = = = #
    dp.register_callback_query_handler(call_stpolkadot, text="call_stpolkadot")
    dp.register_callback_query_handler(process_numberstpolkadot, state=FormSTPOLKADOT.number)
    dp.register_message_handler(process_numberstpolkadot, state=FormSTPOLKADOT.number)
    dp.register_message_handler(process_comfirmstpolkadot, state=FormSTPOLKADOT.comfirm)

    # = = = = = STAKING MENU : BNB = = = = = #
    dp.register_callback_query_handler(call_stbnb, text="call_stbnb")
    dp.register_callback_query_handler(process_numberstbnb, state=FormSTBNB.number)
    dp.register_message_handler(process_numberstbnb, state=FormSTBNB.number)
    dp.register_message_handler(process_comfirmstbnb, state=FormSTBNB.comfirm)
