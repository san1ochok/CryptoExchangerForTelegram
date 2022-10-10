# -*- coding: utf-8 -*-
# = = = = = = = IMPORTS = = = = = = = #
from aiogram import Dispatcher, Bot, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from handlers import db
import config
from handlers import start_place as st
from handlers import p2p_exchanger as ex

bot = Bot(token=config.token, parse_mode=config.parse_mode)
dp = Dispatcher(bot)


# = = = = = = = FSM.STATES : W.BTC = = = = = = = #
class FormWBTC(StatesGroup):
    number = State()
    adress = State()
    comfirm = State()


# = = = = = = = FSM.STATES : W.ETH = = = = = = = #
class FormWETH(StatesGroup):
    number = State()
    adress = State()
    comfirm = State()


# = = = = = = = FSM.STATES : W.SOL = = = = = = = #
class FormWSOL(StatesGroup):
    number = State()
    adress = State()
    comfirm = State()


# = = = = = = = FSM.STATES : W.USDT = = = = = = = #
class FormWUSDT(StatesGroup):
    number = State()
    adress = State()
    comfirm = State()


# = = = = = = = FSM.STATES : W.BNB = = = = = = = #
class FormWBNB(StatesGroup):
    number = State()
    adress = State()
    comfirm = State()


# = = = = = = = FSM.STATES : W.CARDANO = = = = = = = #
class FormWCARDANO(StatesGroup):
    number = State()
    adress = State()
    comfirm = State()


# = = = = = = = FSM.STATES : W.TRON = = = = = = = #
class FormWTRON(StatesGroup):
    number = State()
    adress = State()
    comfirm = State()


# = = = = = = = FSM.STATES : W.BUSD = = = = = = = #
class FormWBUSD(StatesGroup):
    number = State()
    adress = State()
    comfirm = State()


# = = = = = = = FSM.STATES : W.POLKADOT = = = = = = = #
class FormWPOLKADOT(StatesGroup):
    number = State()
    adress = State()
    comfirm = State()


# = = = = = = = FSM.STATES : W.MATIC = = = = = = = #
class FormWMATIC(StatesGroup):
    number = State()
    adress = State()
    comfirm = State()


# = = = = = = = FSM.STATES : W.CWD = = = = = = = #
class FormWCWD(StatesGroup):
    number = State()
    adress = State()
    comfirm = State()


# = = = = = = = FSM.STATES : W.WATT = = = = = = = #
class FormWWATT(StatesGroup):
    number = State()
    adress = State()
    comfirm = State()


# = = = = = = = FSM.STATES : P.BTC = = = = = = = #
class FormPBTC(StatesGroup):
    number = State()
    comfirm = State()


# = = = = = = = FSM.STATES : P.ETH = = = = = = = #
class FormPETH(StatesGroup):
    number = State()
    comfirm = State()


# = = = = = = = FSM.STATES : P.SOL = = = = = = = #
class FormPSOL(StatesGroup):
    number = State()
    comfirm = State()


# = = = = = = = FSM.STATES : P.USDT = = = = = = = #
class FormPUSDT(StatesGroup):
    number = State()
    comfirm = State()


# = = = = = = = FSM.STATES : P.BNB = = = = = = = #
class FormPBNB(StatesGroup):
    number = State()
    comfirm = State()


# = = = = = = = FSM.STATES : P.CARDANO = = = = = = = #
class FormPCARDANO(StatesGroup):
    number = State()
    comfirm = State()


# = = = = = = = FSM.STATES : P.TRON = = = = = = = #
class FormPTRON(StatesGroup):
    number = State()
    comfirm = State()


# = = = = = = = FSM.STATES : P.BUSD = = = = = = = #
class FormPBUSD(StatesGroup):
    number = State()
    comfirm = State()


# = = = = = = = FSM.STATES : P.POLKADOT = = = = = = = #
class FormPPOLKADOT(StatesGroup):
    number = State()
    comfirm = State()


# = = = = = = = FSM.STATES : P.MATIC = = = = = = = #
class FormPMATIC(StatesGroup):
    number = State()
    comfirm = State()


# = = = = = = = FSM.STATES : P.CWD = = = = = = = #
class FormPCWD(StatesGroup):
    number = State()
    comfirm = State()


# = = = = = = = FSM.STATES : P.WATT = = = = = = = #
class FormPWATT(StatesGroup):
    number = State()
    comfirm = State()


# = = = = = = = WALLET STABLE CALLBACK.QUERY BUTTONS : WITHDRAW = = = = = = = #
btnWBitcoin = InlineKeyboardButton("Bitcoin", callback_data="call_wbtc")
btnWEthereum = InlineKeyboardButton("Ethereum", callback_data="call_weth")
btnWSolana = InlineKeyboardButton("Solana", callback_data="call_wsol")
btnWUSDT = InlineKeyboardButton("USDT", callback_data="call_wusdt")
btnWBNB = InlineKeyboardButton("BNB", callback_data="call_wbnb")
btnWCardano = InlineKeyboardButton("Cardano", callback_data="call_wcardano")
btnWTron = InlineKeyboardButton("Tron", callback_data="call_wtron")
btnWBUSD = InlineKeyboardButton("BUSD", callback_data="call_wbusd")
btnWPolkadot = InlineKeyboardButton("Polkadot", callback_data="call_wpolkadot")
btnWMatic = InlineKeyboardButton("Matic", callback_data="call_wmatic")
btnWCWD = InlineKeyboardButton("CWD", callback_data="call_wcwd")
btnWWatt = InlineKeyboardButton("Watt", callback_data="call_wwatt")

# = = = = = = = WALLET STABLE CALLBACK.QUERY BUTTONS : PLENISHMENT = = = = = = = #
btnPBitcoin = InlineKeyboardButton("Bitcoin", callback_data="call_pbtc")
btnPEthereum = InlineKeyboardButton("Ethereum", callback_data="call_peth")
btnPSolana = InlineKeyboardButton("Solana", callback_data="call_psol")
btnPUSDT = InlineKeyboardButton("USDT", callback_data="call_pusdt")
btnPBNB = InlineKeyboardButton("BNB", callback_data="call_pbnb")
btnPCardano = InlineKeyboardButton("Cardano", callback_data="call_pcardano")
btnPTron = InlineKeyboardButton("Tron", callback_data="call_ptron")
btnPBUSD = InlineKeyboardButton("BUSD", callback_data="call_pbusd")
btnPPolkadot = InlineKeyboardButton("Polkadot", callback_data="call_ppolkadot")
btnPMatic = InlineKeyboardButton("Matic", callback_data="call_pmatic")
btnPCWD = InlineKeyboardButton("CWD", callback_data="call_pcwd")
btnPWatt = InlineKeyboardButton("Watt", callback_data="call_pwatt")

btnWalletReplenishment = InlineKeyboardButton("📲 Пополнение", callback_data="call_walletreplenishment")
btnWalletWithdraw = InlineKeyboardButton("Вывод 💲", callback_data="call_walletwithdraw")
btnActivePulls = InlineKeyboardButton("Мои пулы 💸", callback_data="call_activepulls")

# = = = = = = = CRS BUTTONS : COMFIRM = = = = = = = #
btnPaid = KeyboardButton("Подтверждаю")

# = = = = = = = P2P BUTTON : CANCEL = = = = = = = #
btnCancel = KeyboardButton("Отмена 🔴")

menuConfirm = ReplyKeyboardMarkup(resize_keyboard=True).add(btnPaid).add(btnCancel)
menuCancel = ReplyKeyboardMarkup(resize_keyboard=True).add(btnCancel)
mainWMenu = InlineKeyboardMarkup(resize_keyboard=True).add(btnWBitcoin, btnWEthereum, btnWSolana).add(btnWUSDT,
                                                                                                      btnWBNB,
                                                                                                      btnWCardano).add(
    btnWTron, btnWBUSD, btnWPolkadot).add(btnWMatic, btnWCWD, btnWWatt)

mainPMenu = InlineKeyboardMarkup(resize_keyboard=True).add(btnPBitcoin, btnPEthereum, btnPSolana).add(btnPUSDT,
                                                                                                      btnPBNB,
                                                                                                      btnPCardano).add(
    btnPTron, btnPBUSD, btnPPolkadot).add(btnPMatic, btnPCWD, btnPWatt)

mainWallet = InlineKeyboardMarkup(resize_keyboard=True).add(btnWalletReplenishment, btnWalletWithdraw).add(
    btnActivePulls)


@dp.message_handler(lambda msg: msg.text.startswith('Кошелёк👛'))
async def val_p2p_exchanger(message: types.Message):
    for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
        time = row[2]
        bitcoin = row[3]
        ethereum = row[4]
        solana = row[5]
        usdt = row[6]
        bnb = row[7]
        cardano = row[8]
        tron = row[9]
        busd = row[10]
        polkadot = row[11]
        matic = row[12]
        cwd = row[13]
        watt = row[14]
        await message.answer(
            f"*Ваш крипто-кошелёк👛*\n\n🔸BTC - `{'{:0.7f}'.format(bitcoin)}`\n🔸ETH - `{'{:0.7f}'.format(ethereum)}`\n🔸SOL - `{'{:0.4f}'.format(solana)}`\n🔸USDT - `{'{:0.4f}'.format(usdt)}`\n🔸BNB - `{'{:0.4f}'.format(bnb)}`\n🔸CARDANO - `{'{:0.4f}'.format(cardano)}`\n🔸TRON - `{'{:0.4f}'.format(tron)}`\n🔸BUSD - `{'{:0.4f}'.format(busd)}`\n🔸POLKADOT - `{'{:0.4f}'.format(polkadot)}`\n🔸MATIC - `{'{:0.4f}'.format(matic)}`\n🔸CWD - `{'{:0.4f}'.format(cwd)}`\n🔸WATT - `{'{:0.4f}'.format(watt)}`",
            reply_markup=mainWallet)


@dp.message_handler(commands="pay")
async def val_pay(message: types.Message):
    try:
        currency = message.text.split()[1]
        number = float(message.text.split()[2])
        user_id = message.text.split()[3]
    except IndexError:
        await message.reply('Не хватает аргументов!\nПример:\n`/give bitcoin 1.00 5414238721`')
        return

    if currency == 'time':
        db.cursor.execute(f"SELECT name FROM users where id = {user_id}")
        if db.cursor.fetchone() is None:
            db.InsertValue(message.from_user.first_name, user_id)
        plus = number
        db.UpdateValue('time', plus, user_id)
        db.con.commit()
        for row in db.cursor.execute(f"SELECT time FROM users where id={user_id}"):
            await message.reply(
                f"Ты перевёл деньги пользователю: <b><a href='tg://user?id={user_id}'>{user_id}</a></b>\nНа данный момент их количество в выбраной валюте, равно <b>{row[0]}</b> {currency}. ✅",
                parse_mode='html')

    elif currency == 'bitcoin':
        db.cursor.execute(f"SELECT name FROM users where id = {user_id}")
        if db.cursor.fetchone() is None:
            db.InsertValue(message.from_user.first_name, user_id)
        plus = number
        db.UpdateValue('bitcoin', plus, user_id)
        db.con.commit()
        for row in db.cursor.execute(f"SELECT bitcoin FROM users where id={user_id}"):
            await message.reply(
                f"Ты перевёл деньги пользователю: <b><a href='tg://user?id={user_id}'>{user_id}</a></b>\nНа данный момент их количество в выбраной валюте, равно <b>{row[0]}</b> {currency}. ✅",
                parse_mode='html')

    elif currency == 'ethereum':
        db.cursor.execute(f"SELECT name FROM users where id = {user_id}")
        if db.cursor.fetchone() is None:
            db.InsertValue(message.from_user.first_name, user_id)
        plus = number
        db.UpdateValue('ethereum', plus, user_id)
        db.con.commit()
        for row in db.cursor.execute(f"SELECT ethereum FROM users where id={user_id}"):
            await message.reply(
                f"Ты перевёл деньги пользователю: <b><a href='tg://user?id={user_id}'>{user_id}</a></b>\nНа данный момент их количество в выбраной валюте, равно <b>{row[0]}</b> {currency}. ✅",
                parse_mode='html')

    elif currency == 'solana':
        db.cursor.execute(f"SELECT name FROM users where id = {user_id}")
        if db.cursor.fetchone() is None:
            db.InsertValue(message.from_user.first_name, user_id)
        plus = number
        db.UpdateValue('solana', plus, user_id)
        db.con.commit()
        for row in db.cursor.execute(f"SELECT solana FROM users where id={user_id}"):
            await message.reply(
                f"Ты перевёл деньги пользователю: <b><a href='tg://user?id={user_id}'>{user_id}</a></b>\nНа данный момент их количество в выбраной валюте, равно <b>{row[0]}</b> {currency}. ✅",
                parse_mode='html')

    elif currency == 'usdt':
        db.cursor.execute(f"SELECT name FROM users where id = {user_id}")
        if db.cursor.fetchone() is None:
            db.InsertValue(message.from_user.first_name, user_id)
        plus = number
        db.UpdateValue('usdt', plus, user_id)
        db.con.commit()
        for row in db.cursor.execute(f"SELECT usdt FROM users where id={user_id}"):
            await message.reply(
                f"Ты перевёл деньги пользователю: <b><a href='tg://user?id={user_id}'>{user_id}</a></b>\nНа данный момент их количество в выбраной валюте, равно <b>{row[0]}</b> {currency}. ✅",
                parse_mode='html')

    elif currency == 'bnb':
        db.cursor.execute(f"SELECT name FROM users where id = {user_id}")
        if db.cursor.fetchone() is None:
            db.InsertValue(message.from_user.first_name, user_id)
        plus = number
        db.UpdateValue('bnb', plus, user_id)
        db.con.commit()
        for row in db.cursor.execute(f"SELECT bnb FROM users where id={user_id}"):
            await message.reply(
                f"Ты перевёл деньги пользователю: <b><a href='tg://user?id={user_id}'>{user_id}</a></b>\nНа данный момент их количество в выбраной валюте, равно <b>{row[0]}</b> {currency}. ✅",
                parse_mode='html')

    elif currency == 'cardano':
        db.cursor.execute(f"SELECT name FROM users where id = {user_id}")
        if db.cursor.fetchone() is None:
            db.InsertValue(message.from_user.first_name, user_id)
        plus = number
        db.UpdateValue('cardano', plus, user_id)
        db.con.commit()
        for row in db.cursor.execute(f"SELECT cardano FROM users where id={user_id}"):
            await message.reply(
                f"Ты перевёл деньги пользователю: <b><a href='tg://user?id={user_id}'>{user_id}</a></b>\nНа данный момент их количество в выбраной валюте, равно <b>{row[0]}</b> {currency}. ✅",
                parse_mode='html')

    elif currency == 'tron':
        db.cursor.execute(f"SELECT name FROM users where id = {user_id}")
        if db.cursor.fetchone() is None:
            db.InsertValue(message.from_user.first_name, user_id)
        plus = number
        db.UpdateValue('tron', plus, user_id)
        db.con.commit()
        for row in db.cursor.execute(f"SELECT tron FROM users where id={user_id}"):
            await message.reply(
                f"Ты перевёл деньги пользователю: <b><a href='tg://user?id={user_id}'>{user_id}</a></b>\nНа данный момент их количество в выбраной валюте, равно <b>{row[0]}</b> {currency}. ✅",
                parse_mode='html')

    elif currency == 'busd':
        db.cursor.execute(f"SELECT name FROM users where id = {user_id}")
        if db.cursor.fetchone() is None:
            db.InsertValue(message.from_user.first_name, user_id)
        plus = number
        db.UpdateValue('busd', plus, user_id)
        db.con.commit()
        for row in db.cursor.execute(f"SELECT busd FROM users where id={user_id}"):
            await message.reply(
                f"Ты перевёл деньги пользователю: <b><a href='tg://user?id={user_id}'>{user_id}</a></b>\nНа данный момент их количество в выбраной валюте, равно <b>{row[0]}</b> {currency}. ✅",
                parse_mode='html')

    elif currency == 'polkadot':
        db.cursor.execute(f"SELECT name FROM users where id = {user_id}")
        if db.cursor.fetchone() is None:
            db.InsertValue(message.from_user.first_name, user_id)
        plus = number
        db.UpdateValue('polkadot', plus, user_id)
        db.con.commit()
        for row in db.cursor.execute(f"SELECT polkadot FROM users where id={user_id}"):
            await message.reply(
                f"Ты перевёл деньги пользователю: <b><a href='tg://user?id={user_id}'>{user_id}</a></b>\nНа данный момент их количество в выбраной валюте, равно <b>{row[0]}</b> {currency}. ✅",
                parse_mode='html')

    elif currency == 'matic':
        db.cursor.execute(f"SELECT name FROM users where id = {user_id}")
        if db.cursor.fetchone() is None:
            db.InsertValue(message.from_user.first_name, user_id)
        plus = number
        db.UpdateValue('matic', plus, user_id)
        db.con.commit()
        for row in db.cursor.execute(f"SELECT matic FROM users where id={user_id}"):
            await message.reply(
                f"Ты перевёл деньги пользователю: <b><a href='tg://user?id={user_id}'>{user_id}</a></b>\nНа данный момент их количество в выбраной валюте, равно <b>{row[0]}</b> {currency}. ✅",
                parse_mode='html')

    elif currency == 'cwd':
        db.cursor.execute(f"SELECT name FROM users where id = {user_id}")
        if db.cursor.fetchone() is None:
            db.InsertValue(message.from_user.first_name, user_id)
        plus = number
        db.UpdateValue('cwd', plus, user_id)
        db.con.commit()
        for row in db.cursor.execute(f"SELECT cwd FROM users where id={user_id}"):
            await message.reply(
                f"Ты перевёл деньги пользователю: <b><a href='tg://user?id={user_id}'>{user_id}</a></b>\nНа данный момент их количество в выбраной валюте, равно <b>{row[0]}</b> {currency}. ✅",
                parse_mode='html')
    elif currency == 'watt':
        db.cursor.execute(f"SELECT name FROM users where id = {user_id}")
        if db.cursor.fetchone() is None:
            db.InsertValue(message.from_user.first_name, user_id)
        plus = number
        db.UpdateValue('watt', plus, user_id)
        db.con.commit()
        for row in db.cursor.execute(f"SELECT watt FROM users where id={user_id}"):
            await message.reply(
                f"Ты перевёл деньги пользователю: <b><a href='tg://user?id={user_id}'>{user_id}</a></b>\nНа данный момент их количество в выбраной валюте, равно <b>{row[0]}</b> {currency}. ✅",
                parse_mode='html')
    else:
        await message.answer("Error : NoSuchCurrency")


@dp.callback_query_handler(text="call_activepulls")
async def val_activepulls(call: types.CallbackQuery):
    for row in db.cursor.execute(f"SELECT * FROM users where id={call.from_user.id}"):
        if row[2] != 0:
            usdt_active = "🟢"
        elif row[2] == 0:
            usdt_active = "🔴"

        if row[20] != 0:
            tron_active = "🟢"
        elif row[20] == 0:
            tron_active = "🔴"

        if row[21] != 0:
            solana_active = "🟢"
        elif row[21] == 0:
            solana_active = "🔴"

        if row[22] != 0:
            polkadot_active = "🟢"
        elif row[22] == 0:
            polkadot_active = "🔴"

        if row[23] != 0:
            bnb_active = "🟢"
        elif row[23] == 0:
            bnb_active = "🔴"
        await call.message.answer(
            f"*Твои Пулы 💸*\n\n*USDT* - {usdt_active}\n*TRON* - {tron_active}\n*Solana* - {solana_active}\n*Polkadot* - {polkadot_active}\n*BNB* - {bnb_active}\n")


@dp.message_handler(lambda msg: msg.text.startswith("Отмена 🔴"))
async def val_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.callback_query_handler(text="call_walletreplenishment")
async def call_walletreplenishment(call: types.CallbackQuery):
    await call.message.answer("Выберите валюту которую хотите купить:", reply_markup=mainPMenu)


# = = = = = = = BTC : PLENISHMENT = = = = = = = #
@dp.callback_query_handler(text="call_pbtc")
async def call_pbtc(call: types.CallbackQuery):
    await FormPBTC.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormPBTC.number)
async def process_numberpbtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
        else:
            data['number'] = message.text
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            user_id = message.from_user.id
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы покупаете:* `{data['number']}` *BTC*\n*К оплате:* `{float(ex.rubinbtc) * num}` *₽*\n*Реквизиты для оплаты:* `{config.card}`\n\nПосле оплаты не забудьте нажать кнопку «Подтверждаю» и ожидайте одобрения Администратора")
            await FormPBTC.next()
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormPBTC.comfirm)
async def process_comfirmpbtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#PLENISHMENT_\n\n📄 *Чек пользователя*\n\n*Он покупает:* `{data['number']}` *BTC*\n*Оплатил:* `{float(ex.rubinbtc) * num}` *₽*\n*Ваши реквизиты оплаты:* `{config.card}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay bitcoin 0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = ETH : PLENISHMENT = = = = = = = #
@dp.callback_query_handler(text="call_peth")
async def call_peth(call: types.CallbackQuery):
    await FormPETH.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormPETH.number)
async def process_numberpeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
        else:
            data['number'] = message.text
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await FormPETH.next()
            user_id = message.from_user.id
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы покупаете:* `{data['number']}` *ETH*\n*К оплате:* `{float(ex.rubineth) * num}` *₽*\n*Реквизиты для оплаты:* `{config.card}`\n\nПосле оплаты не забудьте нажать кнопку «Подтверждаю» и ожидайте одобрения Администратора")

            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormPETH.comfirm)
async def process_comfirmpeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#PLENISHMENT_\n\n📄 *Чек пользователя*\n\n*Он покупает:* `{data['number']}` *ETH*\n*Оплатил:* `{float(ex.rubineth) * num}` *₽*\n*Ваши реквизиты оплаты:* `{config.card}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay ethereum 0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = SOL : PLENISHMENT = = = = = = = #
@dp.callback_query_handler(text="call_psol")
async def call_psol(call: types.CallbackQuery):
    await FormPSOL.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormPSOL.number)
async def process_numberpsol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
        else:
            data['number'] = message.text
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await FormPSOL.next()
            user_id = message.from_user.id
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы покупаете:* `{data['number']}` *SOL*\n*К оплате:* `{float(ex.rubinsol) * num}` *₽*\n*Реквизиты для оплаты:* `{config.card}`\n\nПосле оплаты не забудьте нажать кнопку «Подтверждаю» и ожидайте одобрения Администратора")

            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormPSOL.comfirm)
async def process_comfirmpsol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#PLENISHMENT_\n\n📄 *Чек пользователя*\n\n*Он покупает:* `{data['number']}` *SOL*\n*Оплатил:* `{float(ex.rubinsol) * num}` *₽*\n*Ваши реквизиты оплаты:* `{config.card}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay solana 0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = USDT : PLENISHMENT = = = = = = = #
@dp.callback_query_handler(text="call_pusdt")
async def call_pusdt(call: types.CallbackQuery):
    await FormPUSDT.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormPUSDT.number)
async def process_numberpusdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
        else:
            data['number'] = message.text
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await FormPUSDT.next()
            user_id = message.from_user.id
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы покупаете:* `{data['number']}` *USDT*\n*К оплате:* `{float(ex.rubinusdt) * num}` *₽*\n*Реквизиты для оплаты:* `{config.card}`\n\nПосле оплаты не забудьте нажать кнопку «Подтверждаю» и ожидайте одобрения Администратора")

            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormPUSDT.comfirm)
async def process_comfirmpusdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#PLENISHMENT_\n\n📄 *Чек пользователя*\n\n*Он покупает:* `{data['number']}` *USDT*\n*Оплатил:* `{float(ex.rubinusdt) * num}` *₽*\n*Ваши реквизиты оплаты:* `{config.card}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay usdt 0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = BNB : PLENISHMENT = = = = = = = #
@dp.callback_query_handler(text="call_pbnb")
async def call_pbnb(call: types.CallbackQuery):
    await FormPBNB.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormPBNB.number)
async def process_numberpbnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
        else:
            data['number'] = message.text
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await FormPBNB.next()
            user_id = message.from_user.id
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы покупаете:* `{data['number']}` *BNB*\n*К оплате:* `{float(ex.rubinbnb) * num}` *₽*\n*Реквизиты для оплаты:* `{config.card}`\n\nПосле оплаты не забудьте нажать кнопку «Подтверждаю» и ожидайте одобрения Администратора")

            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormPBNB.comfirm)
async def process_comfirmpbnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#PLENISHMENT_\n\n📄 *Чек пользователя*\n\n*Он покупает:* `{data['number']}` *BNB*\n*Оплатил:* `{float(ex.rubinbnb) * num}` *₽*\n*Ваши реквизиты оплаты:* `{config.card}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay bnb 0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = CARDANO : PLENISHMENT = = = = = = = #
@dp.callback_query_handler(text="call_pcardano")
async def call_pcardano(call: types.CallbackQuery):
    await FormPCARDANO.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormPCARDANO.number)
async def process_numberpcardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
        else:
            data['number'] = message.text
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await FormPCARDANO.next()
            user_id = message.from_user.id
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы покупаете:* `{data['number']}` *CARDANO*\n*К оплате:* `{float(ex.rubincardano) * num}` *₽*\n*Реквизиты для оплаты:* `{config.card}`\n\nПосле оплаты не забудьте нажать кнопку «Подтверждаю» и ожидайте одобрения Администратора")

            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormPCARDANO.comfirm)
async def process_comfirmpcardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#PLENISHMENT_\n\n📄 *Чек пользователя*\n\n*Он покупает:* `{data['number']}` *CARDANO*\n*Оплатил:* `{float(ex.rubincardano) * num}` *₽*\n*Ваши реквизиты оплаты:* `{config.card}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay cardano 0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = TRON : PLENISHMENT = = = = = = = #
@dp.callback_query_handler(text="call_ptron")
async def call_ptron(call: types.CallbackQuery):
    await FormPTRON.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormPTRON.number)
async def process_numberptron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
        else:
            data['number'] = message.text
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await FormPTRON.next()
            user_id = message.from_user.id
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы покупаете:* `{data['number']}` *TRON*\n*К оплате:* `{float(ex.rubintron) * num}` *₽*\n*Реквизиты для оплаты:* `{config.card}`\n\nПосле оплаты не забудьте нажать кнопку «Подтверждаю» и ожидайте одобрения Администратора")

            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormPTRON.comfirm)
async def process_comfirmptron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#PLENISHMENT_\n\n📄 *Чек пользователя*\n\n*Он покупает:* `{data['number']}` *TRON*\n*Оплатил:* `{float(ex.rubintron) * num}` *₽*\n*Ваши реквизиты оплаты:* `{config.card}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay tron 0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = BUSD : PLENISHMENT = = = = = = = #
@dp.callback_query_handler(text="call_pbusd")
async def call_pbusd(call: types.CallbackQuery):
    await FormPBUSD.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormPBUSD.number)
async def process_numberpbusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
        else:
            data['number'] = message.text
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await FormPBUSD.next()
            user_id = message.from_user.id
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы покупаете:* `{data['number']}` *BUSD*\n*К оплате:* `{float(ex.rubinbusd) * num}` *₽*\n*Реквизиты для оплаты:* `{config.card}`\n\nПосле оплаты не забудьте нажать кнопку «Подтверждаю» и ожидайте одобрения Администратора")

            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormPBUSD.comfirm)
async def process_comfirmpbusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#PLENISHMENT_\n\n📄 *Чек пользователя*\n\n*Он покупает:* `{data['number']}` *BUSD*\n*Оплатил:* `{float(ex.rubinbusd) * num}` *₽*\n*Ваши реквизиты оплаты:* `{config.card}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay busd 0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = POLKADOT : PLENISHMENT = = = = = = = #
@dp.callback_query_handler(text="call_ppolkadot")
async def call_ppolkadot(call: types.CallbackQuery):
    await FormPPOLKADOT.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormPPOLKADOT.number)
async def process_numberppolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
        else:
            data['number'] = message.text
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await FormPPOLKADOT.next()
            user_id = message.from_user.id
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы покупаете:* `{data['number']}` *POLKADOT*\n*К оплате:* `{float(ex.rubinpolkadot) * num}` *₽*\n*Реквизиты для оплаты:* `{config.card}`\n\nПосле оплаты не забудьте нажать кнопку «Подтверждаю» и ожидайте одобрения Администратора")

            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormPPOLKADOT.comfirm)
async def process_comfirmppolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#PLENISHMENT_\n\n📄 *Чек пользователя*\n\n*Он покупает:* `{data['number']}` *POLKADOT*\n*Оплатил:* `{float(ex.rubinpolkadot) * num}` *₽*\n*Ваши реквизиты оплаты:* `{config.card}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay polkadot 0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = MATIC : PLENISHMENT = = = = = = = #
@dp.callback_query_handler(text="call_pmatic")
async def call_pmatic(call: types.CallbackQuery):
    await FormPMATIC.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormPMATIC.number)
async def process_numberpmatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
        else:
            data['number'] = message.text
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await FormPMATIC.next()
            user_id = message.from_user.id
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы покупаете:* `{data['number']}` *MATIC*\n*К оплате:* `{float(ex.rubinmatic) * num}` *₽*\n*Реквизиты для оплаты:* `{config.card}`\n\nПосле оплаты не забудьте нажать кнопку «Подтверждаю» и ожидайте одобрения Администратора")

            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormPMATIC.comfirm)
async def process_comfirmpmatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#PLENISHMENT_\n\n📄 *Чек пользователя*\n\n*Он покупает:* `{data['number']}` *MATIC*\n*Оплатил:* `{float(ex.rubinmatic) * num}` *₽*\n*Ваши реквизиты оплаты:* `{config.card}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay matic 0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = CWD : PLENISHMENT = = = = = = = #
@dp.callback_query_handler(text="call_pcwd")
async def call_pcwd(call: types.CallbackQuery):
    await FormPCWD.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormPCWD.number)
async def process_numberpcwd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
        else:
            data['number'] = message.text
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await FormPCWD.next()
            user_id = message.from_user.id
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы покупаете:* `{data['number']}` *CWD*\n*К оплате:* `{float(ex.rubincwd) * num}` *₽*\n*Реквизиты для оплаты:* `{config.card}`\n\nПосле оплаты не забудьте нажать кнопку «Подтверждаю» и ожидайте одобрения Администратора")

            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormPCWD.comfirm)
async def process_comfirmpcwd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#PLENISHMENT_\n\n📄 *Чек пользователя*\n\n*Он покупает:* `{data['number']}` *CWD*\n*Оплатил:* `{float(ex.rubincwd) * num}` *₽*\n*Ваши реквизиты оплаты:* `{config.card}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay cwd 0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = WATT : PLENISHMENT = = = = = = = #
@dp.callback_query_handler(text="call_pwatt")
async def call_pwatt(call: types.CallbackQuery):
    await FormPWATT.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormPWATT.number)
async def process_numberpwatt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
        else:
            data['number'] = message.text
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await FormPWATT.next()
            user_id = message.from_user.id
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы покупаете:* `{data['number']}` *WATT*\n*К оплате:* `{float(ex.rubinwatt) * num}` *₽*\n*Реквизиты для оплаты:* `{config.card}`\n\nПосле оплаты не забудьте нажать кнопку «Подтверждаю» и ожидайте одобрения Администратора")

            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormPWATT.comfirm)
async def process_comfirmpwatt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#PLENISHMENT_\n\n📄 *Чек пользователя*\n\n*Он покупает:* `{data['number']}` *WATT*\n*Оплатил:* `{float(ex.rubinwatt) * num}` *₽*\n*Ваши реквизиты оплаты:* `{config.card}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay watt 0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.callback_query_handler(text="call_walletwithdraw")
async def call_walletwithdraw(call: types.CallbackQuery):
    await call.message.answer("Выберите валюту которую хотите вывести:", reply_markup=mainWMenu)


# = = = = = = = BTC : WITHDRAW = = = = = = = #
@dp.callback_query_handler(text="call_wbtc")
async def call_wbtc(call: types.CallbackQuery):
    await FormWBTC.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormWBTC.number)
async def process_numberwbtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            data['number'] = message.text
            if data['number'] == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            if float(data['number']) <= row[3]:
                await FormWBTC.next()
                await message.answer("Введите карту на которую вы хотите перевести, ваши средства:",
                                     reply_markup=types.ReplyKeyboardRemove())
            elif float(data['number']) > row[3]:
                await state.finish()
                await message.answer("На вашем балансе в боте, недостаточно средств, для выполнения данного действия",
                                     reply_markup=st.mainMenu)


@dp.message_handler(state=FormWBTC.adress)
async def process_adresswbtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        data['adress'] = message.text
        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы продаёте:* `{data['number']}` *BTC*\n*Ваша карта:* `{adress}`\n*К пополнению:* `{float(ex.rubinbtc) * num}` *₽*\n\nПосле создания запроса не забудьте нажать кнопку «Подтверждаю» и ожидайте одобрения Администратора")
        await FormWBTC.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormWBTC.comfirm)
async def process_comfirmwbtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#WITHDRAW_\n\n📄 *Чек пользователя*\n\n*Он продаёт:* `{data['number']}` *BTC*\n*Вы должны оплатить:* `{float(ex.rubinbtc) * num}` *₽*\n*Карта пользователя:* `{adress}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay bitcoin -0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = ETH : WITHDRAW = = = = = = = #
@dp.callback_query_handler(text="call_weth")
async def call_weth(call: types.CallbackQuery):
    await FormWETH.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormWETH.number)
async def process_numberweth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            data['number'] = message.text
            if data['number'] == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            if float(data['number']) <= row[4]:
                await FormWETH.next()
                await message.answer("Введите карту на которую вы хотите перевести, ваши средства:",
                                     reply_markup=types.ReplyKeyboardRemove())
            elif float(data['number']) > row[4]:
                await state.finish()
                await message.answer("На вашем балансе в боте, недостаточно средств, для выполнения данного действия",
                                     reply_markup=st.mainMenu)


@dp.message_handler(state=FormWETH.adress)
async def process_adressweth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        data['adress'] = message.text
        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы продаёте:* `{data['number']}` *ETH*\n*Ваша карта:* `{adress}`\n*К пополнению:* `{float(ex.rubineth) * num}` *₽*\n\nПосле создания запроса не забудьте нажать кнопку «Подтверждаю» и ожидайте одобрения Администратора")
        await FormWETH.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormWETH.comfirm)
async def process_comfirmweth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#WITHDRAW_\n\n📄 *Чек пользователя*\n\n*Он продаёт:* `{data['number']}` *ETH*\n*Вы должны оплатить:* `{float(ex.rubineth) * num}` *₽*\n*Карта пользователя:* `{adress}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay ethereum -0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = SOL : WITHDRAW = = = = = = = #
@dp.callback_query_handler(text="call_wsol")
async def call_wsol(call: types.CallbackQuery):
    await FormWSOL.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormWSOL.number)
async def process_numberwsol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            data['number'] = message.text
            if data['number'] == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            if float(data['number']) <= row[5]:
                await FormWSOL.next()
                await message.answer("Введите карту на которую вы хотите перевести, ваши средства:",
                                     reply_markup=types.ReplyKeyboardRemove())
            elif float(data['number']) > row[5]:
                await state.finish()
                await message.answer("На вашем балансе в боте, недостаточно средств, для выполнения данного действия",
                                     reply_markup=st.mainMenu)


@dp.message_handler(state=FormWSOL.adress)
async def process_adresswsol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        data['adress'] = message.text
        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы продаёте:* `{data['number']}` *SOL*\n*Ваша карта:* `{adress}`\n*К пополнению:* `{float(ex.rubinsol) * num}` *₽*\n\nПосле создания запроса не забудьте нажать кнопку «Подтверждаю» и ожидайте одобрения Администратора")
        await FormWSOL.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormWSOL.comfirm)
async def process_comfirmwsol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#WITHDRAW_\n\n📄 *Чек пользователя*\n\n*Он продаёт:* `{data['number']}` *SOL*\n*Вы должны оплатить:* `{float(ex.rubinsol) * num}` *₽*\n*Карта пользователя:* `{adress}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay solana -0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = USDT : WITHDRAW = = = = = = = #
@dp.callback_query_handler(text="call_wusdt")
async def call_wusdt(call: types.CallbackQuery):
    await FormWUSDT.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormWUSDT.number)
async def process_numberwusdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            data['number'] = message.text
            if data['number'] == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            if float(data['number']) <= row[6]:
                await FormWUSDT.next()
                await message.answer("Введите карту на которую вы хотите перевести, ваши средства:",
                                     reply_markup=types.ReplyKeyboardRemove())
            elif float(data['number']) > row[6]:
                await state.finish()
                await message.answer("На вашем балансе в боте, недостаточно средств, для выполнения данного действия",
                                     reply_markup=st.mainMenu)


@dp.message_handler(state=FormWUSDT.adress)
async def process_adresswusdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        data['adress'] = message.text
        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы продаёте:* `{data['number']}` *USDT*\n*Ваша карта:* `{adress}`\n*К пополнению:* `{float(ex.rubinusdt) * num}` *₽*\n\nПосле создания запроса не забудьте нажать кнопку «Подтверждаю» и ожидайте одобрения Администратора")
        await FormWUSDT.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormWUSDT.comfirm)
async def process_comfirmwusdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#WITHDRAW_\n\n📄 *Чек пользователя*\n\n*Он продаёт:* `{data['number']}` *USDT*\n*Вы должны оплатить:* `{float(ex.rubinusdt) * num}` *₽*\n*Карта пользователя:* `{adress}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay usdt -0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = BNB : WITHDRAW = = = = = = = #
@dp.callback_query_handler(text="call_wbnb")
async def call_wbnb(call: types.CallbackQuery):
    await FormWBNB.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormWBNB.number)
async def process_numberwbnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            data['number'] = message.text
            if data['number'] == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            if float(data['number']) <= row[7]:
                await FormWBNB.next()
                await message.answer("Введите карту на которую вы хотите перевести, ваши средства:",
                                     reply_markup=types.ReplyKeyboardRemove())
            elif float(data['number']) > row[7]:
                await state.finish()
                await message.answer("На вашем балансе в боте, недостаточно средств, для выполнения данного действия",
                                     reply_markup=st.mainMenu)


@dp.message_handler(state=FormWBNB.adress)
async def process_adresswbnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        data['adress'] = message.text
        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы продаёте:* `{data['number']}` *BNB*\n*Ваша карта:* `{adress}`\n*К пополнению:* `{float(ex.rubinbnb) * num}` *₽*\n\nПосле создания запроса не забудьте нажать кнопку «Подтверждаю» и ожидайте одобрения Администратора")
        await FormWBNB.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormWBNB.comfirm)
async def process_comfirmwbnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#WITHDRAW_\n\n📄 *Чек пользователя*\n\n*Он продаёт:* `{data['number']}` *BNB*\n*Вы должны оплатить:* `{float(ex.rubinbnb) * num}` *₽*\n*Карта пользователя:* `{adress}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay bnb -0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = CARDANO : WITHDRAW = = = = = = = #
@dp.callback_query_handler(text="call_wcardano")
async def call_wcardano(call: types.CallbackQuery):
    await FormWCARDANO.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormWCARDANO.number)
async def process_numberwcardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            data['number'] = message.text
            if data['number'] == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            if float(data['number']) <= row[8]:
                await FormWCARDANO.next()
                await message.answer("Введите карту на которую вы хотите перевести, ваши средства:",
                                     reply_markup=types.ReplyKeyboardRemove())
            elif float(data['number']) > row[8]:
                await state.finish()
                await message.answer("На вашем балансе в боте, недостаточно средств, для выполнения данного действия",
                                     reply_markup=st.mainMenu)


@dp.message_handler(state=FormWCARDANO.adress)
async def process_adresswcardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        data['adress'] = message.text
        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы продаёте:* `{data['number']}` *CARDANO*\n*Ваша карта:* `{adress}`\n*К пополнению:* `{float(ex.rubincardano) * num}` *₽*\n\nПосле создания запроса не забудьте нажать кнопку «Подтверждаю» и ожидайте одобрения Администратора")
        await FormWCARDANO.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormWCARDANO.comfirm)
async def process_comfirmwcardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#WITHDRAW_\n\n📄 *Чек пользователя*\n\n*Он продаёт:* `{data['number']}` *CARDANO*\n*Вы должны оплатить:* `{float(ex.rubincardano) * num}` *₽*\n*Карта пользователя:* `{adress}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay cardano -0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = TRON : WITHDRAW = = = = = = = #
@dp.callback_query_handler(text="call_wtron")
async def call_wtron(call: types.CallbackQuery):
    await FormWTRON.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormWTRON.number)
async def process_numberwtron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            data['number'] = message.text
            if data['number'] == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            if float(data['number']) <= row[9]:
                await FormWTRON.next()
                await message.answer("Введите карту на которую вы хотите перевести, ваши средства:",
                                     reply_markup=types.ReplyKeyboardRemove())
            elif float(data['number']) > row[9]:
                await state.finish()
                await message.answer("На вашем балансе в боте, недостаточно средств, для выполнения данного действия",
                                     reply_markup=st.mainMenu)


@dp.message_handler(state=FormWTRON.adress)
async def process_adresswtron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        data['adress'] = message.text
        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы продаёте:* `{data['number']}` *TRON*\n*Ваша карта:* `{adress}`\n*К пополнению:* `{float(ex.rubintron) * num}` *₽*\n\nПосле создания запроса не забудьте нажать кнопку «Подтверждаю» и ожидайте одобрения Администратора")
        await FormWTRON.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormWTRON.comfirm)
async def process_comfirmwtron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#WITHDRAW_\n\n📄 *Чек пользователя*\n\n*Он продаёт:* `{data['number']}` *TRON*\n*Вы должны оплатить:* `{float(ex.rubintron) * num}` *₽*\n*Карта пользователя:* `{adress}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay tron -0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = BUSD : WITHDRAW = = = = = = = #
@dp.callback_query_handler(text="call_wbusd")
async def call_wbusd(call: types.CallbackQuery):
    await FormWBUSD.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormWBUSD.number)
async def process_numberwbusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            data['number'] = message.text
            if data['number'] == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            if float(data['number']) <= row[10]:
                await FormWBUSD.next()
                await message.answer("Введите карту на которую вы хотите перевести, ваши средства:",
                                     reply_markup=types.ReplyKeyboardRemove())
            elif float(data['number']) > row[10]:
                await state.finish()
                await message.answer("На вашем балансе в боте, недостаточно средств, для выполнения данного действия",
                                     reply_markup=st.mainMenu)


@dp.message_handler(state=FormWBUSD.adress)
async def process_adresswbusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        data['adress'] = message.text
        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы продаёте:* `{data['number']}` *BUSD*\n*Ваша карта:* `{adress}`\n*К пополнению:* `{float(ex.rubinbusd) * num}` *₽*\n\nПосле создания запроса не забудьте нажать кнопку «Подтверждаю» и ожидайте одобрения Администратора")
        await FormWBUSD.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormWBUSD.comfirm)
async def process_comfirmwbusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#WITHDRAW_\n\n📄 *Чек пользователя*\n\n*Он продаёт:* `{data['number']}` *BUSD*\n*Вы должны оплатить:* `{float(ex.rubinbusd) * num}` *₽*\n*Карта пользователя:* `{adress}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay busd -0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = POLKADOT : WITHDRAW = = = = = = = #
@dp.callback_query_handler(text="call_wpolkadot")
async def call_wpolkadot(call: types.CallbackQuery):
    await FormWPOLKADOT.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormWPOLKADOT.number)
async def process_numberwpolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            data['number'] = message.text
            if data['number'] == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            if float(data['number']) <= row[11]:
                await FormWPOLKADOT.next()
                await message.answer("Введите карту на которую вы хотите перевести, ваши средства:",
                                     reply_markup=types.ReplyKeyboardRemove())
            elif float(data['number']) > row[11]:
                await state.finish()
                await message.answer("На вашем балансе в боте, недостаточно средств, для выполнения данного действия",
                                     reply_markup=st.mainMenu)


@dp.message_handler(state=FormWPOLKADOT.adress)
async def process_adresswpolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        data['adress'] = message.text
        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы продаёте:* `{data['number']}` *POLKADOT*\n*Ваша карта:* `{adress}`\n*К пополнению:* `{float(ex.rubinpolkadot) * num}` *₽*\n\nПосле создания запроса не забудьте нажать кнопку «Подтверждаю» и ожидайте одобрения Администратора")
        await FormWPOLKADOT.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormWPOLKADOT.comfirm)
async def process_comfirmwpolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#WITHDRAW_\n\n📄 *Чек пользователя*\n\n*Он продаёт:* `{data['number']}` *POLKADOT*\n*Вы должны оплатить:* `{float(ex.rubinpolkadot) * num}` *₽*\n*Карта пользователя:* `{adress}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay polkadot -0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = MATIC : WITHDRAW = = = = = = = #
@dp.callback_query_handler(text="call_wmatic")
async def call_wmatic(call: types.CallbackQuery):
    await FormWMATIC.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormWMATIC.number)
async def process_numberwmatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            data['number'] = message.text
            if data['number'] == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            if float(data['number']) <= row[12]:
                await FormWMATIC.next()
                await message.answer("Введите карту на которую вы хотите перевести, ваши средства:",
                                     reply_markup=types.ReplyKeyboardRemove())
            elif float(data['number']) > row[12]:
                await state.finish()
                await message.answer("На вашем балансе в боте, недостаточно средств, для выполнения данного действия",
                                     reply_markup=st.mainMenu)


@dp.message_handler(state=FormWMATIC.adress)
async def process_adresswmatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        data['adress'] = message.text
        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы продаёте:* `{data['number']}` *MATIC*\n*Ваша карта:* `{adress}`\n*К пополнению:* `{float(ex.rubinmatic) * num}` *₽*\n\nПосле создания запроса не забудьте нажать кнопку «Подтверждаю» и ожидайте одобрения Администратора")
        await FormWMATIC.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormWMATIC.comfirm)
async def process_comfirmwmatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#WITHDRAW_\n\n📄 *Чек пользователя*\n\n*Он продаёт:* `{data['number']}` *MATIC*\n*Вы должны оплатить:* `{float(ex.rubinmatic) * num}` *₽*\n*Карта пользователя:* `{adress}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay matic -0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = CWD : WITHDRAW = = = = = = = #
@dp.callback_query_handler(text="call_wcwd")
async def call_wcwd(call: types.CallbackQuery):
    await FormWCWD.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormWCWD.number)
async def process_numberwcwd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            data['number'] = message.text
            if data['number'] == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            if float(data['number']) <= row[13]:
                await FormWCWD.next()
                await message.answer("Введите карту на которую вы хотите перевести, ваши средства:",
                                     reply_markup=types.ReplyKeyboardRemove())
            elif float(data['number']) > row[13]:
                await state.finish()
                await message.answer("На вашем балансе в боте, недостаточно средств, для выполнения данного действия",
                                     reply_markup=st.mainMenu)


@dp.message_handler(state=FormWCWD.adress)
async def process_adresswcwd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        data['adress'] = message.text
        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы продаёте:* `{data['number']}` *CWD*\n*Ваша карта:* `{adress}`\n*К пополнению:* `{float(ex.rubincwd) * num}` *₽*\n\nПосле создания запроса не забудьте нажать кнопку «Подтверждаю» и ожидайте одобрения Администратора")
        await FormWCWD.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormWCWD.comfirm)
async def process_comfirmwcwd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#WITHDRAW_\n\n📄 *Чек пользователя*\n\n*Он продаёт:* `{data['number']}` *CWD*\n*Вы должны оплатить:* `{float(ex.rubincwd) * num}` *₽*\n*Карта пользователя:* `{adress}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay cwd -0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = WATT : WITHDRAW = = = = = = = #
@dp.callback_query_handler(text="call_wwatt")
async def call_wwatt(call: types.CallbackQuery):
    await FormWWATT.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormWWATT.number)
async def process_numberwwatt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            data['number'] = message.text
            if data['number'] == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            if float(data['number']) <= row[14]:
                await FormWWATT.next()
                await message.answer("Введите карту на которую вы хотите перевести, ваши средства:",
                                     reply_markup=types.ReplyKeyboardRemove())
            elif float(data['number']) > row[14]:
                await state.finish()
                await message.answer("На вашем балансе в боте, недостаточно средств, для выполнения данного действия",
                                     reply_markup=st.mainMenu)


@dp.message_handler(state=FormWWATT.adress)
async def process_adresswwatt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        data['adress'] = message.text
        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы продаёте:* `{data['number']}` *WATT*\n*Ваша карта:* `{adress}`\n*К пополнению:* `{float(ex.rubinwatt) * num}` *₽*\n\nПосле создания запроса не забудьте нажать кнопку «Подтверждаю» и ожидайте одобрения Администратора")
        await FormWWATT.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormWWATT.comfirm)
async def process_comfirmwwatt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#WITHDRAW_\n\n📄 *Чек пользователя*\n\n*Он продаёт:* `{data['number']}` *WATT*\n*Вы должны оплатить:* `{float(ex.rubinwatt) * num}` *₽*\n*Карта пользователя:* `{adress}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay watt -0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = REGISTER HANDLERS = = = = = = = #
def register_handlers_wallet(dp: Dispatcher):
    dp.register_message_handler(val_p2p_exchanger, lambda msg: msg.text.startswith('Кошелёк👛'))
    dp.register_message_handler(val_pay, commands="pay")
    dp.register_message_handler(val_cancel, lambda msg: msg.text.startswith("Отмена 🔴"))

    dp.register_callback_query_handler(call_walletreplenishment, text="call_walletreplenishment")
    dp.register_callback_query_handler(call_walletwithdraw, text="call_walletwithdraw")
    dp.register_callback_query_handler(val_activepulls, text="call_activepulls")

    # = = = = BITCOIN : WITHDRAW = = = = = #
    dp.register_callback_query_handler(call_wbtc, text="call_wbtc")
    dp.register_message_handler(process_numberwbtc, state=FormWBTC.number)
    dp.register_message_handler(process_adresswbtc, state=FormWBTC.adress)
    dp.register_message_handler(process_comfirmwbtc, state=FormWBTC.comfirm)

    # = = = = ETHEREUM : WITHDRAW = = = = = #
    dp.register_callback_query_handler(call_weth, text="call_weth")
    dp.register_message_handler(process_numberweth, state=FormWETH.number)
    dp.register_message_handler(process_adressweth, state=FormWETH.adress)
    dp.register_message_handler(process_comfirmweth, state=FormWETH.comfirm)

    # = = = = SOLANA : WITHDRAW = = = = = #
    dp.register_callback_query_handler(call_wsol, text="call_wsol")
    dp.register_message_handler(process_numberwsol, state=FormWSOL.number)
    dp.register_message_handler(process_adresswsol, state=FormWSOL.adress)
    dp.register_message_handler(process_comfirmwsol, state=FormWSOL.comfirm)

    # = = = = USDT : WITHDRAW = = = = = #
    dp.register_callback_query_handler(call_wusdt, text="call_wusdt")
    dp.register_message_handler(process_numberwusdt, state=FormWUSDT.number)
    dp.register_message_handler(process_adresswusdt, state=FormWUSDT.adress)
    dp.register_message_handler(process_comfirmwusdt, state=FormWUSDT.comfirm)

    # = = = = BNB : WITHDRAW = = = = = #
    dp.register_callback_query_handler(call_wbnb, text="call_wbnb")
    dp.register_message_handler(process_numberwbnb, state=FormWBNB.number)
    dp.register_message_handler(process_adresswbnb, state=FormWBNB.adress)
    dp.register_message_handler(process_comfirmwbnb, state=FormWBNB.comfirm)

    # = = = = CARDANO : WITHDRAW = = = = = #
    dp.register_callback_query_handler(call_wcardano, text="call_wcardano")
    dp.register_message_handler(process_numberwcardano, state=FormWCARDANO.number)
    dp.register_message_handler(process_adresswcardano, state=FormWCARDANO.adress)
    dp.register_message_handler(process_comfirmwcardano, state=FormWCARDANO.comfirm)

    # = = = = TRON : WITHDRAW = = = = = #
    dp.register_callback_query_handler(call_wtron, text="call_wtron")
    dp.register_message_handler(process_numberwtron, state=FormWTRON.number)
    dp.register_message_handler(process_adresswtron, state=FormWTRON.adress)
    dp.register_message_handler(process_comfirmwtron, state=FormWTRON.comfirm)

    # = = = = BUSD : WITHDRAW = = = = = #
    dp.register_callback_query_handler(call_wbusd, text="call_wbusd")
    dp.register_message_handler(process_numberwbusd, state=FormWBUSD.number)
    dp.register_message_handler(process_adresswbusd, state=FormWBUSD.adress)
    dp.register_message_handler(process_comfirmwbusd, state=FormWBUSD.comfirm)

    # = = = = POLKADOT : WITHDRAW = = = = = #
    dp.register_callback_query_handler(call_wpolkadot, text="call_wpolkadot")
    dp.register_message_handler(process_numberwpolkadot, state=FormWPOLKADOT.number)
    dp.register_message_handler(process_adresswpolkadot, state=FormWPOLKADOT.adress)
    dp.register_message_handler(process_comfirmwpolkadot, state=FormWPOLKADOT.comfirm)

    # = = = = MATIC : WITHDRAW = = = = = #
    dp.register_callback_query_handler(call_wmatic, text="call_wmatic")
    dp.register_message_handler(process_numberwmatic, state=FormWMATIC.number)
    dp.register_message_handler(process_adresswmatic, state=FormWMATIC.adress)
    dp.register_message_handler(process_comfirmwmatic, state=FormWMATIC.comfirm)

    # = = = = CWD : WITHDRAW = = = = = #
    dp.register_callback_query_handler(call_wcwd, text="call_wcwd")
    dp.register_message_handler(process_numberwcwd, state=FormWCWD.number)
    dp.register_message_handler(process_adresswcwd, state=FormWCWD.adress)
    dp.register_message_handler(process_comfirmwcwd, state=FormWCWD.comfirm)

    # = = = = WATT : WITHDRAW = = = = = #
    dp.register_callback_query_handler(call_wwatt, text="call_wwatt")
    dp.register_message_handler(process_numberwwatt, state=FormWWATT.number)
    dp.register_message_handler(process_adresswwatt, state=FormWWATT.adress)
    dp.register_message_handler(process_comfirmwwatt, state=FormWWATT.comfirm)

    # = = = = BITCOIN : PLENISHMENT = = = = = #
    dp.register_callback_query_handler(call_pbtc, text="call_pbtc")
    dp.register_message_handler(process_numberpbtc, state=FormPBTC.number)
    dp.register_message_handler(process_comfirmpbtc, state=FormPBTC.comfirm)

    # = = = = ETHEREUM : PLENISHMENT = = = = = #
    dp.register_callback_query_handler(call_peth, text="call_peth")
    dp.register_message_handler(process_numberpeth, state=FormPETH.number)
    dp.register_message_handler(process_comfirmpeth, state=FormPETH.comfirm)

    # = = = = SOLANA : PLENISHMENT = = = = = #
    dp.register_callback_query_handler(call_psol, text="call_psol")
    dp.register_message_handler(process_numberpsol, state=FormPSOL.number)
    dp.register_message_handler(process_comfirmpsol, state=FormPSOL.comfirm)

    # = = = = USDT : PLENISHMENT = = = = = #
    dp.register_callback_query_handler(call_pusdt, text="call_pusdt")
    dp.register_message_handler(process_numberpusdt, state=FormPUSDT.number)
    dp.register_message_handler(process_comfirmpusdt, state=FormPUSDT.comfirm)

    # = = = = BNB : PLENISHMENT = = = = = #
    dp.register_callback_query_handler(call_pbnb, text="call_pbnb")
    dp.register_message_handler(process_numberpbnb, state=FormPBNB.number)
    dp.register_message_handler(process_comfirmpbnb, state=FormPBNB.comfirm)

    # = = = = CARDANO : PLENISHMENT = = = = = #
    dp.register_callback_query_handler(call_pcardano, text="call_pcardano")
    dp.register_message_handler(process_numberpcardano, state=FormPCARDANO.number)
    dp.register_message_handler(process_comfirmpcardano, state=FormPCARDANO.comfirm)

    # = = = = TRON : PLENISHMENT = = = = = #
    dp.register_callback_query_handler(call_ptron, text="call_ptron")
    dp.register_message_handler(process_numberptron, state=FormPTRON.number)
    dp.register_message_handler(process_comfirmptron, state=FormPTRON.comfirm)

    # = = = = BUSD : PLENISHMENT = = = = = #
    dp.register_callback_query_handler(call_pbusd, text="call_pbusd")
    dp.register_message_handler(process_numberpbusd, state=FormPBUSD.number)
    dp.register_message_handler(process_comfirmpbusd, state=FormPBUSD.comfirm)

    # = = = = POLKADOT : PLENISHMENT = = = = = #
    dp.register_callback_query_handler(call_ppolkadot, text="call_ppolkadot")
    dp.register_message_handler(process_numberppolkadot, state=FormPPOLKADOT.number)
    dp.register_message_handler(process_comfirmppolkadot, state=FormPPOLKADOT.comfirm)

    # = = = = MATIC : PLENISHMENT = = = = = #
    dp.register_callback_query_handler(call_pmatic, text="call_pmatic")
    dp.register_message_handler(process_numberpmatic, state=FormPMATIC.number)
    dp.register_message_handler(process_comfirmpmatic, state=FormPMATIC.comfirm)

    # = = = = CWD : PLENISHMENT = = = = = #
    dp.register_callback_query_handler(call_pcwd, text="call_pcwd")
    dp.register_message_handler(process_numberpcwd, state=FormPCWD.number)
    dp.register_message_handler(process_comfirmpcwd, state=FormPCWD.comfirm)

    # = = = = WATT : PLENISHMENT = = = = = #
    dp.register_callback_query_handler(call_pwatt, text="call_pwatt")
    dp.register_message_handler(process_numberpwatt, state=FormPWATT.number)
    dp.register_message_handler(process_comfirmpwatt, state=FormPWATT.comfirm)
