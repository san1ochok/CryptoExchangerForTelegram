# -*- coding: utf-8 -*-
# = = = = = = = IMPORTS = = = = = = = #
from aiogram import Dispatcher, Bot, types
from handlers import start_place as st
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from bs4 import BeautifulSoup
import requests
import config
from handlers import db

bot = Bot(token=config.token, parse_mode=config.parse_mode)
dp = Dispatcher(bot)

# = = = = = = = USER AGENT = = = = = = = #
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

# = = = = = = = CONVERT : STATES = = = = = = = #
BTC_RUB = 'https://www.google.com/search?q=%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD+%D0%B2+%D1%80%D1%83%D0%B1&ei=RHbaYqivKOSvrgTd4YqYAQ&ved=0ahUKEwio4YS5n4z5AhXkl4sKHd2wAhMQ4dUDCA4&uact=5&oq=%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD+%D0%B2+%D1%80%D1%83%D0%B1&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWOgQIABBHSgQIQRgASgQIRhgAUPgFWPgFYOcHaABwAngAgAGSAYgBkgGSAQMwLjGYAQCgAQHIAQjAAQE&sclient=gws-wiz'

full_page = requests.get(
    BTC_RUB,
    headers=headers
)
soup = BeautifulSoup(
    full_page.content,
    'html.parser'
)
convert = soup.findAll(
    "span", {
        "class": "pclqee"
    }
)

btctorub = convert[0].text
btcrub = btctorub.split()
btcrub = ''.join(btcrub)
rubinbtc = btcrub.replace(",", ".")

# = = = = = = = ETH.TO.RUB CONVERT : STATES = = = = = = = #
ETH_RUB = 'https://www.google.com/search?q=ETH+%D0%BA+%D1%80%D1%83%D0%B1&oq=ETH+%D0%BA+%D1%80%D1%83%D0%B1&aqs=chrome..69i57j0i19l3j0i19i22i30l6.2854j0j7&sourceid=chrome&ie=UTF-8'

full_page = requests.get(
    ETH_RUB,
    headers=headers
)
soup = BeautifulSoup(
    full_page.content,
    'html.parser'
)
convert = soup.findAll(
    "span", {
        "class": "pclqee"
    }
)

ethtorub = convert[0].text
ethrub = ethtorub.split()
ethrub = ''.join(ethrub)
rubineth = ethrub.replace(",", ".")

# = = = = = = = SOL.TO.RUB CONVERT : STATES = = = = = = = #
SOL_RUB = 'https://valuta.exchange/ru/sol-to-rub'

full_page = requests.get(
    SOL_RUB,
    headers=headers
)
soup = BeautifulSoup(
    full_page.content,
    'html.parser'
)
convert = soup.findAll(
    "span", {
        "class": "UpdateTime__ExchangeRate-sc-136xv3i-1 djCdnS"
    }
)

soltorub = convert[0].text
solrub = soltorub.split()
solrub = ''.join(solrub)
rubinsol = solrub.replace(",", ".")

# = = = = = = = USDT.TO.RUB CONVERT : STATES = = = = = = = #
USDT_RUB = 'https://www.google.com/search?q=usdt+rub&ei=XUbdYrXqIcKQrgTEuYFg&ved=0ahUKEwj1jMSXzpH5AhVCiIsKHcRcAAwQ4dUDCA4&uact=5&oq=usdt+rub&gs_lcp=Cgdnd3Mtd2l6EAMyCggAELEDEIMBEEMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgAEEcQsAM6BwgAELADEENKBAhBGABKBAhGGABQrxRYkBtgshxoAXABeACAAckDiAHlCZIBBTMtMS4ymAEAoAEByAEKwAEB&sclient=gws-wiz'

full_page = requests.get(
    USDT_RUB,
    headers=headers
)
soup = BeautifulSoup(
    full_page.content,
    'html.parser'
)
convert = soup.findAll(
    "span", {
        "class": "pclqee"
    }
)

usdttorub = convert[0].text
usdtrub = usdttorub.split()
usdtrub = ''.join(usdtrub)
rubinusdt = usdtrub.replace(",", ".")

# = = = = = = = BNB.TO.RUB CONVERT : STATES = = = = = = = #
BNB_RUB = 'https://www.google.com/search?q=bnb+rub&oq=bnb+rub&aqs=chrome..69i57j0i271l2.2323j0j7&sourceid=chrome&ie=UTF-8'

full_page = requests.get(
    BNB_RUB,
    headers=headers
)
soup = BeautifulSoup(
    full_page.content,
    'html.parser'
)
convert = soup.findAll(
    "span", {
        "class": "pclqee"
    }
)

bnbtorub = convert[0].text
bnbrub = bnbtorub.split()
bnbrub = ''.join(bnbrub)
rubinbnb = bnbrub.replace(",", ".")

# = = = = = = = CARDANO.TO.RUB CONVERT : STATES = = = = = = = #
CARDANO_RUB = 'https://www.google.com/search?q=cardano+rub&ei=al3dYuGTHZGdrwTDpq_ABQ&ved=0ahUKEwjh8KeV5JH5AhWRzosKHUPTC1gQ4dUDCA4&uact=5&oq=cardano+rub&gs_lcp=Cgdnd3Mtd2l6EAMyBAguEA0yBAguEA0yBAguEA0yBAguEA0yBAgAEA0yBAguEA0yBAguEA0yBAgAEA0yBAgAEA0yBAgAEA06BggAEB4QBzoICAAQHhAHEAo6BQgAEIAEOgQIABAeSgQIQRgASgQIRhgAUABYoxNg0xVoAXABeAGAAbgEiAHtDpIBCzAuMy4yLjEuMC4xmAEAoAEBwAEB&sclient=gws-wiz'

full_page = requests.get(
    CARDANO_RUB,
    headers=headers
)
soup = BeautifulSoup(
    full_page.content,
    'html.parser'
)
convert = soup.findAll(
    "span", {
        "class": "pclqee"
    }
)

cardanotorub = convert[0].text
cardanorub = cardanotorub.split()
cardanorub = ''.join(cardanorub)
rubincardano = cardanorub.replace(",", ".")

# = = = = = = = TRON.TO.RUB CONVERT : STATES = = = = = = = #
TRON_RUB = 'https://www.google.com/search?q=TRON+TO+RUB&oq=TRON+TO+RUB&aqs=chrome..69i57j0i512j0i10i22i30.2733j0j7&sourceid=chrome&ie=UTF-8'

full_page = requests.get(
    TRON_RUB,
    headers=headers
)
soup = BeautifulSoup(
    full_page.content,
    'html.parser'
)
convert = soup.findAll(
    "span", {
        "class": "pclqee"
    }
)

trontorub = convert[0].text
tronrub = trontorub.split()
tronrub = ''.join(tronrub)
rubintron = tronrub.replace(",", ".")

# = = = = = = = BUSD.TO.RUB CONVERT : STATES = = = = = = = #
BUSD_RUB = 'https://www.google.com/search?q=usdt+rub&ei=XUbdYrXqIcKQrgTEuYFg&ved=0ahUKEwj1jMSXzpH5AhVCiIsKHcRcAAwQ4dUDCA4&uact=5&oq=usdt+rub&gs_lcp=Cgdnd3Mtd2l6EAMyCggAELEDEIMBEEMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgAEEcQsAM6BwgAELADEENKBAhBGABKBAhGGABQrxRYkBtgshxoAXABeACAAckDiAHlCZIBBTMtMS4ymAEAoAEByAEKwAEB&sclient=gws-wiz'

full_page = requests.get(
    BUSD_RUB,
    headers=headers
)
soup = BeautifulSoup(
    full_page.content,
    'html.parser'
)
convert = soup.findAll(
    "span", {
        "class": "pclqee"
    }
)

busdtorub = convert[0].text
busdrub = busdtorub.split()
busdrub = ''.join(busdrub)
rubinbusd = busdrub.replace(",", ".")

# = = = = = = = POLKADOT.TO.RUB CONVERT : STATES = = = = = = = #
POLKADOT_RUB = 'https://valuta.exchange/ru/dot-to-rub'

full_page = requests.get(
    POLKADOT_RUB,
    headers=headers
)
soup = BeautifulSoup(
    full_page.content,
    'html.parser'
)
convert = soup.findAll(
    "span", {
        "class": "UpdateTime__ExchangeRate-sc-136xv3i-1 djCdnS"
    }
)

polkadottorub = convert[0].text
polkadotrub = polkadottorub.split()
polkadotrub = ''.join(polkadotrub)
rubinpolkadot = polkadotrub.replace(",", ".")

# = = = = = = = MATIC.TO.RUB CONVERT : STATES = = = = = = = #
MATIC_RUB = 'https://www.google.com/search?q=matic+to+rub&oq=matic+to+rub&aqs=chrome..69i57j0i10i22i30j0i15i22i30.4373j0j7&sourceid=chrome&ie=UTF-8'

full_page = requests.get(
    MATIC_RUB,
    headers=headers
)
soup = BeautifulSoup(
    full_page.content,
    'html.parser'
)
convert = soup.findAll(
    "div", {
        "class": "IZ6rdc"
    }
)

matictorub = convert[0].text
maticrub = matictorub.split()
maticrub = ''.join(maticrub)
rubinmatic = maticrub.replace(",", ".")

# = = = = = = = WATT.TO.RUB CONVERT : STATES = = = = = = = #
WATT_RUB = 'https://www.google.com/search?q=1.60+dol+to+rub&oq=1.60+dol+&aqs=chrome.0.69i59l2j69i57j69i60.3592j0j4&sourceid=chrome&ie=UTF-8'

full_page = requests.get(
    WATT_RUB,
    headers=headers
)
soup = BeautifulSoup(
    full_page.content,
    'html.parser'
)
convert = soup.findAll(
    "span", {
        "class": "DFlfde",
        "class": "SwHCTb",
        "data-precision": 2
    }
)

watttorub = convert[0].text
wattrub = watttorub.split()
wattrub = ''.join(wattrub)
rubinwatt = wattrub.replace(",", ".")


# = = = = = = = FSM.STATES : BITCOIN = = = = = = = #
class FormBuyBTC(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormSellBTC(StatesGroup):
    number = State()
    adress = State()
    comfirm = State()


# = = = = = = = FSM.STATES : ETHEREUM = = = = = = = #
class FormBuyETH(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormSellETH(StatesGroup):
    number = State()
    adress = State()
    comfirm = State()


# = = = = = = = FSM.STATES : SOLANA = = = = = = = #
class FormBuySOL(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormSellSOL(StatesGroup):
    number = State()
    adress = State()
    comfirm = State()


# = = = = = = = FSM.STATES : USDT = = = = = = = #
class FormBuyUSDT(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormSellUSDT(StatesGroup):
    number = State()
    adress = State()
    comfirm = State()


# = = = = = = = FSM.STATES : BNB = = = = = = = #
class FormBuyBNB(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormSellBNB(StatesGroup):
    number = State()
    adress = State()
    comfirm = State()


# = = = = = = = FSM.STATES : CARDANO = = = = = = = #
class FormBuyCARDANO(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormSellCARDANO(StatesGroup):
    number = State()
    adress = State()
    comfirm = State()


# = = = = = = = FSM.STATES : TRON = = = = = = = #
class FormBuyTRON(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormSellTRON(StatesGroup):
    number = State()
    adress = State()
    comfirm = State()


# = = = = = = = FSM.STATES : BUSD = = = = = = = #
class FormBuyBUSD(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormSellBUSD(StatesGroup):
    number = State()
    adress = State()
    comfirm = State()


# = = = = = = = FSM.STATES : POLKADOT = = = = = = = #
class FormBuyPOLKADOT(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormSellPOLKADOT(StatesGroup):
    number = State()
    adress = State()
    comfirm = State()


# = = = = = = = FSM.STATES : MATIC = = = = = = = #
class FormBuyMATIC(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormSellMATIC(StatesGroup):
    number = State()
    adress = State()
    comfirm = State()


# = = = = = = = FSM.STATES : CWD = = = = = = = #
class FormBuyCWD(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormSellCWD(StatesGroup):
    number = State()
    adress = State()
    comfirm = State()


# = = = = = = = FSM.STATES : WATT = = = = = = = #
class FormBuyWATT(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormSellWATT(StatesGroup):
    number = State()
    adress = State()
    comfirm = State()


# = = = = = = = P2P BUTTONS : BUY/SELL = = = = = = = #
btnP2PBuyBTC = InlineKeyboardButton("🟢 Купить", callback_data="call_p2pbuybtc")
btnP2PSellBTC = InlineKeyboardButton("Продать 🔴", callback_data="call_p2psellbtc")

btnP2PBuyETH = InlineKeyboardButton("🟢 Купить", callback_data="call_p2pbuyeth")
btnP2PSellETH = InlineKeyboardButton("Продать 🔴", callback_data="call_p2pselleth")

btnP2PBuySOL = InlineKeyboardButton("🟢 Купить", callback_data="call_p2pbuysol")
btnP2PSellSOL = InlineKeyboardButton("Продать 🔴", callback_data="call_p2psellsol")

btnP2PBuyUSDT = InlineKeyboardButton("🟢 Купить", callback_data="call_p2pbuyusdt")
btnP2PSellUSDT = InlineKeyboardButton("Продать 🔴", callback_data="call_p2psellusdt")

btnP2PBuyBNB = InlineKeyboardButton("🟢 Купить", callback_data="call_p2pbuybnb")
btnP2PSellBNB = InlineKeyboardButton("Продать 🔴", callback_data="call_p2psellbnb")

btnP2PBuyCARDANO = InlineKeyboardButton("🟢 Купить", callback_data="call_p2pbuycardano")
btnP2PSellCARDANO = InlineKeyboardButton("Продать 🔴", callback_data="call_p2psellcardano")

btnP2PBuyTRON = InlineKeyboardButton("🟢 Купить", callback_data="call_p2pbuytron")
btnP2PSellTRON = InlineKeyboardButton("Продать 🔴", callback_data="call_p2pselltron")

btnP2PBuyBUSD = InlineKeyboardButton("🟢 Купить", callback_data="call_p2pbuybusd")
btnP2PSellBUSD = InlineKeyboardButton("Продать 🔴", callback_data="call_p2psellbusd")

btnP2PBuyPOLKADOT = InlineKeyboardButton("🟢 Купить", callback_data="call_p2pbuypolkadot")
btnP2PSellPOLKADOT = InlineKeyboardButton("Продать 🔴", callback_data="call_p2psellpolkadot")

btnP2PBuyMATIC = InlineKeyboardButton("🟢 Купить", callback_data="call_p2pbuymatic")
btnP2PSellMATIC = InlineKeyboardButton("Продать 🔴", callback_data="call_p2psellmatic")

btnP2PBuyCWD = InlineKeyboardButton("🟢 Купить", callback_data="call_p2pbuycwd")
btnP2PSellCWD = InlineKeyboardButton("Продать 🔴", callback_data="call_p2psellcwd")

btnP2PBuyWATT = InlineKeyboardButton("🟢 Купить", callback_data="call_p2pbuywatt")
btnP2PSellWATT = InlineKeyboardButton("Продать 🔴", callback_data="call_p2psellwatt")

# = = = = = = = P2P STABLE CALLBACK.QUERY BUTTONS = = = = = = = #
btnP2PBitcoin = InlineKeyboardButton("Bitcoin", callback_data="call_p2pbitcoin")
btnP2PEthereum = InlineKeyboardButton("Ethereum", callback_data="call_p2pethereum")
btnP2PSolana = InlineKeyboardButton("Solana", callback_data="call_p2psolana")
btnP2PUSDT = InlineKeyboardButton("USDT", callback_data="call_p2pusdt")
btnP2PBNB = InlineKeyboardButton("BNB", callback_data="call_p2pbnb")
btnP2PCardano = InlineKeyboardButton("Cardano", callback_data="call_p2pcardano")
btnP2PTron = InlineKeyboardButton("Tron", callback_data="call_p2ptron")
btnP2PBUSD = InlineKeyboardButton("BUSD", callback_data="call_p2pbusd")
btnP2PPolkadot = InlineKeyboardButton("Polkadot", callback_data="call_p2ppolkadot")
btnP2PMatic = InlineKeyboardButton("Matic", callback_data="call_p2pmatic")
btnP2PCWD = InlineKeyboardButton("CWD", callback_data="call_p2pcwd")
btnP2PWatt = InlineKeyboardButton("Watt", callback_data="call_p2pwatt")

# = = = = = = = P2P STABLE BUTTONS = = = = = = = #
btnToMyBalance = KeyboardButton("На баланс бота 📲")
btnToAnotherWallet = KeyboardButton("На другой кошелёк 💸")

# = = = = = = = P2P BUTTONS : COMFIRM = = = = = = = #
btnPaid = KeyboardButton("Я оплатил(а)")
btnAgree = KeyboardButton("Я согласен(а)")

# = = = = = = = P2P BUTTON : CANCEL = = = = = = = #
btnCancel = KeyboardButton("Отмена 🔴")

# = = = = = = = P2P STABLE MENUS = = = = = = = #
menuConfirm = ReplyKeyboardMarkup(resize_keyboard=True).add(btnPaid).add(btnCancel)
menuConfirm2 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnAgree).add(btnCancel)
menuBuyTo = ReplyKeyboardMarkup(resize_keyboard=True).add(btnToMyBalance).add(btnToAnotherWallet).add(btnCancel)

menuP2PActionBTC = InlineKeyboardMarkup(resize_keyboard=True).add(btnP2PBuyBTC, btnP2PSellBTC)
menuP2PActionETH = InlineKeyboardMarkup(resize_keyboard=True).add(btnP2PBuyETH, btnP2PSellETH)
menuP2PActionSOL = InlineKeyboardMarkup(resize_keyboard=True).add(btnP2PBuySOL, btnP2PSellSOL)
menuP2PActionUSDT = InlineKeyboardMarkup(resize_keyboard=True).add(btnP2PBuyUSDT, btnP2PSellUSDT)
menuP2PActionBNB = InlineKeyboardMarkup(resize_keyboard=True).add(btnP2PBuyBNB, btnP2PSellBNB)
menuP2PActionCARDANO = InlineKeyboardMarkup(resize_keyboard=True).add(btnP2PBuyCARDANO, btnP2PSellCARDANO)
menuP2PActionTRON = InlineKeyboardMarkup(resize_keyboard=True).add(btnP2PBuyTRON, btnP2PSellTRON)
menuP2PActionBUSD = InlineKeyboardMarkup(resize_keyboard=True).add(btnP2PBuyBUSD, btnP2PSellBUSD)
menuP2PActionPOLKADOT = InlineKeyboardMarkup(resize_keyboard=True).add(btnP2PBuyPOLKADOT, btnP2PSellPOLKADOT)
menuP2PActionMATIC = InlineKeyboardMarkup(resize_keyboard=True).add(btnP2PBuyMATIC, btnP2PSellMATIC)
menuP2PActionCWD = InlineKeyboardMarkup(resize_keyboard=True).add(btnP2PBuyCWD, btnP2PSellCWD)
menuP2PActionWATT = InlineKeyboardMarkup(resize_keyboard=True).add(btnP2PBuyWATT, btnP2PSellWATT)

menuCancel = ReplyKeyboardMarkup(resize_keyboard=True).add(btnCancel)
mainP2P = InlineKeyboardMarkup(resize_keyboard=True).add(btnP2PBitcoin, btnP2PEthereum, btnP2PSolana).add(btnP2PUSDT,
                                                                                                          btnP2PBNB,
                                                                                                          btnP2PCardano).add(
    btnP2PTron, btnP2PBUSD, btnP2PPolkadot).add(btnP2PMatic, btnP2PCWD, btnP2PWatt)


@dp.message_handler(lambda msg: msg.text.startswith('P2P обменник💸'))
async def val_p2p_exchanger(message: types.Message):
    await message.answer("*P2P обменник* – сервис для покупки криптовалюты через перевод на карту",
                         reply_markup=types.ReplyKeyboardRemove())
    await message.answer("Выберите криптовалюту:", reply_markup=mainP2P)


@dp.message_handler(lambda msg: msg.text.startswith("Отмена 🔴"))
async def val_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


# = = = = = = = BTC TO RUB = = = = = = = #
@dp.callback_query_handler(text="call_p2pbitcoin")
async def call_p2p_p2pbitcoin(call: types.CallbackQuery):
    await call.message.answer("🪙 Выберите действие с '*Bitcoin*'", reply_markup=menuP2PActionBTC)
    await call.message.delete()


# = = = = = = = ETH TO RUB = = = = = = = #
@dp.callback_query_handler(text="call_p2pethereum")
async def call_p2p_p2pethereum(call: types.CallbackQuery):
    await call.message.answer("🪙 Выберите действие с '*Ethereum*'", reply_markup=menuP2PActionETH)
    await call.message.delete()


# = = = = = = = SOL TO RUB = = = = = = = #
@dp.callback_query_handler(text="call_p2psolana")
async def call_p2p_p2psolana(call: types.CallbackQuery):
    await call.message.answer("🪙 Выберите действие с '*Solana*'", reply_markup=menuP2PActionSOL)
    await call.message.delete()


# = = = = = = = USDT TO RUB = = = = = = = #
@dp.callback_query_handler(text="call_p2pusdt")
async def call_p2p_p2pusdt(call: types.CallbackQuery):
    await call.message.answer("🪙 Выберите действие с '*USDT*'", reply_markup=menuP2PActionUSDT)
    await call.message.delete()


# = = = = = = = BNB TO RUB = = = = = = = #
@dp.callback_query_handler(text="call_p2pbnb")
async def call_p2p_p2pbnb(call: types.CallbackQuery):
    await call.message.answer("🪙 Выберите действие с '*BNB*'", reply_markup=menuP2PActionBNB)
    await call.message.delete()


# = = = = = = = CARDANO TO RUB = = = = = = = #
@dp.callback_query_handler(text="call_p2pcardano")
async def call_p2p_p2pcardano(call: types.CallbackQuery):
    await call.message.answer("🪙 Выберите действие с '*Cardano*'", reply_markup=menuP2PActionCARDANO)
    await call.message.delete()


# = = = = = = = TRON TO RUB = = = = = = = #
@dp.callback_query_handler(text="call_p2ptron")
async def call_p2p_p2ptron(call: types.CallbackQuery):
    await call.message.answer("🪙 Выберите действие с '*Tron*'", reply_markup=menuP2PActionTRON)
    await call.message.delete()


# = = = = = = = BUSD TO RUB = = = = = = = #
@dp.callback_query_handler(text="call_p2pbusd")
async def call_p2p_p2pbusd(call: types.CallbackQuery):
    await call.message.answer("🪙 Выберите действие с '*BUSD*'", reply_markup=menuP2PActionBUSD)
    await call.message.delete()


# = = = = = = = POLKADOT TO RUB = = = = = = = #
@dp.callback_query_handler(text="call_p2ppolkadot")
async def call_p2p_p2ppolkadot(call: types.CallbackQuery):
    await call.message.answer("🪙 Выберите действие с '*Polkadot*'", reply_markup=menuP2PActionPOLKADOT)
    await call.message.delete()


# = = = = = = = MATIC TO RUB = = = = = = = #
@dp.callback_query_handler(text="call_p2pmatic")
async def call_p2p_p2pmatic(call: types.CallbackQuery):
    await call.message.answer("🪙 Выберите действие с '*Matic*'", reply_markup=menuP2PActionMATIC)
    await call.message.delete()


# = = = = = = = CWD TO RUB = = = = = = = #
@dp.callback_query_handler(text="call_p2pcwd")
async def call_p2p_p2pcwd(call: types.CallbackQuery):
    await call.message.answer("🪙 Выберите действие с '*CWD*'", reply_markup=menuP2PActionCWD)
    await call.message.delete()


# = = = = = = = WATT TO RUB = = = = = = = #
@dp.callback_query_handler(text="call_p2pwatt")
async def call_p2p_p2pwatt(call: types.CallbackQuery):
    await call.message.answer("🪙 Выберите действие с '*WATT*'", reply_markup=menuP2PActionWATT)
    await call.message.delete()


# = = = = = = = BTC TO RUB : BUY = = = = = = = #
@dp.callback_query_handler(text="call_p2pbuybtc")
async def call_p2p_buybitcoin(call: types.CallbackQuery):
    await FormBuyBTC.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormBuyBTC.number)
async def process_numberbuybtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
        else:
            data['number'] = message.text
            await FormBuyBTC.next()
            await message.answer("Куда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormBuyBTC.type)
async def process_typebuybtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['type'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        if data['type'] == "На баланс бота 📲":
            user_id = message.from_user.id
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы покупаете:* `{data['number']}` *BTC*\n*К оплате:* `{float(rubinbtc) * num}` *₽*\n*Реквизиты для оплаты:* `{config.card}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
            await FormBuyBTC.next()
            await FormBuyBTC.next()
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
        elif data['type'] == "На другой кошелёк 💸":
            await FormBuyBTC.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())
        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormBuyBTC.adress)
async def process_adressbuybtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        data['adress'] = message.text
        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы покупаете:* `{data['number']}` *BTC*\nЦелевой адресс: `{adress}`\n*К оплате:* `{float(rubinbtc) * num}` *₽*\n*Реквизиты для оплаты:* `{config.walletBitcoin}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormBuyBTC.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormBuyBTC.comfirm)
async def process_comfirmbuybtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Я оплатил(а)":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#P2P_\n\n📄 *Чек пользователя*\n\n*Он покупает:* `{data['number']}` *BTC*\n*Оплатил:* `{float(rubinbtc) * num}` *₽*\n*Ваши реквизиты оплаты:* `{config.card}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay bitcoin 0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = BTC TO RUB : SELL = = = = = = = #
@dp.callback_query_handler(text="call_p2psellbtc")
async def call_p2p_sellbitcoin(call: types.CallbackQuery):
    await FormSellBTC.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormSellBTC.number)
async def process_numbersellbtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            data['number'] = message.text
            if data['number'] == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            if float(data['number']) <= row[3]:
                await FormSellBTC.next()
                await message.answer("Введите карту на которую вы хотите перевести, ваши средства:",
                                     reply_markup=types.ReplyKeyboardRemove())
            elif float(data['number']) > row[3]:
                await state.finish()
                await message.answer("На вашем балансе в боте, недостаточно средств, для выполнения данного действия",
                                     reply_markup=st.mainMenu)


@dp.message_handler(state=FormSellBTC.adress)
async def process_adresssellbtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        data['adress'] = message.text
        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы продаёте:* `{data['number']}` *BTC*\nВаша карта: `{adress}`\n*К пополнению:* `{float(rubinbtc) * num}` *₽*\n\nПосле создания запроса не забудьте нажать кнопку «Я согласен(а)» и ожидайте одобрения Администратора")
        await FormSellBTC.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm2)


@dp.message_handler(state=FormSellBTC.comfirm)
async def process_comfirmsellbtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Я согласен(а)":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#P2P_\n\n📄 *Чек пользователя*\n\n*Он продаёт:* `{data['number']}` *BTC*\n*Вы должны оплатить:* `{float(rubinbtc) * num}` *₽*\n*Карта пользователя:* `{adress}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay bitcoin -0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = ETH TO RUB : BUY = = = = = = = #
@dp.callback_query_handler(text="call_p2pbuyeth")
async def call_p2p_buyethreum(call: types.CallbackQuery):
    await FormBuyETH.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormBuyETH.number)
async def process_numberbuyeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
        else:
            data['number'] = message.text
            await FormBuyETH.next()
            await message.answer("Куда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormBuyETH.type)
async def process_typebuyeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['type'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        if data['type'] == "На баланс бота 📲":
            user_id = message.from_user.id
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы покупаете:* `{data['number']}` *ETH*\n*К оплате:* `{float(rubineth) * num}` *₽*\n*Реквизиты для оплаты:* `{config.card}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
            await FormBuyETH.next()
            await FormBuyETH.next()
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
        elif data['type'] == "На другой кошелёк 💸":
            await FormBuyETH.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())
        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormBuyETH.adress)
async def process_adressbuyeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        data['adress'] = message.text
        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы покупаете:* `{data['number']}` *ETH*\nЦелевой адресс: `{adress}`\n*К оплате:* `{float(rubineth) * num}` *₽*\n*Реквизиты для оплаты:* `{config.walletEthereum}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormBuyETH.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormBuyETH.comfirm)
async def process_comfirmbuyeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Я оплатил(а)":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            adress = data['adress'] = message.text
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#P2P_\n\n📄 *Чек пользователя*\n\n*Он покупает:* `{data['number']}` *ETH*\n*Оплатил:* `{float(rubineth) * num}` *₽*\n*Ваши реквизиты оплаты:* `{config.card}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay ethereum 0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = ETH TO RUB : SELL = = = = = = = #
@dp.callback_query_handler(text="call_p2pselleth")
async def call_p2p_sellethereum(call: types.CallbackQuery):
    await FormSellETH.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormSellETH.number)
async def process_numberselleth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
        else:
            for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
                data['number'] = message.text
                if float(data['number']) <= row[4]:
                    await FormSellETH.next()
                    await message.answer("Введите карту на которую вы хотите перевести, ваши средства:",
                                         reply_markup=menuCancel)
                elif float(data['number']) > row[4]:
                    await state.finish()
                    await message.answer(
                        "На вашем балансе в боте, недостаточно средств, для выполнения данного действия",
                        reply_markup=st.mainMenu)


@dp.message_handler(state=FormSellETH.adress)
async def process_adressselleth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
        else:
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            adress = data['adress'] = message.text
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы продаёте:* `{data['number']}` *ETH*\nВаша карта: `{adress}`\n*К пополнению:* `{float(rubineth) * num}` *₽*\n\nПосле создания запроса не забудьте нажать кнопку «Я согласен(а)» и ожидайте одобрения Администратора")
            await FormSellETH.next()
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm2)


@dp.message_handler(state=FormSellETH.comfirm)
async def process_comfirmselleth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Я согласен(а)":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#P2P_\n\n📄 *Чек пользователя*\n\n*Он продаёт:* `{data['number']}` *ETH*\n*Вы должны оплатить:* `{float(rubineth) * num}` *₽*\n*Карта пользователя:* `{adress}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay ethereum -0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = SOL TO RUB : BUY = = = = = = = #
@dp.callback_query_handler(text="call_p2pbuysol")
async def call_p2p_buysolana(call: types.CallbackQuery):
    await FormBuySOL.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormBuySOL.number)
async def process_numberbuysol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
        else:
            data['number'] = message.text
            await FormBuySOL.next()
            await message.answer("Куда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormBuySOL.type)
async def process_typebuysol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['type'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        if data['type'] == "На баланс бота 📲":
            user_id = message.from_user.id
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы покупаете:* `{data['number']}` *SOL*\n*К оплате:* `{float(rubinsol) * num}` *₽*\n*Реквизиты для оплаты:* `{config.card}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
            await FormBuySOL.next()
            await FormBuySOL.next()
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
        elif data['type'] == "На другой кошелёк 💸":
            await FormBuySOL.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())
        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormBuySOL.adress)
async def process_adressbuysol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        data['adress'] = message.text
        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы покупаете:* `{data['number']}` *SOL*\nЦелевой адресс: `{adress}`\n*К оплате:* `{float(rubinsol) * num}` *₽*\n*Реквизиты для оплаты:* `{config.walletSolana}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormBuySOL.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormBuySOL.comfirm)
async def process_comfirmbuysol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Я оплатил(а)":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            adress = data['adress'] = message.text
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#P2P_\n\n📄 *Чек пользователя*\n\n*Он покупает:* `{data['number']}` *SOL*\n*Оплатил:* `{float(rubinsol) * num}` *₽*\n*Ваши реквизиты оплаты:* `{config.card}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay solana 0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = SOL TO RUB : SELL = = = = = = = #
@dp.callback_query_handler(text="call_p2psellsol")
async def call_p2p_sellsolana(call: types.CallbackQuery):
    await FormSellSOL.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormSellSOL.number)
async def process_numbersellsol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
        else:
            for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
                data['number'] = message.text
                if float(data['number']) <= row[5]:
                    await FormSellSOL.next()
                    await message.answer("Введите карту на которую вы хотите перевести, ваши средства:",
                                         reply_markup=menuCancel)
                elif float(data['number']) > row[5]:
                    await state.finish()
                    await message.answer(
                        "На вашем балансе в боте, недостаточно средств, для выполнения данного действия",
                        reply_markup=st.mainMenu)


@dp.message_handler(state=FormSellSOL.adress)
async def process_adresssellsol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
        else:
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            adress = data['adress'] = message.text
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы продаёте:* `{data['number']}` *SOL*\nВаша карта: `{adress}`\n*К пополнению:* `{float(rubinsol) * num}` *₽*\n\nПосле создания запроса не забудьте нажать кнопку «Я согласен(а)» и ожидайте одобрения Администратора")
            await FormSellSOL.next()
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm2)


@dp.message_handler(state=FormSellSOL.comfirm)
async def process_comfirmsellsol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Я согласен(а)":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#P2P_\n\n📄 *Чек пользователя*\n\n*Он продаёт:* `{data['number']}` *SOL*\n*Вы должны оплатить:* `{float(rubinsol) * num}` *₽*\n*Карта пользователя:* `{adress}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay solana -0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = USDT TO RUB : BUY = = = = = = = #
@dp.callback_query_handler(text="call_p2pbuyusdt")
async def call_p2p_buyusdt(call: types.CallbackQuery):
    await FormBuyUSDT.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormBuyUSDT.number)
async def process_numberbuyusdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
        else:
            data['number'] = message.text
            await FormBuyUSDT.next()
            await message.answer("Куда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormBuyUSDT.type)
async def process_typebuyusdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['type'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        if data['type'] == "На баланс бота 📲":
            user_id = message.from_user.id
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы покупаете:* `{data['number']}` *USDT*\n*К оплате:* `{float(rubinusdt) * num}` *₽*\n*Реквизиты для оплаты:* `{config.card}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
            await FormBuyUSDT.next()
            await FormBuyUSDT.next()
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
        elif data['type'] == "На другой кошелёк 💸":
            await FormBuyUSDT.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())
        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormBuyUSDT.adress)
async def process_adressbuyusdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        data['adress'] = message.text
        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы покупаете:* `{data['number']}` *USDT*\nЦелевой адресс: `{adress}`\n*К оплате:* `{float(rubinusdt) * num}` *₽*\n*Реквизиты для оплаты:* ERC-20 -`{config.walletUSDT_ERC20}`\nTRC-20 -`{config.walletUSDT_TRC20}`\nPOLYGON -`{config.walletUSDT_POLYGON}`\nBEP-20 -`{config.walletUSDT_BEP20}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormBuyUSDT.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormBuyUSDT.comfirm)
async def process_comfirmbuyusdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Я оплатил(а)":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            adress = data['adress'] = message.text
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#P2P_\n\n📄 *Чек пользователя*\n\n*Он покупает:* `{data['number']}` *USDT*\n*Оплатил:* `{float(rubinusdt) * num}` *₽*\n*Ваши реквизиты оплаты:* `{config.card}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay usdt 0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = USDT TO RUB : SELL = = = = = = = #
@dp.callback_query_handler(text="call_p2psellusdt")
async def call_p2p_sellusdt(call: types.CallbackQuery):
    await FormSellUSDT.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormSellUSDT.number)
async def process_numbersellusdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
        else:
            for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
                data['number'] = message.text
                if float(data['number']) <= row[6]:
                    await FormSellUSDT.next()
                    await message.answer("Введите карту на которую вы хотите перевести, ваши средства:",
                                         reply_markup=menuCancel)
                elif float(data['number']) > row[6]:
                    await state.finish()
                    await message.answer(
                        "На вашем балансе в боте, недостаточно средств, для выполнения данного действия",
                        reply_markup=st.mainMenu)


@dp.message_handler(state=FormSellUSDT.adress)
async def process_adresssellusdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
        else:
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            adress = data['adress'] = message.text
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы продаёте:* `{data['number']}` *USDT*\nВаша карта: `{adress}`\n*К пополнению:* `{float(rubinusdt) * num}` *₽*\n\nПосле создания запроса не забудьте нажать кнопку «Я согласен(а)» и ожидайте одобрения Администратора")
            await FormSellUSDT.next()
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm2)


@dp.message_handler(state=FormSellUSDT.comfirm)
async def process_comfirmsellusdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Я согласен(а)":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#P2P_\n\n📄 *Чек пользователя*\n\n*Он продаёт:* `{data['number']}` *USDT*\n*Вы должны оплатить:* `{float(rubinusdt) * num}` *₽*\n*Карта пользователя:* `{adress}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay usdt -0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = BNB TO RUB : BUY = = = = = = = #
@dp.callback_query_handler(text="call_p2pbuybnb")
async def call_p2p_buybnb(call: types.CallbackQuery):
    await FormBuyBNB.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormBuyBNB.number)
async def process_numberbuybnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
        else:
            data['number'] = message.text
            await FormBuyBNB.next()
            await message.answer("Куда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormBuyBNB.type)
async def process_typebuybnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['type'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        if data['type'] == "На баланс бота 📲":
            user_id = message.from_user.id
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы покупаете:* `{data['number']}` *BNB*\n*К оплате:* `{float(rubinbnb) * num}` *₽*\n*Реквизиты для оплаты:* `{config.card}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
            await FormBuyBNB.next()
            await FormBuyBNB.next()
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
        elif data['type'] == "На другой кошелёк 💸":
            await FormBuyBNB.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())
        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormBuyBNB.adress)
async def process_adressbuybnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        data['adress'] = message.text
        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы покупаете:* `{data['number']}` *BNB*\nЦелевой адресс: `{adress}`\n*К оплате:* `{float(rubinbnb) * num}` *₽*\n*Реквизиты для оплаты:* `{config.walletBNB}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormBuyBNB.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormBuyBNB.comfirm)
async def process_comfirmbuybnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Я оплатил(а)":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            adress = data['adress'] = message.text
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#P2P_\n\n📄 *Чек пользователя*\n\n*Он покупает:* `{data['number']}` *BNB*\n*Оплатил:* `{float(rubinbnb) * num}` *₽*\n*Ваши реквизиты оплаты:* `{config.card}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay bnb 0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = BNB TO RUB : SELL = = = = = = = #
@dp.callback_query_handler(text="call_p2psellbnb")
async def call_p2p_sellbnb(call: types.CallbackQuery):
    await FormSellBNB.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormSellBNB.number)
async def process_numbersellbnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
        else:
            for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
                data['number'] = message.text
                if float(data['number']) <= row[7]:
                    await FormSellBNB.next()
                    await message.answer("Введите карту на которую вы хотите перевести, ваши средства:",
                                         reply_markup=menuCancel)
                elif float(data['number']) > row[7]:
                    await state.finish()
                    await message.answer(
                        "На вашем балансе в боте, недостаточно средств, для выполнения данного действия",
                        reply_markup=st.mainMenu)


@dp.message_handler(state=FormSellBNB.adress)
async def process_adresssellbnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
        else:
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            adress = data['adress'] = message.text
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы продаёте:* `{data['number']}` *BNB*\nВаша карта: `{adress}`\n*К пополнению:* `{float(rubinbnb) * num}` *₽*\n\nПосле создания запроса не забудьте нажать кнопку «Я согласен(а)» и ожидайте одобрения Администратора")
            await FormSellBNB.next()
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm2)


@dp.message_handler(state=FormSellBNB.comfirm)
async def process_comfirmsellbnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Я согласен(а)":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#P2P_\n\n📄 *Чек пользователя*\n\n*Он продаёт:* `{data['number']}` *BNB*\n*Вы должны оплатить:* `{float(rubinbnb) * num}` *₽*\n*Карта пользователя:* `{adress}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay bnb -0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = CARDANO TO RUB : BUY = = = = = = = #
@dp.callback_query_handler(text="call_p2pbuycardano")
async def call_p2p_buycardano(call: types.CallbackQuery):
    await FormBuyCARDANO.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormBuyCARDANO.number)
async def process_numberbuycardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
        else:
            data['number'] = message.text
            await FormBuyCARDANO.next()
            await message.answer("Куда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormBuyCARDANO.type)
async def process_typebuycardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['type'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        if data['type'] == "На баланс бота 📲":
            user_id = message.from_user.id
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы покупаете:* `{data['number']}` *CARDANO*\n*К оплате:* `{float(rubincardano) * num}` *₽*\n*Реквизиты для оплаты:* `{config.card}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
            await FormBuyCARDANO.next()
            await FormBuyCARDANO.next()
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
        elif data['type'] == "На другой кошелёк 💸":
            await FormBuyCARDANO.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())
        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormBuyCARDANO.adress)
async def process_adressbuycardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        data['adress'] = message.text
        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы покупаете:* `{data['number']}` *CARDANO*\nЦелевой адресс: `{adress}`\n*К оплате:* `{float(rubincardano) * num}` *₽*\n*Реквизиты для оплаты:* `{config.walletCardano}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormBuyCARDANO.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormBuyCARDANO.comfirm)
async def process_comfirmbuycardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Я оплатил(а)":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            adress = data['adress'] = message.text
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#P2P_\n\n📄 *Чек пользователя*\n\n*Он покупает:* `{data['number']}` *CARDANO*\n*Оплатил:* `{float(rubincardano) * num}` *₽*\n*Ваши реквизиты оплаты:* `{config.card}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay cardano 0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = CARDANO TO RUB : SELL = = = = = = = #
@dp.callback_query_handler(text="call_p2psellcardano")
async def call_p2p_sellcardano(call: types.CallbackQuery):
    await FormSellCARDANO.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormSellCARDANO.number)
async def process_numbersellcardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
        else:
            for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
                data['number'] = message.text
                if float(data['number']) <= row[8]:
                    await FormSellCARDANO.next()
                    await message.answer("Введите карту на которую вы хотите перевести, ваши средства:",
                                         reply_markup=menuCancel)
                elif float(data['number']) > row[8]:
                    await state.finish()
                    await message.answer(
                        "На вашем балансе в боте, недостаточно средств, для выполнения данного действия",
                        reply_markup=st.mainMenu)


@dp.message_handler(state=FormSellCARDANO.adress)
async def process_adresssellcardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
        else:
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            adress = data['adress'] = message.text
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы продаёте:* `{data['number']}` *CARDANO*\nВаша карта: `{adress}`\n*К пополнению:* `{float(rubincardano) * num}` *₽*\n\nПосле создания запроса не забудьте нажать кнопку «Я согласен(а)» и ожидайте одобрения Администратора")
            await FormSellCARDANO.next()
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm2)


@dp.message_handler(state=FormSellCARDANO.comfirm)
async def process_comfirmsellcardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Я согласен(а)":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#P2P_\n\n📄 *Чек пользователя*\n\n*Он продаёт:* `{data['number']}` *CARDANO*\n*Вы должны оплатить:* `{float(rubincardano) * num}` *₽*\n*Карта пользователя:* `{adress}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay cardano -0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = TRON TO RUB : BUY = = = = = = = #
@dp.callback_query_handler(text="call_p2pbuytron")
async def call_p2p_buytron(call: types.CallbackQuery):
    await FormBuyTRON.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormBuyTRON.number)
async def process_numberbuytron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
        else:
            data['number'] = message.text
            await FormBuyTRON.next()
            await message.answer("Куда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormBuyTRON.type)
async def process_typebuytron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['type'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        if data['type'] == "На баланс бота 📲":
            user_id = message.from_user.id
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы покупаете:* `{data['number']}` *TRON*\n*К оплате:* `{float(rubintron) * num}` *₽*\n*Реквизиты для оплаты:* `{config.card}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
            await FormBuyTRON.next()
            await FormBuyTRON.next()
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
        elif data['type'] == "На другой кошелёк 💸":
            await FormBuyTRON.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())
        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormBuyTRON.adress)
async def process_adressbuytron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        data['adress'] = message.text
        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы покупаете:* `{data['number']}` *TRON*\nЦелевой адресс: `{adress}`\n*К оплате:* `{float(rubintron) * num}` *₽*\n*Реквизиты для оплаты:* `{config.walletTron}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormBuyTRON.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormBuyTRON.comfirm)
async def process_comfirmbuytron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Я оплатил(а)":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#P2P_\n\n📄 *Чек пользователя*\n\n*Он покупает:* `{data['number']}` *TRON*\n*Оплатил:* `{float(rubintron) * num}` *₽*\n*Ваши реквизиты оплаты:* `{config.card}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay tron 0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = TRON TO RUB : SELL = = = = = = = #
@dp.callback_query_handler(text="call_p2pselltron")
async def call_p2p_selltron(call: types.CallbackQuery):
    await FormSellTRON.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormSellTRON.number)
async def process_numberselltron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            data['number'] = message.text
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            else:
                if float(data['number']) <= row[9]:
                    await FormSellTRON.next()
                    await message.answer("Введите карту на которую вы хотите перевести, ваши средства:",
                                         reply_markup=types.ReplyKeyboardRemove())
                elif float(data['number']) > row[9]:
                    await state.finish()
                    await message.answer(
                        "На вашем балансе в боте, недостаточно средств, для выполнения данного действия",
                        reply_markup=st.mainMenu)


@dp.message_handler(state=FormSellTRON.adress)
async def process_adressselltron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        data['adress'] = message.text
        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы продаёте:* `{data['number']}` *TRON*\nВаша карта: `{adress}`\n*К пополнению:* `{float(rubintron) * num}` *₽*\n\nПосле создания запроса не забудьте нажать кнопку «Я согласен(а)» и ожидайте одобрения Администратора")
        await FormSellTRON.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm2)


@dp.message_handler(state=FormSellTRON.comfirm)
async def process_comfirmselltron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Я согласен(а)":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#P2P_\n\n📄 *Чек пользователя*\n\n*Он продаёт:* `{data['number']}` *TRON*\n*Вы должны оплатить:* `{float(rubintron) * num}` *₽*\n*Карта пользователя:* `{adress}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay tron -0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = BUSD TO RUB : BUY = = = = = = = #
@dp.callback_query_handler(text="call_p2pbuybusd")
async def call_p2p_buybusd(call: types.CallbackQuery):
    await FormBuyBUSD.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormBuyBUSD.number)
async def process_numberbuybusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
        else:
            data['number'] = message.text
            await FormBuyBUSD.next()
            await message.answer("Куда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormBuyBUSD.type)
async def process_typebuybusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['type'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        if data['type'] == "На баланс бота 📲":
            user_id = message.from_user.id
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы покупаете:* `{data['number']}` *BUSD*\n*К оплате:* `{float(rubinbusd) * num}` *₽*\n*Реквизиты для оплаты:* `{config.card}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
            await FormBuyBUSD.next()
            await FormBuyBUSD.next()
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
        elif data['type'] == "На другой кошелёк 💸":
            await FormBuyBUSD.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())
        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormBuyBUSD.adress)
async def process_adressbuybusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        data['adress'] = message.text
        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы покупаете:* `{data['number']}` *BUSD*\nЦелевой адресс: `{adress}`\n*К оплате:* `{float(rubinbusd) * num}` *₽*\n*Реквизиты для оплаты:* ERC-20 -`{config.walletBUSD_ERC20}`\nBEP-20 -`{config.walletBUSD_BEP20}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormBuyBUSD.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormBuyBUSD.comfirm)
async def process_comfirmbuybusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Я оплатил(а)":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            adress = data['adress'] = message.text
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#P2P_\n\n📄 *Чек пользователя*\n\n*Он покупает:* `{data['number']}` *BUSD*\n*Оплатил:* `{float(rubinbusd) * num}` *₽*\n*Ваши реквизиты оплаты:* `{config.card}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay busd 0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = BUSD TO RUB : SELL = = = = = = = #
@dp.callback_query_handler(text="call_p2psellbusd")
async def call_p2p_sellbusd(call: types.CallbackQuery):
    await FormSellBUSD.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormSellBUSD.number)
async def process_numbersellbusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
        else:
            for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
                data['number'] = message.text
                if float(data['number']) <= row[10]:
                    await FormSellUSDT.next()
                    await message.answer("Введите карту на которую вы хотите перевести, ваши средства:",
                                         reply_markup=menuCancel)
                elif float(data['number']) > row[10]:
                    await state.finish()
                    await message.answer(
                        "На вашем балансе в боте, недостаточно средств, для выполнения данного действия",
                        reply_markup=st.mainMenu)


@dp.message_handler(state=FormSellBUSD.adress)
async def process_adresssellbusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
        else:
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            adress = data['adress'] = message.text
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы продаёте:* `{data['number']}` *BUSD*\nВаша карта: `{adress}`\n*К пополнению:* `{float(rubinbusd) * num}` *₽*\n\nПосле создания запроса не забудьте нажать кнопку «Я согласен(а)» и ожидайте одобрения Администратора")
            await FormSellBUSD.next()
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm2)


@dp.message_handler(state=FormSellBUSD.comfirm)
async def process_comfirmsellbusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Я согласен(а)":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#P2P_\n\n📄 *Чек пользователя*\n\n*Он продаёт:* `{data['number']}` *BUSD*\n*Вы должны оплатить:* `{float(rubinbusd) * num}` *₽*\n*Карта пользователя:* `{adress}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay busd -0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = POLKADOT TO RUB : BUY = = = = = = = #
@dp.callback_query_handler(text="call_p2pbuypolkadot")
async def call_p2p_buypolkadot(call: types.CallbackQuery):
    await FormBuyPOLKADOT.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormBuyPOLKADOT.number)
async def process_numberbuypolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
        else:
            data['number'] = message.text
            await FormBuyPOLKADOT.next()
            await message.answer("Куда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormBuyPOLKADOT.type)
async def process_typebuypolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['type'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        if data['type'] == "На баланс бота 📲":
            user_id = message.from_user.id
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы покупаете:* `{data['number']}` *POLKADOT*\n*К оплате:* `{float(rubinbtc) * num}` *₽*\n*Реквизиты для оплаты:* `{config.card}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
            await FormBuyPOLKADOT.next()
            await FormBuyPOLKADOT.next()
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
        elif data['type'] == "На другой кошелёк 💸":
            await FormBuyPOLKADOT.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())
        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormBuyPOLKADOT.adress)
async def process_adressbuypolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        data['adress'] = message.text
        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы покупаете:* `{data['number']}` *POLKADOT*\nЦелевой адресс: `{adress}`\n*К оплате:* `{float(rubinpolkadot) * num}` *₽*\n*Реквизиты для оплаты:* `{config.walletPolkadot}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormBuyPOLKADOT.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormBuyPOLKADOT.comfirm)
async def process_comfirmbuypolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Я оплатил(а)":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#P2P_\n\n📄 *Чек пользователя*\n\n*Он покупает:* `{data['number']}` *POLKADOT*\n*Оплатил:* `{float(rubinpolkadot) * num}` *₽*\n*Ваши реквизиты оплаты:* `{config.card}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay polkadot 0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = POLKADOT TO RUB : SELL = = = = = = = #
@dp.callback_query_handler(text="call_p2psellpolkadot")
async def call_p2p_sellpolkadot(call: types.CallbackQuery):
    await FormSellPOLKADOT.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormSellPOLKADOT.number)
async def process_numbersellpolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            data['number'] = message.text
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            else:
                if float(data['number']) <= row[11]:
                    await FormSellPOLKADOT.next()
                    await message.answer("Введите карту на которую вы хотите перевести, ваши средства:",
                                         reply_markup=types.ReplyKeyboardRemove())
                elif float(data['number']) > row[11]:
                    await state.finish()
                    await message.answer(
                        "На вашем балансе в боте, недостаточно средств, для выполнения данного действия",
                        reply_markup=st.mainMenu)


@dp.message_handler(state=FormSellPOLKADOT.adress)
async def process_adresssellpolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        data['adress'] = message.text
        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы продаёте:* `{data['number']}` *POLKADOT*\nВаша карта: `{adress}`\n*К пополнению:* `{float(rubinpolkadot) * num}` *₽*\n\nПосле создания запроса не забудьте нажать кнопку «Я согласен(а)» и ожидайте одобрения Администратора")
        await FormSellPOLKADOT.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm2)


@dp.message_handler(state=FormSellPOLKADOT.comfirm)
async def process_comfirmsellpolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Я согласен(а)":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#P2P_\n\n📄 *Чек пользователя*\n\n*Он продаёт:* `{data['number']}` *POLKADOT*\n*Вы должны оплатить:* `{float(rubinpolkadot) * num}` *₽*\n*Карта пользователя:* `{adress}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay polkadot -0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = MATIC TO RUB : BUY = = = = = = = #
@dp.callback_query_handler(text="call_p2pbuymatic")
async def call_p2p_buymatic(call: types.CallbackQuery):
    await FormBuyMATIC.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormBuyMATIC.number)
async def process_numberbuymatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
        else:
            data['number'] = message.text
            await FormBuyMATIC.next()
            await message.answer("Куда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormBuyMATIC.type)
async def process_typebuymatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['type'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        if data['type'] == "На баланс бота 📲":
            user_id = message.from_user.id
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы покупаете:* `{data['number']}` *MATIC*\n*К оплате:* `{float(rubinmatic) * num}` *₽*\n*Реквизиты для оплаты:* `{config.card}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
            await FormBuyMATIC.next()
            await FormBuyMATIC.next()
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
        elif data['type'] == "На другой кошелёк 💸":
            await FormBuyMATIC.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())
        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormBuyMATIC.adress)
async def process_adressbuymatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        data['adress'] = message.text
        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы покупаете:* `{data['number']}` *MATIC*\nЦелевой адресс: `{adress}`\n*К оплате:* `{float(rubinmatic) * num}` *₽*\n*Реквизиты для оплаты:* `{config.walletMatic}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormBuyMATIC.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormBuyMATIC.comfirm)
async def process_comfirmbuymatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Я оплатил(а)":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#P2P_\n\n📄 *Чек пользователя*\n\n*Он покупает:* `{data['number']}` *MATIC*\n*Оплатил:* `{float(rubinmatic) * num}` *₽*\n*Ваши реквизиты оплаты:* `{config.card}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay matic 0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = MATIC TO RUB : SELL = = = = = = = #
@dp.callback_query_handler(text="call_p2psellmatic")
async def call_p2p_sellmatic(call: types.CallbackQuery):
    await FormSellMATIC.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormSellMATIC.number)
async def process_numbersellmatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            data['number'] = message.text
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            else:
                if float(data['number']) <= row[12]:
                    await FormSellMATIC.next()
                    await message.answer("Введите карту на которую вы хотите перевести, ваши средства:",
                                         reply_markup=types.ReplyKeyboardRemove())
                elif float(data['number']) > row[12]:
                    await state.finish()
                    await message.answer(
                        "На вашем балансе в боте, недостаточно средств, для выполнения данного действия",
                        reply_markup=st.mainMenu)


@dp.message_handler(state=FormSellMATIC.adress)
async def process_adresssellmatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        data['adress'] = message.text
        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы продаёте:* `{data['number']}` *MATIC*\nВаша карта: `{adress}`\n*К пополнению:* `{float(rubinmatic) * num}` *₽*\n\nПосле создания запроса не забудьте нажать кнопку «Я согласен(а)» и ожидайте одобрения Администратора")
        await FormSellMATIC.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm2)


@dp.message_handler(state=FormSellMATIC.comfirm)
async def process_comfirmsellmatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Я согласен(а)":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#P2P_\n\n📄 *Чек пользователя*\n\n*Он продаёт:* `{data['number']}` *MATIC*\n*Вы должны оплатить:* `{float(rubinmatic) * num}` *₽*\n*Карта пользователя:* `{adress}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay matic -0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = CWD TO RUB : BUY = = = = = = = #
@dp.callback_query_handler(text="call_p2pbuycwd")
async def call_p2p_buycwd(call: types.CallbackQuery):
    await FormBuyCWD.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormBuyCWD.number)
async def process_numberbuycwd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
        else:
            data['number'] = message.text
            await FormBuyCWD.next()
            await message.answer("Куда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormBuyCWD.type)
async def process_typebuycwd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['type'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        if data['type'] == "На баланс бота 📲":
            user_id = message.from_user.id
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы покупаете:* `{data['number']}` *CWD*\n*К оплате:* `{1 * num}` *₽*\n*Реквизиты для оплаты:* `{config.card}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
            await FormBuyCWD.next()
            await FormBuyCWD.next()
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
        elif data['type'] == "На другой кошелёк 💸":
            await FormBuyCWD.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())
        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormBuyCWD.adress)
async def process_adressbuycwd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        data['adress'] = message.text
        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы покупаете:* `{data['number']}` *CWD*\nЦелевой адресс: `{adress}`\n*К оплате:* `{1 * num}` *₽*\n*Реквизиты для оплаты:* `{config.walletCWD}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormBuyCWD.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormBuyCWD.comfirm)
async def process_comfirmbuycwd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Я оплатил(а)":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#P2P_\n\n📄 *Чек пользователя*\n\n*Он покупает:* `{data['number']}` *CWD*\n*Оплатил:* `{1 * num}` *₽*\n*Ваши реквизиты оплаты:* `{config.card}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay cwd 0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = CWD TO RUB : SELL = = = = = = = #
@dp.callback_query_handler(text="call_p2psellcwd")
async def call_p2p_sellcwd(call: types.CallbackQuery):
    await FormSellCWD.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormSellCWD.number)
async def process_numbersellcwd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            data['number'] = message.text
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            else:
                if float(data['number']) <= row[13]:
                    await FormSellCWD.next()
                    await message.answer("Введите карту на которую вы хотите перевести, ваши средства:",
                                         reply_markup=types.ReplyKeyboardRemove())
                elif float(data['number']) > row[13]:
                    await state.finish()
                    await message.answer(
                        "На вашем балансе в боте, недостаточно средств, для выполнения данного действия",
                        reply_markup=st.mainMenu)


@dp.message_handler(state=FormSellCWD.adress)
async def process_adresssellcwd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        data['adress'] = message.text
        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы продаёте:* `{data['number']}` *CWD*\nВаша карта: `{adress}`\n*К пополнению:* `{1 * num}` *₽*\n\nПосле создания запроса не забудьте нажать кнопку «Я согласен(а)» и ожидайте одобрения Администратора")
        await FormSellCWD.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm2)


@dp.message_handler(state=FormSellCWD.comfirm)
async def process_comfirmsellcwd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Я согласен(а)":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#P2P_\n\n📄 *Чек пользователя*\n\n*Он продаёт:* `{data['number']}` *CWD*\n*Вы должны оплатить:* `{1 * num}` *₽*\n*Карта пользователя:* `{adress}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay cwd -0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = WATT TO RUB : BUY = = = = = = = #
@dp.callback_query_handler(text="call_p2pbuywatt")
async def call_p2p_buywatt(call: types.CallbackQuery):
    await FormBuyWATT.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormBuyWATT.number)
async def process_numberbuywatt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
        else:
            data['number'] = message.text
            await FormBuyWATT.next()
            await message.answer("Куда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormBuyWATT.type)
async def process_typebuywatt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['type'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        if data['type'] == "На баланс бота 📲":
            user_id = message.from_user.id
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы покупаете:* `{data['number']}` *WATT*\n*К оплате:* `{float(rubinwatt) * num}` *₽*\n*Реквизиты для оплаты:* `{config.card}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
            await FormBuyWATT.next()
            await FormBuyWATT.next()
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
        elif data['type'] == "На другой кошелёк 💸":
            await FormBuyWATT.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())
        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormBuyWATT.adress)
async def process_adressbuywatt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        data['adress'] = message.text
        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы покупаете:* `{data['number']}` *WATT*\nЦелевой адресс: `{adress}`\n*К оплате:* `{float(rubinwatt) * num}` *₽*\n*Реквизиты для оплаты:* `{config.walletWatt}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormBuyWATT.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormBuyWATT.comfirm)
async def process_comfirmbuywatt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Я оплатил(а)":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#P2P_\n\n📄 *Чек пользователя*\n\n*Он покупает:* `{data['number']}` *WATT*\n*Оплатил:* `{float(rubinwatt) * num}` *₽*\n*Ваши реквизиты оплаты:* `{config.card}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay watt 0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = WATT TO RUB : SELL = = = = = = = #
@dp.callback_query_handler(text="call_p2psellwatt")
async def call_p2p_sellwatt(call: types.CallbackQuery):
    await FormSellWATT.number.set()
    await call.message.answer("Введите количество:", reply_markup=menuCancel)


@dp.message_handler(state=FormSellWATT.number)
async def process_numbersellwatt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            data['number'] = message.text
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            else:
                if float(data['number']) <= row[14]:
                    await FormSellWATT.next()
                    await message.answer("Введите карту на которую вы хотите перевести, ваши средства:",
                                         reply_markup=types.ReplyKeyboardRemove())
                elif float(data['number']) > row[14]:
                    await state.finish()
                    await message.answer(
                        "На вашем балансе в боте, недостаточно средств, для выполнения данного действия",
                        reply_markup=st.mainMenu)


@dp.message_handler(state=FormSellWATT.adress)
async def process_adresssellwatt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        data['adress'] = message.text
        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы продаёте:* `{data['number']}` *WATT*\nВаша карта: `{adress}`\n*К пополнению:* `{float(rubinwatt) * num}` *₽*\n\nПосле создания запроса не забудьте нажать кнопку «Я согласен(а)» и ожидайте одобрения Администратора")
        await FormSellWATT.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm2)


@dp.message_handler(state=FormSellWATT.comfirm)
async def process_comfirmsellwatt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Я согласен(а)":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            data['adress'] = message.text
            adress = data['adress']
            user_id = message.from_user.id
            await bot.send_message(config.admin_id,
                                   f"_#P2P_\n\n📄 *Чек пользователя*\n\n*Он продаёт:* `{data['number']}` *WATT*\n*Вы должны оплатить:* `{float(rubinwatt) * num}` *₽*\n*Карта пользователя:* `{adress}`\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay watt -0.1 {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = REGISTER HANDLERS = = = = = = = #
def register_handlers_p2pexchanger(dp: Dispatcher):
    # = = = = = = P2P ACTIVE  = = = = = = #
    dp.register_message_handler(val_cancel, lambda msg: msg.text.startswith("Отмена 🔴"))
    dp.register_message_handler(val_p2p_exchanger, lambda msg: msg.text.startswith('P2P обменник💸'))

    # = = = = = P2P MENU : ALL CRYPTOCURRENCY = = = = = #
    dp.register_callback_query_handler(call_p2p_p2pbitcoin, text="call_p2pbitcoin")
    dp.register_callback_query_handler(call_p2p_p2pethereum, text="call_p2pethereum")
    dp.register_callback_query_handler(call_p2p_p2psolana, text="call_p2psolana")
    dp.register_callback_query_handler(call_p2p_p2pusdt, text="call_p2pusdt")
    dp.register_callback_query_handler(call_p2p_p2pbnb, text="call_p2pbnb")
    dp.register_callback_query_handler(call_p2p_p2pcardano, text="call_p2pcardano")
    dp.register_callback_query_handler(call_p2p_p2ptron, text="call_p2ptron")
    dp.register_callback_query_handler(call_p2p_p2pbusd, text="call_p2pbusd")
    dp.register_callback_query_handler(call_p2p_p2ppolkadot, text="call_p2ppolkadot")
    dp.register_callback_query_handler(call_p2p_p2pmatic, text="call_p2pmatic")
    dp.register_callback_query_handler(call_p2p_p2pcwd, text="call_p2pcwd")
    dp.register_callback_query_handler(call_p2p_p2pwatt, text="call_p2pwatt")

    # = = = = P2P BITCOIN MENU : BUY = = = = #
    dp.register_callback_query_handler(call_p2p_buybitcoin, text="call_p2pbuybtc")
    dp.register_message_handler(process_numberbuybtc, state=FormBuyBTC.number)
    dp.register_message_handler(process_typebuybtc, state=FormBuyBTC.type)
    dp.register_message_handler(process_adressbuybtc, state=FormBuyBTC.adress)
    dp.register_message_handler(process_comfirmbuybtc, state=FormBuyBTC.comfirm)

    # = = = = P2P BITCOIN MENU : SELL = = = = #
    dp.register_callback_query_handler(call_p2p_sellbitcoin, text="call_p2psellbtc")
    dp.register_message_handler(process_numbersellbtc, state=FormSellBTC.number)
    dp.register_message_handler(process_adresssellbtc, state=FormSellBTC.adress)
    dp.register_message_handler(process_comfirmsellbtc, state=FormSellBTC.comfirm)

    # = = = = P2P ETHREUM MENU : BUY = = = = #
    dp.register_callback_query_handler(call_p2p_buyethreum, text="call_p2pbuyeth")
    dp.register_message_handler(process_numberbuyeth, state=FormBuyETH.number)
    dp.register_message_handler(process_typebuyeth, state=FormBuyETH.type)
    dp.register_message_handler(process_adressbuyeth, state=FormBuyETH.adress)
    dp.register_message_handler(process_comfirmbuyeth, state=FormBuyETH.comfirm)

    # = = = = P2P ETHREUM MENU : SELL = = = = #
    dp.register_callback_query_handler(call_p2p_sellethereum, text="call_p2pselleth")
    dp.register_message_handler(process_numberselleth, state=FormSellETH.number)
    dp.register_message_handler(process_adressselleth, state=FormSellETH.adress)
    dp.register_message_handler(process_comfirmselleth, state=FormSellETH.comfirm)

    # = = = = P2P SOLANA MENU : BUY = = = = #
    dp.register_callback_query_handler(call_p2p_buysolana, text="call_p2pbuysol")
    dp.register_message_handler(process_numberbuysol, state=FormBuySOL.number)
    dp.register_message_handler(process_typebuysol, state=FormBuySOL.type)
    dp.register_message_handler(process_adressbuysol, state=FormBuySOL.adress)
    dp.register_message_handler(process_comfirmbuysol, state=FormBuySOL.comfirm)

    # = = = = P2P SOLANA MENU : SELL = = = = #
    dp.register_callback_query_handler(call_p2p_sellsolana, text="call_p2psellsol")
    dp.register_message_handler(process_numbersellsol, state=FormSellSOL.number)
    dp.register_message_handler(process_adresssellsol, state=FormSellSOL.adress)
    dp.register_message_handler(process_comfirmsellsol, state=FormSellSOL.comfirm)

    # = = = = P2P USDT MENU : BUY = = = = #
    dp.register_callback_query_handler(call_p2p_buyusdt, text="call_p2pbuyusdt")
    dp.register_message_handler(process_numberbuyusdt, state=FormBuyUSDT.number)
    dp.register_message_handler(process_typebuyusdt, state=FormBuyUSDT.type)
    dp.register_message_handler(process_adressbuyusdt, state=FormBuyUSDT.adress)
    dp.register_message_handler(process_comfirmbuyusdt, state=FormBuyUSDT.comfirm)

    # = = = = P2P USDT MENU : SELL = = = = #
    dp.register_callback_query_handler(call_p2p_sellusdt, text="call_p2psellusdt")
    dp.register_message_handler(process_numbersellusdt, state=FormSellUSDT.number)
    dp.register_message_handler(process_adresssellusdt, state=FormSellUSDT.adress)
    dp.register_message_handler(process_comfirmsellusdt, state=FormSellUSDT.comfirm)

    # = = = = P2P BNB MENU : BUY = = = = #
    dp.register_callback_query_handler(call_p2p_buybnb, text="call_p2pbuybnb")
    dp.register_message_handler(process_numberbuybnb, state=FormBuyBNB.number)
    dp.register_message_handler(process_typebuybnb, state=FormBuyBNB.type)
    dp.register_message_handler(process_adressbuybnb, state=FormBuyBNB.adress)
    dp.register_message_handler(process_comfirmbuybnb, state=FormBuyBNB.comfirm)

    # = = = = P2P BNB MENU : SELL = = = = #
    dp.register_callback_query_handler(call_p2p_sellbnb, text="call_p2psellbnb")
    dp.register_message_handler(process_numbersellbnb, state=FormSellBNB.number)
    dp.register_message_handler(process_adresssellbnb, state=FormSellBNB.adress)
    dp.register_message_handler(process_comfirmsellbnb, state=FormSellBNB.comfirm)

    # = = = = P2P CARDANO MENU : BUY = = = = #
    dp.register_callback_query_handler(call_p2p_buycardano, text="call_p2pbuycardano")
    dp.register_message_handler(process_numberbuycardano, state=FormBuyCARDANO.number)
    dp.register_message_handler(process_typebuycardano, state=FormBuyCARDANO.type)
    dp.register_message_handler(process_adressbuycardano, state=FormBuyCARDANO.adress)
    dp.register_message_handler(process_comfirmbuycardano, state=FormBuyCARDANO.comfirm)

    # = = = = P2P CARDANO MENU : SELL = = = = #
    dp.register_callback_query_handler(call_p2p_sellcardano, text="call_p2psellcardano")
    dp.register_message_handler(process_numbersellcardano, state=FormSellCARDANO.number)
    dp.register_message_handler(process_adresssellcardano, state=FormSellCARDANO.adress)
    dp.register_message_handler(process_comfirmsellcardano, state=FormSellCARDANO.comfirm)

    # = = = = P2P TRON MENU : BUY = = = = #
    dp.register_callback_query_handler(call_p2p_buytron, text="call_p2pbuytron")
    dp.register_message_handler(process_numberbuytron, state=FormBuyTRON.number)
    dp.register_message_handler(process_typebuytron, state=FormBuyTRON.type)
    dp.register_message_handler(process_adressbuytron, state=FormBuyTRON.adress)
    dp.register_message_handler(process_comfirmbuytron, state=FormBuyTRON.comfirm)

    # = = = = P2P TRON MENU : SELL = = = = #
    dp.register_callback_query_handler(call_p2p_selltron, text="call_p2pselltron")
    dp.register_message_handler(process_numberselltron, state=FormSellTRON.number)
    dp.register_message_handler(process_adressselltron, state=FormSellTRON.adress)
    dp.register_message_handler(process_comfirmselltron, state=FormSellTRON.comfirm)

    # = = = = P2P BUSD MENU : BUY = = = = #
    dp.register_callback_query_handler(call_p2p_buybusd, text="call_p2pbuybusd")
    dp.register_message_handler(process_numberbuybusd, state=FormBuyBUSD.number)
    dp.register_message_handler(process_typebuybusd, state=FormBuyBUSD.type)
    dp.register_message_handler(process_adressbuybusd, state=FormBuyBUSD.adress)
    dp.register_message_handler(process_comfirmbuybusd, state=FormBuyBUSD.comfirm)

    # = = = = P2P BUSD MENU : SELL = = = = #
    dp.register_callback_query_handler(call_p2p_sellbusd, text="call_p2psellbusd")
    dp.register_message_handler(process_numbersellbusd, state=FormSellBUSD.number)
    dp.register_message_handler(process_adresssellbusd, state=FormSellBUSD.adress)
    dp.register_message_handler(process_comfirmsellbusd, state=FormSellBUSD.comfirm)

    # = = = = P2P POLKADOT MENU : BUY = = = = #
    dp.register_callback_query_handler(call_p2p_buypolkadot, text="call_p2pbuypolkadot")
    dp.register_message_handler(process_numberbuypolkadot, state=FormBuyPOLKADOT.number)
    dp.register_message_handler(process_typebuypolkadot, state=FormBuyPOLKADOT.type)
    dp.register_message_handler(process_adressbuypolkadot, state=FormBuyPOLKADOT.adress)
    dp.register_message_handler(process_comfirmbuypolkadot, state=FormBuyPOLKADOT.comfirm)

    # = = = = P2P POLKADOT MENU : SELL = = = = #
    dp.register_callback_query_handler(call_p2p_sellpolkadot, text="call_p2psellpolkadot")
    dp.register_message_handler(process_numbersellpolkadot, state=FormSellPOLKADOT.number)
    dp.register_message_handler(process_adresssellpolkadot, state=FormSellPOLKADOT.adress)
    dp.register_message_handler(process_comfirmsellpolkadot, state=FormSellPOLKADOT.comfirm)

    # = = = = P2P MATIC MENU : BUY = = = = #
    dp.register_callback_query_handler(call_p2p_buymatic, text="call_p2pbuymatic")
    dp.register_message_handler(process_numberbuymatic, state=FormBuyMATIC.number)
    dp.register_message_handler(process_typebuymatic, state=FormBuyMATIC.type)
    dp.register_message_handler(process_adressbuymatic, state=FormBuyMATIC.adress)
    dp.register_message_handler(process_comfirmbuymatic, state=FormBuyMATIC.comfirm)

    # = = = = P2P MATIC MENU : SELL = = = = #
    dp.register_callback_query_handler(call_p2p_sellmatic, text="call_p2psellmatic")
    dp.register_message_handler(process_numbersellmatic, state=FormSellMATIC.number)
    dp.register_message_handler(process_adresssellmatic, state=FormSellMATIC.adress)
    dp.register_message_handler(process_comfirmsellmatic, state=FormSellMATIC.comfirm)

    # = = = = P2P CWD MENU : BUY = = = = #
    dp.register_callback_query_handler(call_p2p_buycwd, text="call_p2pbuycwd")
    dp.register_message_handler(process_numberbuycwd, state=FormBuyCWD.number)
    dp.register_message_handler(process_typebuycwd, state=FormBuyCWD.type)
    dp.register_message_handler(process_adressbuycwd, state=FormBuyCWD.adress)
    dp.register_message_handler(process_comfirmbuycwd, state=FormBuyCWD.comfirm)

    # = = = = P2P CWD MENU : SELL = = = = #
    dp.register_callback_query_handler(call_p2p_sellcwd, text="call_p2psellcwd")
    dp.register_message_handler(process_numbersellcwd, state=FormSellCWD.number)
    dp.register_message_handler(process_adresssellcwd, state=FormSellCWD.adress)
    dp.register_message_handler(process_comfirmsellcwd, state=FormSellCWD.comfirm)

    # = = = = P2P WATT MENU : BUY = = = = #
    dp.register_callback_query_handler(call_p2p_buywatt, text="call_p2pbuywatt")
    dp.register_message_handler(process_numberbuywatt, state=FormBuyWATT.number)
    dp.register_message_handler(process_typebuywatt, state=FormBuyWATT.type)
    dp.register_message_handler(process_adressbuywatt, state=FormBuyWATT.adress)
    dp.register_message_handler(process_comfirmbuywatt, state=FormBuyWATT.comfirm)

    # = = = = P2P WATT MENU : SELL = = = = #
    dp.register_callback_query_handler(call_p2p_sellwatt, text="call_p2psellwatt")
    dp.register_message_handler(process_numbersellwatt, state=FormSellWATT.number)
    dp.register_message_handler(process_adresssellwatt, state=FormSellWATT.adress)
    dp.register_message_handler(process_comfirmsellwatt, state=FormSellWATT.comfirm)
