# -*- coding: utf-8 -*-
# = = = = = = = IMPORTS = = = = = = = #
from aiogram import Dispatcher, Bot, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import config
from handlers import start_place as st
from handlers import db
from handlers import p2p_exchanger as ex

from bs4 import BeautifulSoup
import requests

bot = Bot(token=config.token, parse_mode=config.parse_mode)
dp = Dispatcher(bot)

# = = = = = = = USER AGENT = = = = = = = #
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

# = = = = = = = RUB.TO.BTC CONVERT : STATES = = = = = = = #
BTCINRUB = 0.00000070

# = = = = = = = RUB.TO.ETH CONVERT : STATES = = = = = = = #
RUB_ETH = 'https://www.google.com/search?q=%D1%80%D1%83%D0%B1+%D0%BA+%D0%B5%D1%84%D0%B8%D1%80&ei=TXXiYv2oN4PQqwGd9KKwCw&ved=0ahUKEwi9g7DTv5v5AhUD6CoKHR26CLYQ4dUDCA4&uact=5&oq=%D1%80%D1%83%D0%B1+%D0%BA+%D0%B5%D1%84%D0%B8%D1%80&gs_lcp=Cgdnd3Mtd2l6EAMyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoKCAAQsQMQgwEQQzoECC4QQzoLCAAQgAQQsQMQgwE6CAguEIAEELEDOg4ILhCABBCxAxCDARDUAjoHCAAQsQMQQ0oECEEYAEoECEYYAFAAWJIaYOUcaABwAXgAgAHzCogB2S-SAQU2LTEuNJgBAKABAcABAQ&sclient=gws-wiz'

full_page = requests.get(
    RUB_ETH,
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
ETHINRUB = ethrub.replace(",", ".")

# = = = = = = = RUB.TO.SOL CONVERT : STATES = = = = = = = #
RUB_SOL = 'https://valuta.exchange/ru/rub-to-sol'

full_page = requests.get(
    RUB_SOL,
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
SOLINRUB = solrub.replace(",", ".")

# = = = = = = = RUB.TO.USDT CONVERT : STATES = = = = = = = #
RUB_USDT = 'https://www.google.com/search?q=rub+usdt&ei=q4_iYu7vJ62FwPAPg6K-8AM&ved=0ahUKEwiu8fPl2Jv5AhWtAhAIHQORDz4Q4dUDCA4&uact=5&oq=rub+usdt&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgYIABAeEBYyCAgAEB4QFhAKMgYIABAeEBYyCAgAEB4QFhAKMgYIABAeEBYyCAgAEB4QFhAKOhAILhCxAxCDARDHARDRAxBDOgoILhDHARDRAxBDOgsILhCABBDHARCvAToICAAQsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOhEILhCABBCxAxDHARDRAxDUAjoLCAAQgAQQsQMQgwE6CQgAEIAEEAoQAToICAAQgAQQsQM6CQguEIAEEAoQAToFCC4QgAQ6BAgAEA06BggAEB4QDToICAAQHhAIEA06CQgAEA0QRhCCAkoECEEYAEoECEYYAFAAWK81YL04aANwAXgAgAHZBYgByTGSAQkzLTMuMi41LjKYAQCgAQGgAQLAAQE&sclient=gws-wiz'

full_page = requests.get(
    RUB_USDT,
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
USDTINRUB = usdtrub.replace(",", ".")

# = = = = = = = RUB.TO.BNB CONVERT : STATES = = = = = = = #
RUB_BNB = 'https://www.google.com/search?q=rub+BNB&ei=m5HiYtr5MvL6qwHyzp6IBQ&ved=0ahUKEwias8DS2pv5AhVy_SoKHXKnB1EQ4dUDCA4&uact=5&oq=rub+BNB&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgUIABCABDIFCAAQgAQyBAgAEEMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6CggAELEDEIMBEEM6CwgAEIAEELEDEIMBOggIABCABBCxAzoPCAAQsQMQgwEQQxBGEIICSgQIQRgASgQIRhgAUABY6Q1gpg9oAHABeACAAYsCiAGiBpIBBTAuMS4zmAEAoAEBwAEB&sclient=gws-wiz'

full_page = requests.get(
    RUB_BNB,
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
BNBINRUB = bnbrub.replace(",", ".")

# = = = = = = = RUB.TO.CARDANO CONVERT : STATES = = = = = = = #
RUB_CARDANO = 'https://www.google.com/search?q=rub+cardano+&ei=mpPiYsvCGOqjrgSbs7b4AQ&ved=0ahUKEwjL9_rF3Jv5AhXqkYsKHZuZDR8Q4dUDCA4&uact=5&oq=rub+cardano+&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEB4QFjoHCAAQsQMQQzoECAAQQzoKCAAQsQMQgwEQQzoLCAAQgAQQsQMQgwE6CAgAEIAEELEDOgUIABCABDoLCC4QgAQQsQMQgwFKBAhBGABKBAhGGABQAFjrCWC3F2gAcAF4AIAB-wKIAf8HkgEHMC4yLjAuMpgBAKABAaABAsABAQ&sclient=gws-wiz'

full_page = requests.get(
    RUB_CARDANO,
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
CARDANOINRUB = cardanorub.replace(",", ".")

# = = = = = = = RUB.TO.TRON CONVERT : STATES = = = = = = = #
RUB_TRON = 'https://www.google.com/search?q=RUB+TO+TRON&ei=-5XiYq_JB9jQqwG29YagBA&ved=0ahUKEwjvspzo3pv5AhVY6CoKHba6AUQQ4dUDCA4&uact=5&oq=RUB+TO+TRON&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMggIABAeEA8QFjIKCAAQHhAPEBYQCjoKCAAQsQMQgwEQQzoECAAQQzoHCAAQsQMQQzoLCAAQgAQQsQMQgwE6CAgAEIAEELEDOg8IABCxAxCDARBDEEYQggI6BggAEB4QFjoICAAQHhAWEApKBAhBGABKBAhGGABQAFjJGWDHG2gAcAF4AIABvwKIAdASkgEHMC40LjMuM5gBAKABAcABAQ&sclient=gws-wiz'

full_page = requests.get(
    RUB_TRON,
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
TRONINRUB = tronrub.replace(",", ".")

# = = = = = = = RUB.TO.BUSD CONVERT : STATES = = = = = = = #
RUB_BUSD = 'https://www.google.com/search?q=rub+usdt&ei=q4_iYu7vJ62FwPAPg6K-8AM&ved=0ahUKEwiu8fPl2Jv5AhWtAhAIHQORDz4Q4dUDCA4&uact=5&oq=rub+usdt&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgYIABAeEBYyCAgAEB4QFhAKMgYIABAeEBYyCAgAEB4QFhAKMgYIABAeEBYyCAgAEB4QFhAKOhAILhCxAxCDARDHARDRAxBDOgoILhDHARDRAxBDOgsILhCABBDHARCvAToICAAQsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOhEILhCABBCxAxDHARDRAxDUAjoLCAAQgAQQsQMQgwE6CQgAEIAEEAoQAToICAAQgAQQsQM6CQguEIAEEAoQAToFCC4QgAQ6BAgAEA06BggAEB4QDToICAAQHhAIEA06CQgAEA0QRhCCAkoECEEYAEoECEYYAFAAWK81YL04aANwAXgAgAHZBYgByTGSAQkzLTMuMi41LjKYAQCgAQGgAQLAAQE&sclient=gws-wiz'

full_page = requests.get(
    RUB_BUSD,
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
BUSDINRUB = busdrub.replace(",", ".")

# = = = = = = = RUB.TO.POLKADOT CONVERT : STATES = = = = = = = #
RUB_POLKADOT = 'https://valuta.exchange/ru/rub-to-dot'

full_page = requests.get(
    RUB_POLKADOT,
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
POLKADOTINRUB = polkadotrub.replace(",", ".")

# = = = = = = = RUB.TO.MATIC CONVERT : STATES = = = = = = = #
RUB_MATIC = 'https://walletinvestor.com/converter/rub/polygon/1'

full_page = requests.get(
    RUB_MATIC,
    headers=headers
)
soup = BeautifulSoup(
    full_page.content,
    'html.parser'
)
convert = soup.findAll(
    "span", {
        "class": "converter-title-amount"
    }
)

matictorub = convert[0].text
maticrub = matictorub.split()
maticrub = ''.join(maticrub)
MATICINRUB = maticrub.replace(",", ".")


# = = = = = = = FSM.STATES : CRS.BTC = = = = = = = #
class FormCRSBTCtoETH(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSBTCtoSOL(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSBTCtoUSDT(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSBTCtoBNB(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSBTCtoCARDANO(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSBTCtoTRON(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSBTCtoBUSD(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSBTCtoPOLKADOT(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSBTCtoMATIC(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


# = = = = = = = FSM.STATES : CRS.ETH = = = = = = = #
class FormCRSETHtoBTC(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSETHtoSOL(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSETHtoUSDT(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSETHtoBNB(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSETHtoCARDANO(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSETHtoTRON(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSETHtoBUSD(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSETHtoPOLKADOT(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSETHtoMATIC(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


# = = = = = = = FSM.STATES : CRS.SOL = = = = = = = #
class FormCRSSOLtoBTC(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSSOLtoETH(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSSOLtoUSDT(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSSOLtoBNB(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSSOLtoCARDANO(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSSOLtoTRON(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSSOLtoBUSD(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSSOLtoPOLKADOT(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSSOLtoMATIC(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


# = = = = = = = FSM.STATES : CRS.USDT = = = = = = = #
class FormCRSUSDTtoBTC(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSUSDTtoETH(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSUSDTtoSOL(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSUSDTtoBNB(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSUSDTtoCARDANO(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSUSDTtoTRON(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSUSDTtoBUSD(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSUSDTtoPOLKADOT(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSUSDTtoMATIC(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


# = = = = = = = FSM.STATES : CRS.BNB = = = = = = = #
class FormCRSBNBtoBTC(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSBNBtoETH(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSBNBtoSOL(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSBNBtoUSDT(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSBNBtoCARDANO(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSBNBtoTRON(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSBNBtoBUSD(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSBNBtoPOLKADOT(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSBNBtoMATIC(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


# = = = = = = = FSM.STATES : CRS.CARDANO = = = = = = = #
class FormCRSCARDANOtoBTC(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSCARDANOtoETH(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSCARDANOtoSOL(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSCARDANOtoUSDT(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSCARDANOtoBNB(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSCARDANOtoTRON(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSCARDANOtoBUSD(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSCARDANOtoPOLKADOT(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSCARDANOtoMATIC(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


# = = = = = = = FSM.STATES : CRS.TRON = = = = = = = #
class FormCRSTRONtoBTC(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSTRONtoETH(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSTRONtoSOL(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSTRONtoUSDT(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSTRONtoBNB(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSTRONtoCARDANO(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSTRONtoBUSD(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSTRONtoPOLKADOT(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSTRONtoMATIC(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


# = = = = = = = FSM.STATES : CRS.BUSD = = = = = = = #
class FormCRSBUSDtoBTC(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSBUSDtoETH(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSBUSDtoSOL(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSBUSDtoUSDT(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSBUSDtoBNB(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSBUSDtoCARDANO(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSBUSDtoTRON(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSBUSDtoPOLKADOT(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSBUSDtoMATIC(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


# = = = = = = = FSM.STATES : CRS.POLKADOT = = = = = = = #
class FormCRSPOLKADOTtoBTC(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSPOLKADOTtoETH(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSPOLKADOTtoSOL(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSPOLKADOTtoUSDT(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSPOLKADOTtoBNB(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSPOLKADOTtoCARDANO(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSPOLKADOTtoTRON(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSPOLKADOTtoBUSD(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSPOLKADOTtoMATIC(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


# = = = = = = = FSM.STATES : CRS.MATIC = = = = = = = #
class FormCRSMATICtoBTC(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSMATICtoETH(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSMATICtoSOL(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSMATICtoUSDT(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSMATICtoBNB(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSMATICtoCARDANO(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSMATICtoTRON(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSMATICtoBUSD(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


class FormCRSMATICtoPOLKADOT(StatesGroup):
    number = State()
    type = State()
    adress = State()
    comfirm = State()


# = = = = = = = CRS STABLE CALLBACK.QUERY BUTTONS : FROM = = = = = = = #
btncrs_frBitcoin = InlineKeyboardButton("Bitcoin", callback_data="call_frcrsbitcoin")
btncrs_frEthereum = InlineKeyboardButton("Ethereum", callback_data="call_frcrsethereum")
btncrs_frSolana = InlineKeyboardButton("Solana", callback_data="call_frcrssolana")
btncrs_frUSDT = InlineKeyboardButton("USDT", callback_data="call_frcrsusdt")
btncrs_frBNB = InlineKeyboardButton("BNB", callback_data="call_frcrsbnb")
btncrs_frCardano = InlineKeyboardButton("Cardano", callback_data="call_frcrscardano")
btncrs_frTron = InlineKeyboardButton("Tron", callback_data="call_frcrstron")
btncrs_frBUSD = InlineKeyboardButton("BUSD", callback_data="call_frcrsbusd")
btncrs_frPolkadot = InlineKeyboardButton("Polkadot", callback_data="call_frcrspolkadot")
btncrs_frMatic = InlineKeyboardButton("Matic", callback_data="call_frcrsmatic")

# = = = = = = = CRS BUTTONS : FROM BITCOIN = = = = = = = #
btncrs_toEthereumBTC = InlineKeyboardButton("Ethereum", callback_data="call_tocrsethereumBTC")
btncrs_toSolanaBTC = InlineKeyboardButton("Solana", callback_data="call_tocrssolBTC")
btncrs_toUSDTBTC = InlineKeyboardButton("USDT", callback_data="call_tocrsusdtBTC")
btncrs_toBNBBTC = InlineKeyboardButton("BNB", callback_data="call_tocrsbnbBTC")
btncrs_toCardanoBTC = InlineKeyboardButton("Cardano", callback_data="call_tocrscardanoBTC")
btncrs_toTronBTC = InlineKeyboardButton("Tron", callback_data="call_tocrstronBTC")
btncrs_toBUSDBTC = InlineKeyboardButton("BUSD", callback_data="call_tocrsbusdBTC")
btncrs_toPolkadotBTC = InlineKeyboardButton("Polkadot", callback_data="call_tocrspolkadotBTC")
btncrs_toMaticBTC = InlineKeyboardButton("Matic", callback_data="call_tocrsmaticBTC")

# = = = = = = = CRS BUTTONS : FROM ETHEREUM = = = = = = = #
btncrs_toBitcoinETH = InlineKeyboardButton("Bitcoin", callback_data="call_tocrsbitcoinETH")
btncrs_toSolanaETH = InlineKeyboardButton("Solana", callback_data="call_tocrssolETH")
btncrs_toUSDTETH = InlineKeyboardButton("USDT", callback_data="call_tocrsusdtETH")
btncrs_toBNBETH = InlineKeyboardButton("BNB", callback_data="call_tocrsbnbETH")
btncrs_toCardanoETH = InlineKeyboardButton("Cardano", callback_data="call_tocrscardanoETH")
btncrs_toTronETH = InlineKeyboardButton("Tron", callback_data="call_tocrstronETH")
btncrs_toBUSDETH = InlineKeyboardButton("BUSD", callback_data="call_tocrsbusdETH")
btncrs_toPolkadotETH = InlineKeyboardButton("Polkadot", callback_data="call_tocrspolkadotETH")
btncrs_toMaticETH = InlineKeyboardButton("Matic", callback_data="call_tocrsmaticETH")

# = = = = = = = CRS BUTTONS : FROM SOLANA = = = = = = = #
btncrs_toBitcoinSOL = InlineKeyboardButton("Bitcoin", callback_data="call_tocrsbitcoinSOL")
btncrs_toEthereumSOL = InlineKeyboardButton("Ethereum", callback_data="call_tocrsethereumSOL")
btncrs_toUSDTSOL = InlineKeyboardButton("USDT", callback_data="call_tocrsusdtSOL")
btncrs_toBNBSOL = InlineKeyboardButton("BNB", callback_data="call_tocrsbnbSOL")
btncrs_toCardanoSOL = InlineKeyboardButton("Cardano", callback_data="call_tocrscardanoSOL")
btncrs_toTronSOL = InlineKeyboardButton("Tron", callback_data="call_tocrstronSOL")
btncrs_toBUSDSOL = InlineKeyboardButton("BUSD", callback_data="call_tocrsbusdSOL")
btncrs_toPolkadotSOL = InlineKeyboardButton("Polkadot", callback_data="call_tocrspolkadotSOL")
btncrs_toMaticSOL = InlineKeyboardButton("Matic", callback_data="call_tocrsmaticSOL")

# = = = = = = = CRS BUTTONS : FROM USDT = = = = = = = #
btncrs_toBitcoinUSDT = InlineKeyboardButton("Bitcoin", callback_data="call_tocrsbitcoinUSDT")
btncrs_toEthereumUSDT = InlineKeyboardButton("Ethereum", callback_data="call_tocrsethereumUSDT")
btncrs_toSolanaUSDT = InlineKeyboardButton("Solana", callback_data="call_tocrssolUSDT")
btncrs_toBNBUSDT = InlineKeyboardButton("BNB", callback_data="call_tocrsbnbUSDT")
btncrs_toCardanoUSDT = InlineKeyboardButton("Cardano", callback_data="call_tocrscardanoUSDT")
btncrs_toTronUSDT = InlineKeyboardButton("Tron", callback_data="call_tocrstronUSDT")
btncrs_toBUSDUSDT = InlineKeyboardButton("BUSD", callback_data="call_tocrsbusdUSDT")
btncrs_toPolkadotUSDT = InlineKeyboardButton("Polkadot", callback_data="call_tocrspolkadotUSDT")
btncrs_toMaticUSDT = InlineKeyboardButton("Matic", callback_data="call_tocrsmaticUSDT")

# = = = = = = = CRS BUTTONS : FROM BNB = = = = = = = #
btncrs_toBitcoinBNB = InlineKeyboardButton("Bitcoin", callback_data="call_tocrsbitcoinBNB")
btncrs_toEthereumBNB = InlineKeyboardButton("Ethereum", callback_data="call_tocrsethereumBNB")
btncrs_toSolanaBNB = InlineKeyboardButton("Solana", callback_data="call_tocrssolBNB")
btncrs_toUSDTBNB = InlineKeyboardButton("USDT", callback_data="call_tocrsusdtBNB")
btncrs_toCardanoBNB = InlineKeyboardButton("Cardano", callback_data="call_tocrscardanoBNB")
btncrs_toTronBNB = InlineKeyboardButton("Tron", callback_data="call_tocrstronBNB")
btncrs_toBUSDBNB = InlineKeyboardButton("BUSD", callback_data="call_tocrsbusdBNB")
btncrs_toPolkadotBNB = InlineKeyboardButton("Polkadot", callback_data="call_tocrspolkadotBNB")
btncrs_toMaticBNB = InlineKeyboardButton("Matic", callback_data="call_tocrsmaticBNB")

# = = = = = = = CRS BUTTONS : FROM CARDANO = = = = = = = #
btncrs_toBitcoinCARDANO = InlineKeyboardButton("Bitcoin", callback_data="call_tocrsbitcoinCARDANO")
btncrs_toEthereumCARDANO = InlineKeyboardButton("Ethereum", callback_data="call_tocrsethereumCARDANO")
btncrs_toSolanaCARDANO = InlineKeyboardButton("Solana", callback_data="call_tocrssolCARDANO")
btncrs_toBNBCARDANO = InlineKeyboardButton("BNB", callback_data="call_tocrsbnbCARDANO")
btncrs_toUSDTCARDANO = InlineKeyboardButton("USDT", callback_data="call_tocrsusdtCARDANO")
btncrs_toCardanoCARDANO = InlineKeyboardButton("Cardano", callback_data="call_tocrscardanoCARDANO")
btncrs_toTronCARDANO = InlineKeyboardButton("Tron", callback_data="call_tocrstronCARDANO")
btncrs_toBUSDCARDANO = InlineKeyboardButton("BUSD", callback_data="call_tocrsbusdCARDANO")
btncrs_toPolkadotCARDANO = InlineKeyboardButton("Polkadot", callback_data="call_tocrspolkadotCARDANO")
btncrs_toMaticCARDANO = InlineKeyboardButton("Matic", callback_data="call_tocrsmaticCARDANO")

# = = = = = = = CRS BUTTONS : FROM TRON = = = = = = = #
btncrs_toBitcoinTRON = InlineKeyboardButton("Bitcoin", callback_data="call_tocrsbitcoinTRON")
btncrs_toEthereumTRON = InlineKeyboardButton("Ethereum", callback_data="call_tocrsethereumTRON")
btncrs_toSolanaTRON = InlineKeyboardButton("Solana", callback_data="call_tocrssolTRON")
btncrs_toBNBTRON = InlineKeyboardButton("BNB", callback_data="call_tocrsbnbTRON")
btncrs_toUSDTTRON = InlineKeyboardButton("USDT", callback_data="call_tocrsusdtTRON")
btncrs_toCardanoTRON = InlineKeyboardButton("Cardano", callback_data="call_tocrscardanoTRON")
btncrs_toTronTRON = InlineKeyboardButton("Tron", callback_data="call_tocrstronTRON")
btncrs_toBUSDTRON = InlineKeyboardButton("BUSD", callback_data="call_tocrsbusdTRON")
btncrs_toPolkadotTRON = InlineKeyboardButton("Polkadot", callback_data="call_tocrspolkadotTRON")
btncrs_toMaticTRON = InlineKeyboardButton("Matic", callback_data="call_tocrsmaticTRON")

# = = = = = = = CRS BUTTONS : FROM BUSD = = = = = = = #
btncrs_toBitcoinBUSD = InlineKeyboardButton("Bitcoin", callback_data="call_tocrsbitcoinBUSD")
btncrs_toEthereumBUSD = InlineKeyboardButton("Ethereum", callback_data="call_tocrsethereumBUSD")
btncrs_toSolanaBUSD = InlineKeyboardButton("Solana", callback_data="call_tocrssolBUSD")
btncrs_toBNBBUSD = InlineKeyboardButton("BNB", callback_data="call_tocrsbnbBUSD")
btncrs_toUSDTBUSD = InlineKeyboardButton("USDT", callback_data="call_tocrsusdtBUSD")
btncrs_toCardanoBUSD = InlineKeyboardButton("Cardano", callback_data="call_tocrscardanoBUSD")
btncrs_toTronBUSD = InlineKeyboardButton("Tron", callback_data="call_tocrstronBUSD")
btncrs_toBUSDBUSD = InlineKeyboardButton("BUSD", callback_data="call_tocrsbusdBUSD")
btncrs_toPolkadotBUSD = InlineKeyboardButton("Polkadot", callback_data="call_tocrspolkadotBUSD")
btncrs_toMaticBUSD = InlineKeyboardButton("Matic", callback_data="call_tocrsmaticBUSD")

# = = = = = = = CRS BUTTONS : FROM POLKADOT = = = = = = = #
btncrs_toBitcoinPOLKADOT = InlineKeyboardButton("Bitcoin", callback_data="call_tocrsbitcoinPOLKADOT")
btncrs_toEthereumPOLKADOT = InlineKeyboardButton("Ethereum", callback_data="call_tocrsethereumPOLKADOT")
btncrs_toSolanaPOLKADOT = InlineKeyboardButton("Solana", callback_data="call_tocrssolPOLKADOT")
btncrs_toBNBPOLKADOT = InlineKeyboardButton("BNB", callback_data="call_tocrsbnbPOLKADOT")
btncrs_toUSDTPOLKADOT = InlineKeyboardButton("USDT", callback_data="call_tocrsusdtPOLKADOT")
btncrs_toCardanoPOLKADOT = InlineKeyboardButton("Cardano", callback_data="call_tocrscardanoPOLKADOT")
btncrs_toTronPOLKADOT = InlineKeyboardButton("Tron", callback_data="call_tocrstronPOLKADOT")
btncrs_toBUSDPOLKADOT = InlineKeyboardButton("BUSD", callback_data="call_tocrsbusdPOLKADOT")
btncrs_toPolkadotPOLKADOT = InlineKeyboardButton("Polkadot", callback_data="call_tocrspolkadotPOLKADOT")
btncrs_toMaticPOLKADOT = InlineKeyboardButton("Matic", callback_data="call_tocrsmaticPOLKADOT")

# = = = = = = = CRS BUTTONS : FROM MATIC = = = = = = = #
btncrs_toBitcoinMATIC = InlineKeyboardButton("Bitcoin", callback_data="call_tocrsbitcoinMATIC")
btncrs_toEthereumMATIC = InlineKeyboardButton("Ethereum", callback_data="call_tocrsethereumMATIC")
btncrs_toSolanaMATIC = InlineKeyboardButton("Solana", callback_data="call_tocrssolMATIC")
btncrs_toBNBMATIC = InlineKeyboardButton("BNB", callback_data="call_tocrsbnbMATIC")
btncrs_toUSDTMATIC = InlineKeyboardButton("USDT", callback_data="call_tocrsusdtMATIC")
btncrs_toCardanoMATIC = InlineKeyboardButton("Cardano", callback_data="call_tocrscardanoMATIC")
btncrs_toTronMATIC = InlineKeyboardButton("Tron", callback_data="call_tocrstronMATIC")
btncrs_toBUSDMATIC = InlineKeyboardButton("BUSD", callback_data="call_tocrsbusdMATIC")
btncrs_toPolkadotMATIC = InlineKeyboardButton("Polkadot", callback_data="call_tocrspolkadotMATIC")
btncrs_toMaticMATIC = InlineKeyboardButton("Matic", callback_data="call_tocrsmaticMATIC")

# = = = = = = = CRS BUTTONS : COMFIRM = = = = = = = #
btnPaid = KeyboardButton("Подтверждаю")

# = = = = = = = P2P STABLE BUTTONS = = = = = = = #
btnFromMyBalance = KeyboardButton("С баланса бота 📲")
btnFromAnotherWallet = KeyboardButton("С другого кошелька 💸")

# = = = = = = = CRS BUTTON : CANCEL = = = = = = = #
btnCancel = KeyboardButton("Отмена 🔴")
menuConfirm = ReplyKeyboardMarkup(resize_keyboard=True).add(btnPaid).add(btnCancel)
menuBuyTo = ReplyKeyboardMarkup(resize_keyboard=True).add(btnFromMyBalance).add(btnFromAnotherWallet).add(btnCancel)

menuCancel = ReplyKeyboardMarkup(resize_keyboard=True).add(btnCancel)
maincrsfr = InlineKeyboardMarkup(resize_keyboard=True).add(btncrs_frBitcoin, btncrs_frEthereum, btncrs_frSolana).add(
    btncrs_frUSDT, btncrs_frBNB, btncrs_frCardano).add(btncrs_frTron, btncrs_frBUSD, btncrs_frPolkadot).add(
    btncrs_frMatic)
menuConfirm = ReplyKeyboardMarkup(resize_keyboard=True).add(btnPaid).add(btnCancel)

maincrstoBTC = InlineKeyboardMarkup(resize_keyboard=True).add(btncrs_toEthereumBTC, btncrs_toSolanaBTC,
                                                              btncrs_toUSDTBTC).add(btncrs_toBNBBTC,
                                                                                    btncrs_toCardanoBTC,
                                                                                    btncrs_toTronBTC).add(
    btncrs_toBUSDBTC, btncrs_toPolkadotBTC, btncrs_toMaticBTC)
maincrstoETH = InlineKeyboardMarkup(resize_keyboard=True).add(btncrs_toBitcoinETH, btncrs_toSolanaETH,
                                                              btncrs_toUSDTETH).add(btncrs_toBNBETH,
                                                                                    btncrs_toCardanoETH,
                                                                                    btncrs_toTronETH).add(
    btncrs_toBUSDETH, btncrs_toPolkadotETH, btncrs_toMaticETH)
maincrstoSOL = InlineKeyboardMarkup(resize_keyboard=True).add(btncrs_toBitcoinSOL, btncrs_toEthereumSOL,
                                                              btncrs_toUSDTSOL).add(btncrs_toBNBSOL,
                                                                                    btncrs_toCardanoSOL,
                                                                                    btncrs_toTronSOL).add(
    btncrs_toBUSDSOL, btncrs_toPolkadotSOL, btncrs_toMaticSOL)
maincrstoUSDT = InlineKeyboardMarkup(resize_keyboard=True).add(btncrs_toBitcoinUSDT, btncrs_toEthereumUSDT,
                                                               btncrs_toSolanaUSDT).add(btncrs_toBNBUSDT,
                                                                                        btncrs_toCardanoUSDT,
                                                                                        btncrs_toTronUSDT).add(
    btncrs_toBUSDUSDT, btncrs_toPolkadotUSDT, btncrs_toMaticUSDT)
maincrstoBNB = InlineKeyboardMarkup(resize_keyboard=True).add(btncrs_toBitcoinBNB, btncrs_toEthereumBNB,
                                                              btncrs_toSolanaBNB).add(btncrs_toUSDTBNB,
                                                                                      btncrs_toCardanoBNB,
                                                                                      btncrs_toTronBNB).add(
    btncrs_toBUSDBNB, btncrs_toPolkadotBNB, btncrs_toMaticBNB)
maincrstoCARDANO = InlineKeyboardMarkup(resize_keyboard=True).add(btncrs_toBitcoinCARDANO, btncrs_toEthereumCARDANO,
                                                                  btncrs_toSolanaCARDANO).add(btncrs_toUSDTCARDANO,
                                                                                              btncrs_toBNBCARDANO,
                                                                                              btncrs_toTronCARDANO).add(
    btncrs_toBUSDCARDANO, btncrs_toPolkadotCARDANO, btncrs_toMaticCARDANO)
maincrstoTRON = InlineKeyboardMarkup(resize_keyboard=True).add(btncrs_toBitcoinTRON, btncrs_toEthereumTRON,
                                                               btncrs_toSolanaTRON).add(btncrs_toUSDTTRON,
                                                                                        btncrs_toBNBTRON,
                                                                                        btncrs_toCardanoTRON).add(
    btncrs_toBUSDTRON, btncrs_toPolkadotTRON, btncrs_toMaticTRON)
maincrstoBUSD = InlineKeyboardMarkup(resize_keyboard=True).add(btncrs_toBitcoinBUSD, btncrs_toEthereumBUSD,
                                                               btncrs_toSolanaBUSD).add(btncrs_toUSDTBUSD,
                                                                                        btncrs_toBNBBUSD,
                                                                                        btncrs_toCardanoBUSD).add(
    btncrs_toTronBUSD, btncrs_toPolkadotBUSD, btncrs_toMaticBUSD)
maincrstoPOLKADOT = InlineKeyboardMarkup(resize_keyboard=True).add(btncrs_toBitcoinPOLKADOT, btncrs_toEthereumPOLKADOT,
                                                                   btncrs_toSolanaPOLKADOT).add(btncrs_toUSDTPOLKADOT,
                                                                                                btncrs_toBNBPOLKADOT,
                                                                                                btncrs_toCardanoPOLKADOT).add(
    btncrs_toBUSDPOLKADOT, btncrs_toTronPOLKADOT, btncrs_toMaticPOLKADOT)
maincrstoMATIC = InlineKeyboardMarkup(resize_keyboard=True).add(btncrs_toBitcoinMATIC, btncrs_toEthereumMATIC,
                                                                btncrs_toSolanaMATIC).add(btncrs_toUSDTMATIC,
                                                                                          btncrs_toBNBMATIC,
                                                                                          btncrs_toCardanoMATIC).add(
    btncrs_toBUSDMATIC, btncrs_toPolkadotMATIC, btncrs_toTronMATIC)


@dp.message_handler(lambda msg: msg.text.startswith('Crosschain обмен💱'))
async def val_crosschain_exchanger(message: types.Message):
    await message.answer(
        "Через этот сервис вы можете поменять одну криптовалюту на другую за пару кликов, например Bitcoin на Ethereum",
        reply_markup=types.ReplyKeyboardRemove())

    await message.answer("Выберите криптовалюту, которую хотите обменять:", reply_markup=maincrsfr)


# = = = = = = = CANCEL BUTTON : END STATES = = = = = = = #
@dp.message_handler(lambda msg: msg.text.startswith("Отмена 🔴"))
async def val_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


# = = = = = = = FROM BTC = = = = = = = #
@dp.callback_query_handler(text="call_frcrsbitcoin")
async def call_crosschain_frbitcoin(call: types.CallbackQuery):
    await call.message.answer("🪙 Выберите криптовалюту, которую хотите получить:", reply_markup=maincrstoBTC)
    await call.message.delete()


# = = = = = FROM BTC TO ETH = = = = = #
@dp.callback_query_handler(text="call_tocrsethereumBTC")
async def call_crosschain_frbitcoin_toeth(call: types.CallbackQuery):
    await FormCRSBTCtoETH.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSBTCtoETH.number)
async def process_numberCRS_btctoeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[3]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSBTCtoETH.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSBTCtoETH.type)
async def process_typeCRS_btctoeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *BTC*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinbtc) * float(ETHINRUB) * num)}` *ETH*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSBTCtoETH.next()
            await FormCRSBTCtoETH.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSBTCtoETH.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSBTCtoETH.adress)
async def process_adressCRS_btctoeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *BTC*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinbtc) * float(ETHINRUB) * num)} `\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *BTC*\n*Реквизиты для оплаты:* `{config.walletBitcoin}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSBTCtoETH.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSBTCtoETH.comfirm)
async def process_comfirmCRS_btctoeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BTC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbtc) * float(ETHINRUB) * num)}` *ETH*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay bitcoin -{num} {user_id}` & `/pay ethereum {'{:0.4f}'.format(float(ex.rubinbtc) * float(ETHINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BTC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbtc) * float(ETHINRUB) * num)}` *ETH*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay ethereum {'{:0.4f}'.format(float(ex.rubinbtc) * float(ETHINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM BTC TO SOL = = = = = #
@dp.callback_query_handler(text="call_tocrssolBTC")
async def call_crosschain_frbitcoin_tosol(call: types.CallbackQuery):
    await FormCRSBTCtoSOL.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSBTCtoSOL.number)
async def process_numberCRS_btctosol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[3]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSBTCtoSOL.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSBTCtoSOL.type)
async def process_typeCRS_btctosol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *BTC*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinbtc) * float(SOLINRUB) * num)}` *SOL*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSBTCtoSOL.next()
            await FormCRSBTCtoSOL.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSBTCtoSOL.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSBTCtoSOL.adress)
async def process_adressCRS_btctosol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *BTC*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinbtc) * float(SOLINRUB) * num)}` *SOL*\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *BTC*\n*Реквизиты для оплаты:* `{config.walletBitcoin}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSBTCtoSOL.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSBTCtoETH.comfirm)
async def process_comfirmCRS_btctosol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BTC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbtc) * float(SOLINRUB) * num)}` *SOL*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay bitcoin -{num} {user_id}` & `/pay solana {'{:0.4f}'.format(float(ex.rubinbtc) * float(ETHINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BTC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbtc) * float(SOLINRUB) * num)}` *SOL*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay solana {'{:0.4f}'.format(float(ex.rubinbtc) * float(ETHINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM BTC TO USDT = = = = = #
@dp.callback_query_handler(text="call_tocrsusdtBTC")
async def call_crosschain_frbitcoin_tousdt(call: types.CallbackQuery):
    await FormCRSBTCtoUSDT.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSBTCtoUSDT.number)
async def process_numberCRS_btctousdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[3]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSBTCtoUSDT.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSBTCtoUSDT.type)
async def process_typeCRS_btctousdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *BTC*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinbtc) * float(USDTINRUB) * num)}` *USDT*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSBTCtoUSDT.next()
            await FormCRSBTCtoUSDT.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSBTCtoUSDT.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSBTCtoUSDT.adress)
async def process_adressCRS_btctousdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *BTC*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinbtc) * float(USDTINRUB) * num)} `\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *BTC*\n*Реквизиты для оплаты:* `{config.walletBitcoin}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSBTCtoUSDT.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSBTCtoUSDT.comfirm)
async def process_comfirmCRS_btctousdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BTC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbtc) * float(USDTINRUB) * num)}` *USDT*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay bitcoin -{num} {user_id}` & `/pay usdt {'{:0.4f}'.format(float(ex.rubinbtc) * float(USDTINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BTC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbtc) * float(USDTINRUB) * num)}` *USDT*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay usdt {'{:0.4f}'.format(float(ex.rubinbtc) * float(USDTINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM BTC TO BNB = = = = = #
@dp.callback_query_handler(text="call_tocrsbnbBTC")
async def call_crosschain_frbitcoin_tobnb(call: types.CallbackQuery):
    await FormCRSBTCtoBNB.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSBTCtoBNB.number)
async def process_numberCRS_btctobnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[3]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSBTCtoBNB.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSBTCtoBNB.type)
async def process_typeCRS_btctobnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *BTC*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinbtc) * float(BNBINRUB) * num)}` *BNB*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSBTCtoBNB.next()
            await FormCRSBTCtoBNB.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSBTCtoBNB.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSBTCtoBNB.adress)
async def process_adressCRS_btctobnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *BTC*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinbtc) * float(BNBINRUB) * num)} `\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *BTC*\n*Реквизиты для оплаты:* `{config.walletBitcoin}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSBTCtoBNB.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSBTCtoBNB.comfirm)
async def process_comfirmCRS_btctobnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BTC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbtc) * float(BNBINRUB) * num)}` *BNB*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay bitcoin -{num} {user_id}` & `/pay bnb {'{:0.4f}'.format(float(ex.rubinbtc) * float(BNBINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BTC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbtc) * float(BNBINRUB) * num)}` *BNB*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay bnb {'{:0.4f}'.format(float(ex.rubinbtc) * float(BNBINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM BTC TO CARDANO = = = = = #
@dp.callback_query_handler(text="call_tocrscardanoBTC")
async def call_crosschain_frbitcoin_tocardano(call: types.CallbackQuery):
    await FormCRSBTCtoCARDANO.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSBTCtoCARDANO.number)
async def process_numberCRS_btctocardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[3]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSBTCtoCARDANO.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSBTCtoCARDANO.type)
async def process_typeCRS_btctocardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *BTC*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinbtc) * float(CARDANOINRUB) * num)}` *CARDANO*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSBTCtoCARDANO.next()
            await FormCRSBTCtoCARDANO.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSBTCtoCARDANO.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSBTCtoCARDANO.adress)
async def process_adressCRS_btctocardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *BTC*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinbtc) * float(CARDANOINRUB) * num)} `\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *BTC*\n*Реквизиты для оплаты:* `{config.walletBitcoin}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSBTCtoCARDANO.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSBTCtoCARDANO.comfirm)
async def process_comfirmCRS_btctocardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BTC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbtc) * float(CARDANOINRUB) * num)}` *CARDANO*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay bitcoin -{num} {user_id}` & `/pay cardano {'{:0.4f}'.format(float(ex.rubinbtc) * float(CARDANOINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BTC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbtc) * float(CARDANOINRUB) * num)}` *CARDANO*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay cardano {'{:0.4f}'.format(float(ex.rubinbtc) * float(CARDANOINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM BTC TO TRON = = = = = #
@dp.callback_query_handler(text="call_tocrstronBTC")
async def call_crosschain_frbitcoin_totron(call: types.CallbackQuery):
    await FormCRSBTCtoTRON.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSBTCtoTRON.number)
async def process_numberCRS_btctotron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[3]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSBTCtoTRON.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSBTCtoTRON.type)
async def process_typeCRS_btctotron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *BTC*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinbtc) * float(TRONINRUB) * num)}` *TRON*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSBTCtoTRON.next()
            await FormCRSBTCtoTRON.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSBTCtoTRON.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSBTCtoTRON.adress)
async def process_adressCRS_btctotron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *BTC*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinbtc) * float(TRONINRUB) * num)} `\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *BTC*\n*Реквизиты для оплаты:* `{config.walletBitcoin}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSBTCtoTRON.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSBTCtoTRON.comfirm)
async def process_comfirmCRS_btctotron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BTC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbtc) * float(TRONINRUB) * num)}` *TRON*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay bitcoin -{num} {user_id}` & `/pay tron {'{:0.4f}'.format(float(ex.rubinbtc) * float(TRONINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BTC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbtc) * float(TRONINRUB) * num)}` *TRON*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay tron {'{:0.4f}'.format(float(ex.rubinbtc) * float(TRONINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM BTC TO BUSD = = = = = #
@dp.callback_query_handler(text="call_tocrsbusdBTC")
async def call_crosschain_frbitcoin_tobusd(call: types.CallbackQuery):
    await FormCRSBTCtoBUSD.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSBTCtoBUSD.number)
async def process_numberCRS_btctobusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[3]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSBTCtoBUSD.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSBTCtoBUSD.type)
async def process_typeCRS_btctobusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *BTC*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinbtc) * float(BUSDINRUB) * num)}` *BUSD*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSBTCtoBUSD.next()
            await FormCRSBTCtoBUSD.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSBTCtoBUSD.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSBTCtoBUSD.adress)
async def process_adressCRS_btctobusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *BTC*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinbtc) * float(BUSDINRUB) * num)} `\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *BTC*\n*Реквизиты для оплаты:* `{config.walletBitcoin}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSBTCtoBUSD.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSBTCtoBUSD.comfirm)
async def process_comfirmCRS_btctobusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BTC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbtc) * float(BUSDINRUB) * num)}` *BUSD*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay bitcoin -{num} {user_id}` & `/pay busd {'{:0.4f}'.format(float(ex.rubinbtc) * float(BUSDINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BTC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbtc) * float(BUSDINRUB) * num)}` *BUSD*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay busd {'{:0.4f}'.format(float(ex.rubinbtc) * float(BUSDINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM BTC TO POLKADOT = = = = = #
@dp.callback_query_handler(text="call_tocrspolkadotBTC")
async def call_crosschain_frbitcoin_topolkadot(call: types.CallbackQuery):
    await FormCRSBTCtoPOLKADOT.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSBTCtoPOLKADOT.number)
async def process_numberCRS_btctopolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[3]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSBTCtoPOLKADOT.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSBTCtoPOLKADOT.type)
async def process_typeCRS_btctopolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *BTC*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinbtc) * float(POLKADOTINRUB) * num)}` *POLKADOT*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSBTCtoPOLKADOT.next()
            await FormCRSBTCtoPOLKADOT.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSBTCtoPOLKADOT.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSBTCtoPOLKADOT.adress)
async def process_adressCRS_btctopolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *BTC*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinbtc) * float(POLKADOTINRUB) * num)} `\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *BTC*\n*Реквизиты для оплаты:* `{config.walletBitcoin}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSBTCtoPOLKADOT.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSBTCtoPOLKADOT.comfirm)
async def process_comfirmCRS_btctopolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BTC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbtc) * float(POLKADOTINRUB) * num)}` *DOT*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay bitcoin -{num} {user_id}` & `/pay polkadot {'{:0.4f}'.format(float(ex.rubinbtc) * float(POLKADOTINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BTC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbtc) * float(POLKADOTINRUB) * num)}` *DOT*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay polkadot {'{:0.4f}'.format(float(ex.rubinbtc) * float(POLKADOTINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM BTC TO MATIC = = = = = #
@dp.callback_query_handler(text="call_tocrsmaticBTC")
async def call_crosschain_frbitcoin_tomatic(call: types.CallbackQuery):
    await FormCRSBTCtoMATIC.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSBTCtoMATIC.number)
async def process_numberCRS_btctomatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[3]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSBTCtoMATIC.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSBTCtoMATIC.type)
async def process_typeCRS_btctomatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *BTC*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinbtc) * float(MATICINRUB) * num)}` *MATIC*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSBTCtoMATIC.next()
            await FormCRSBTCtoMATIC.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSBTCtoMATIC.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSBTCtoMATIC.adress)
async def process_adressCRS_btctomatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *BTC*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinbtc) * float(MATICINRUB) * num)} `\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *BTC*\n*Реквизиты для оплаты:* `{config.walletBitcoin}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSBTCtoMATIC.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSBTCtoMATIC.comfirm)
async def process_comfirmCRS_btctomatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BTC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbtc) * float(MATICINRUB) * num)}` *MATIC*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay bitcoin -{num} {user_id}` & `/pay matic {'{:0.4f}'.format(float(ex.rubinbtc) * float(MATICINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BTC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbtc) * float(MATICINRUB) * num)}` *MATIC*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay matic {'{:0.4f}'.format(float(ex.rubinbtc) * float(MATICINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = FROM ETH = = = = = = = #
@dp.callback_query_handler(text="call_frcrsethereum")
async def call_crosschain_frethereum(call: types.CallbackQuery):
    await call.message.answer("🪙 Выберите криптовалюту, которую хотите получить:", reply_markup=maincrstoETH)
    await call.message.delete()


# = = = = = FROM ETH TO BTC = = = = = #
@dp.callback_query_handler(text="call_tocrsbitcoinETH")
async def call_crosschain_frethereum_tobtc(call: types.CallbackQuery):
    await FormCRSETHtoBTC.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:",
                              reply_markup=menuCancel)


@dp.message_handler(state=FormCRSETHtoBTC.number)
async def process_numberCRS_ethtobtc(message: types.Message,
                                     state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(
                f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer(
                    "Действие отменено. Вы вернулись в главное меню",
                    reply_markup=st.mainMenu)
            elif float(data['number']) > row[4]:
                await state.finish()
                await message.answer(
                    "На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                    reply_markup=st.mainMenu)
            else:
                await FormCRSETHtoBTC.next()
                await message.answer("Откуда перевести средства:",
                                     reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSETHtoBTC.type)
async def process_typeCRS_ethtobtc(message: types.Message,
                                   state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *ETH\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinbeth) * float(BTCINRUB) * num)}` *BTC")
            await message.answer("Подтвердите ваш платёж",
                                 reply_markup=menuConfirm)
            await FormCRSETHtoBTC.next()
            await FormCRSETHtoBTC.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSETHtoBTC.next()
            await message.answer("Введите целевой кошелёк: ",
                                 reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer(
                "Действие отменено. Вы вернулись в главное меню",
                reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSETHtoBTC.adress)
async def process_adressCRS_ethtobtc(message: types.Message,
                                     state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *ETH\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinbtc) * float(BTCINRUB) * num)} `\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *ETH\n*Реквизиты для оплаты:* `{config.walletEthereum}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSETHtoBTC.next()
        await message.answer("Подтвердите ваш платёж",
                             reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSETHtoBTC.comfirm)
async def process_comfirmCRS_ethtobtc(message: types.Message,
                                      state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *ETH\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbtc) * float(BTCINRUB) * num)}` *BTC*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay ethereum -{num} {user_id}` & `/pay bitcoin {'{:0.4f}'.format(float(ex.rubinbeth) * float(BTCINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(
                    config.admin_id,
                    f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *ETH\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbeth) * float(BTCINRUB) * num)}` *BTC*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay bitcoin {'{:0.4f}'.format(float(ex.rubinbeth) * float(BTCINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню",
                                 reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM ETH TO SOL = = = = = #
@dp.callback_query_handler(text="call_tocrssolETH")
async def call_crosschain_frethereum_tosol(call: types.CallbackQuery):
    await FormCRSETHtoSOL.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSETHtoSOL.number)
async def process_numberCRS_ethtosol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[4]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSETHtoSOL.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSETHtoSOL.type)
async def process_typeCRS_ethtosol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *ETH*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubineth) * float(SOLINRUB) * num)}` *SOL*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSETHtoSOL.next()
            await FormCRSETHtoSOL.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSETHtoSOL.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSETHtoSOL.adress)
async def process_adressCRS_ethtosol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *ETH*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubineth) * float(SOLINRUB) * num)} `\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *ETH*\n*Реквизиты для оплаты:* `{config.walletEthereum}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSETHtoSOL.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSETHtoSOL.comfirm)
async def process_comfirmCRS_ethtosol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *ETH*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubineth) * float(SOLINRUB) * num)}` *SOL*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay ethereum -{num} {user_id}` & `/pay solana {'{:0.4f}'.format(float(ex.rubineth) * float(SOLINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *ETH*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubineth) * float(SOLINRUB) * num)}` *SOL*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay solana {'{:0.4f}'.format(float(ex.rubineth) * float(SOLINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSETHtoSOL.comfirm)
async def process_comfirmCRS_ethtosol(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *ETH*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubineth) * float(SOLINRUB) * num)}` *SOL*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay ethereum -{num} {user_id}` & `/pay solana {'{:0.4f}'.format(float(ex.rubineth) * float(SOLINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM ETH TO USDT = = = = = #
@dp.callback_query_handler(text="call_tocrsusdtETH")
async def call_crosschain_frethereum_tousdt(call: types.CallbackQuery):
    await FormCRSETHtoUSDT.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSETHtoUSDT.number)
async def process_numberCRS_ethtousdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[4]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSETHtoUSDT.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSETHtoUSDT.type)
async def process_typeCRS_ethtousdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *ETH*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubineth) * float(USDTINRUB) * num)}` *USDT*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSETHtoUSDT.next()
            await FormCRSETHtoUSDT.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSETHtoUSDT.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSETHtoUSDT.adress)
async def process_adressCRS_ethtousdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *ETH*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubineth) * float(USDTINRUB) * num)} `\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *ETH*\n*Реквизиты для оплаты:* `{config.walletEthereum}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSETHtoUSDT.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSETHtoUSDT.comfirm)
async def process_comfirmCRS_ethtousdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *ETH*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubineth) * float(USDTINRUB) * num)}` *USDT*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay ethereum -{num} {user_id}` & `/pay usdt {'{:0.4f}'.format(float(ex.rubineth) * float(USDTINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *ETH*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubineth) * float(USDTINRUB) * num)}` *USDT*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay usdt {'{:0.4f}'.format(float(ex.rubineth) * float(USDTINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSETHtoUSDT.comfirm)
async def process_comfirmCRS_ethtousdt(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *ETH*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubineth) * float(USDTINRUB) * num)}` *USDT*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay ethereum -{num} {user_id}` & `/pay usdt {'{:0.4f}'.format(float(ex.rubineth) * float(USDTINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM ETH TO BNB = = = = = #
@dp.callback_query_handler(text="call_tocrsbnbETH")
async def call_crosschain_frethereum_tobnb(call: types.CallbackQuery):
    await FormCRSETHtoBNB.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSETHtoBNB.number)
async def process_numberCRS_ethtobnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[4]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSETHtoBNB.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSETHtoBNB.type)
async def process_typeCRS_ethtobnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *ETH*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubineth) * float(BNBINRUB) * num)}` *BNB*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSETHtoBNB.next()
            await FormCRSETHtoBNB.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSETHtoBNB.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSETHtoBNB.adress)
async def process_adressCRS_ethtobnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *ETH*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubineth) * float(BNBINRUB) * num)} `\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *ETH*\n*Реквизиты для оплаты:* `{config.walletEthereum}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSETHtoBNB.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSETHtoBNB.comfirm)
async def process_comfirmCRS_ethtobnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *ETH*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubineth) * float(BNBINRUB) * num)}` *BNB*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay ethereum -{num} {user_id}` & `/pay bnb {'{:0.4f}'.format(float(ex.rubineth) * float(BNBINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *ETH*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubineth) * float(BNBINRUB) * num)}` *BNB*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay bnb {'{:0.4f}'.format(float(ex.rubineth) * float(BNBINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM ETH TO CARDANO = = = = = #
@dp.callback_query_handler(text="call_tocrscardanoETH")
async def call_crosschain_frethereum_tocardano(call: types.CallbackQuery):
    await FormCRSETHtoCARDANO.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSETHtoCARDANO.number)
async def process_numberCRS_ethtocardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[4]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSETHtoCARDANO.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSETHtoCARDANO.type)
async def process_typeCRS_ethtocardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *ETH*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubineth) * float(CARDANOINRUB) * num)}` *CARDANO*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSETHtoCARDANO.next()
            await FormCRSETHtoCARDANO.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSETHtoCARDANO.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSETHtoCARDANO.adress)
async def process_adressCRS_ethtocardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *ETH*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubineth) * float(CARDANOINRUB) * num)} `\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *ETH*\n*Реквизиты для оплаты:* `{config.walletEthereum}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSETHtoCARDANO.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSETHtoCARDANO.comfirm)
async def process_comfirmCRS_ethtocardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *ETH*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubineth) * float(CARDANOINRUB) * num)}` *CARDANO*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay ethereum -{num} {user_id}` & `/pay cardano {'{:0.4f}'.format(float(ex.rubineth) * float(CARDANOINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *ETH*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubineth) * float(CARDANOINRUB) * num)}` *CARDANO*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay cardano {'{:0.4f}'.format(float(ex.rubineth) * float(CARDANOINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSETHtoCARDANO.comfirm)
async def process_comfirmCRS_ethtocardano(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *ETH*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubineth) * float(CARDANOINRUB) * num)}` *CARDANO*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay ethereum -{num} {user_id}` & `/pay cardano {'{:0.4f}'.format(float(ex.rubineth) * float(CARDANOINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM ETH TO TRON = = = = = #
@dp.callback_query_handler(text="call_tocrstronETH")
async def call_crosschain_frethereum_totron(call: types.CallbackQuery):
    await FormCRSETHtoTRON.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSETHtoTRON.number)
async def process_numberCRS_ethtotron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[4]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSETHtoTRON.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSETHtoTRON.type)
async def process_typeCRS_ethtotron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *ETH*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubineth) * float(TRONINRUB) * num)}` *TRON*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSETHtoTRON.next()
            await FormCRSETHtoTRON.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSETHtoTRON.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSETHtoTRON.adress)
async def process_adressCRS_ethtotron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *ETH*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubineth) * float(TRONINRUB) * num)} `\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *ETH*\n*Реквизиты для оплаты:* `{config.walletEthereum}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSETHtoTRON.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSETHtoTRON.comfirm)
async def process_comfirmCRS_ethtotron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *ETH*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubineth) * float(TRONINRUB) * num)}` *TRON*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay ethereum -{num} {user_id}` & `/pay tron {'{:0.4f}'.format(float(ex.rubineth) * float(TRONINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *ETH*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubineth) * float(TRONINRUB) * num)}` *TRON*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay tron {'{:0.4f}'.format(float(ex.rubineth) * float(TRONINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSETHtoTRON.comfirm)
async def process_comfirmCRS_ethtotron(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *ETH*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubineth) * float(TRONINRUB) * num)}` *TRON*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay ethereum -{num} {user_id}` & `/pay tron {'{:0.4f}'.format(float(ex.rubineth) * float(TRONINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM ETH TO BUSD = = = = = #
@dp.callback_query_handler(text="call_tocrsbusdETH")
async def call_crosschain_frethereum_tobusd(call: types.CallbackQuery):
    await FormCRSETHtoBUSD.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSETHtoBUSD.number)
async def process_numberCRS_ethtobusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[4]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSETHtoBUSD.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSETHtoBUSD.type)
async def process_typeCRS_ethtobusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *ETH*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubineth) * float(BUSDINRUB) * num)}` *BUSD*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSETHtoBUSD.next()
            await FormCRSETHtoBUSD.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSETHtoBUSD.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSETHtoBUSD.adress)
async def process_adressCRS_ethtobusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *ETH*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubineth) * float(BUSDINRUB) * num)} `\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *ETH*\n*Реквизиты для оплаты:* `{config.walletEthereum}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSETHtoBUSD.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSETHtoBUSD.comfirm)
async def process_comfirmCRS_ethtobusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *ETH*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubineth) * float(BUSDINRUB) * num)}` *BUSD*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay ethereum -{num} {user_id}` & `/pay busd {'{:0.4f}'.format(float(ex.rubineth) * float(BUSDINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *ETH*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubineth) * float(BUSDINRUB) * num)}` *BUSD*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay busd {'{:0.4f}'.format(float(ex.rubineth) * float(BUSDINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSETHtoBUSD.comfirm)
async def process_comfirmCRS_ethtobusd(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *ETH*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubineth) * float(BUSDINRUB) * num)}` *BUSD*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay ethereum -{num} {user_id}` & `/pay busd {'{:0.4f}'.format(float(ex.rubineth) * float(BUSDINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM ETH TO POLKADOT = = = = = #
@dp.callback_query_handler(text="call_tocrspolkadotETH")
async def call_crosschain_frethereum_topolkadot(call: types.CallbackQuery):
    await FormCRSETHtoPOLKADOT.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSETHtoPOLKADOT.number)
async def process_numberCRS_ethtopolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[4]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSETHtoPOLKADOT.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSETHtoPOLKADOT.type)
async def process_typeCRS_ethtopolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *ETH*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubineth) * float(POLKADOTINRUB) * num)}` *POLKADOT*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSETHtoPOLKADOT.next()
            await FormCRSETHtoPOLKADOT.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSETHtoPOLKADOT.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSETHtoPOLKADOT.adress)
async def process_adressCRS_ethtopolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *ETH*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubineth) * float(POLKADOTINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *ETH*\n*Реквизиты для оплаты:* `{config.walletEthereum}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSETHtoPOLKADOT.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSETHtoPOLKADOT.comfirm)
async def process_comfirmCRS_ethtopolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *ETH*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubineth) * float(POLKADOTINRUB) * num)}` *DOT*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay ethereum -{num} {user_id}` & `/pay polkadot {'{:0.4f}'.format(float(ex.rubineth) * float(POLKADOTINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *ETH*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubineth) * float(POLKADOTINRUB) * num)}` *DOT*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay polkadot {'{:0.4f}'.format(float(ex.rubineth) * float(POLKADOTINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSETHtoPOLKADOT.comfirm)
async def process_comfirmCRS_ethtopolkadot(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *ETH*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubineth) * float(POLKADOTINRUB) * num)}` *DOT*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay ethereum -{num} {user_id}` & `/pay polkadot {'{:0.4f}'.format(float(ex.rubineth) * float(POLKADOTINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM ETH TO MATIC = = = = = #
@dp.callback_query_handler(text="call_tocrsmaticETH")
async def call_crosschain_frethereum_tomatic(call: types.CallbackQuery):
    await FormCRSETHtoMATIC.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSETHtoMATIC.number)
async def process_numberCRS_ethtomatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[4]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSETHtoMATIC.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSETHtoMATIC.type)
async def process_typeCRS_ethtomatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *ETH*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubineth) * float(MATICINRUB) * num)}` *MATIC*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSETHtoMATIC.next()
            await FormCRSETHtoMATIC.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSETHtoMATIC.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSETHtoMATIC.adress)
async def process_adressCRS_ethtomatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *ETH*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubineth) * float(MATICINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *ETH*\n*Реквизиты для оплаты:* `{config.walletEthereum}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSETHtoMATIC.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSETHtoMATIC.comfirm)
async def process_comfirmCRS_ethtomatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *ETH*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubineth) * float(MATICINRUB) * num)}` *MATIC*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay ethereum -{num} {user_id}` & `/pay matic {'{:0.4f}'.format(float(ex.rubineth) * float(MATICINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *ETH*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubineth) * float(MATICINRUB) * num)}` *MATIC*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay matic {'{:0.4f}'.format(float(ex.rubineth) * float(MATICINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSETHtoMATIC.comfirm)
async def process_comfirmCRS_ethtomatic(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *ETH*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubineth) * float(MATICINRUB) * num)}` *MATIC*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay ethereum -{num} {user_id}` & `/pay matic {'{:0.4f}'.format(float(ex.rubineth) * float(MATICINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = FROM SOL = = = = = = = #
@dp.callback_query_handler(text="call_frcrssolana")
async def call_crosschain_frsolana(call: types.CallbackQuery):
    await call.message.answer("🪙 Выберите криптовалюту, которую хотите получить:", reply_markup=maincrstoSOL)
    await call.message.delete()


# = = = = = FROM SOL TO BTC = = = = = #
@dp.callback_query_handler(text="call_tocrsbitcoinSOL")
async def call_crosschain_frsolana_tobtc(call: types.CallbackQuery):
    await FormCRSSOLtoBTC.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSSOLtoBTC.number)
async def process_numberCRS_soltobtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[5]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSSOLtoBTC.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSSOLtoBTC.type)
async def process_typeCRS_soltobtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *SOL*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(BTCINRUB) * num)}` *BTC*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSSOLtoBTC.next()
            await FormCRSSOLtoBTC.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSSOLtoBTC.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSSOLtoBTC.adress)
async def process_adressCRS_soltobtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *SOL*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(BTCINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *SOL*\n*Реквизиты для оплаты:* `{config.walletSolana}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSSOLtoBTC.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSSOLtoBTC.comfirm)
async def process_comfirmCRS_soltobtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *SOL*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(BTCINRUB) * num)}` *BTC*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay solana -{num} {user_id}` & `/pay bitcoin {'{:0.4f}'.format(float(ex.rubinsol) * float(BTCINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *SOL*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(BTCINRUB) * num)}` *BTC*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay bitcoin {'{:0.4f}'.format(float(ex.rubinsol) * float(BTCINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSSOLtoBTC.comfirm)
async def process_comfirmCRS_soltobtc(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *SOL*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(BTCINRUB) * num)}` *BTC*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay solana -{num} {user_id}` & `/pay bitcoin {'{:0.4f}'.format(float(ex.rubinsol) * float(BTCINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM SOL TO ETH = = = = = #
@dp.callback_query_handler(text="call_tocrsethereumSOL")
async def call_crosschain_frsolana_toeth(call: types.CallbackQuery):
    await FormCRSSOLtoETH.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSSOLtoETH.number)
async def process_numberCRS_soltoeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[5]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSSOLtoETH.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSSOLtoETH.type)
async def process_typeCRS_soltoeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *SOL*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(ETHINRUB) * num)}` *ETH*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSSOLtoETH.next()
            await FormCRSSOLtoETH.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSSOLtoETH.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSSOLtoETH.adress)
async def process_adressCRS_soltoeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *SOL*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(ETHINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *SOL*\n*Реквизиты для оплаты:* `{config.walletSolana}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSSOLtoETH.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSSOLtoETH.comfirm)
async def process_comfirmCRS_soltoeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *SOL*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(ETHINRUB) * num)}` *ETH*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay solana -{num} {user_id}` & `/pay ethereum {'{:0.4f}'.format(float(ex.rubinsol) * float(ETHINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *SOL*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(ETHINRUB) * num)}` *ETH*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay ethereum {'{:0.4f}'.format(float(ex.rubinsol) * float(ETHINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSSOLtoETH.comfirm)
async def process_comfirmCRS_soltoeth(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *SOL*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(ETHINRUB) * num)}` *ETH*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay solana -{num} {user_id}` & `/pay ethereum {'{:0.4f}'.format(float(ex.rubinsol) * float(ETHINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM SOL TO USDT = = = = = #
@dp.callback_query_handler(text="call_tocrsusdtSOL")
async def call_crosschain_frsolana_tousdt(call: types.CallbackQuery):
    await FormCRSSOLtoUSDT.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSSOLtoUSDT.number)
async def process_numberCRS_soltousdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[5]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSSOLtoUSDT.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSSOLtoUSDT.type)
async def process_typeCRS_soltousdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *SOL*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(USDTINRUB) * num)}` *USDT*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSSOLtoUSDT.next()
            await FormCRSSOLtoUSDT.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSSOLtoUSDT.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSSOLtoUSDT.adress)
async def process_adressCRS_soltousdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *SOL*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(USDTINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *SOL*\n*Реквизиты для оплаты:* `{config.walletSolana}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSSOLtoUSDT.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSSOLtoUSDT.comfirm)
async def process_comfirmCRS_soltousdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *SOL*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(USDTINRUB) * num)}` *USDT*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay solana -{num} {user_id}` & `/pay usdt {'{:0.4f}'.format(float(ex.rubinsol) * float(USDTINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *SOL*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(USDTINRUB) * num)}` *USDT*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay usdt {'{:0.4f}'.format(float(ex.rubinsol) * float(USDTINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSSOLtoUSDT.comfirm)
async def process_comfirmCRS_soltousdt(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *SOL*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(USDTINRUB) * num)}` *USDT*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay solana -{num} {user_id}` & `/pay usdt {'{:0.4f}'.format(float(ex.rubinsol) * float(USDTINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM SOL TO BNB = = = = = #
@dp.callback_query_handler(text="call_tocrsbnbSOL")
async def call_crosschain_frsolana_tobnb(call: types.CallbackQuery):
    await FormCRSSOLtoBNB.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSSOLtoBNB.number)
async def process_numberCRS_soltobnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[5]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSSOLtoBNB.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSSOLtoBNB.type)
async def process_typeCRS_soltobnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *SOL*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(BNBINRUB) * num)}` *BNB*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSSOLtoBNB.next()
            await FormCRSSOLtoBNB.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSSOLtoBNB.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSSOLtoBNB.adress)
async def process_adressCRS_soltobnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *SOL*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(BNBINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *SOL*\n*Реквизиты для оплаты:* `{config.walletSolana}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSSOLtoBNB.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSSOLtoBNB.comfirm)
async def process_comfirmCRS_soltobnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *SOL*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(BNBINRUB) * num)}` *BNB*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay solana -{num} {user_id}` & `/pay bnb {'{:0.4f}'.format(float(ex.rubinsol) * float(BNBINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *SOL*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(BNBINRUB) * num)}` *BNB*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay bnb {'{:0.4f}'.format(float(ex.rubinsol) * float(BNBINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSSOLtoBNB.comfirm)
async def process_comfirmCRS_soltobnb(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *SOL*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(BNBINRUB) * num)}` *BNB*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay solana -{num} {user_id}` & `/pay bnb {'{:0.4f}'.format(float(ex.rubinsol) * float(BNBINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM SOL TO CARDANO = = = = = #
@dp.callback_query_handler(text="call_tocrscardanoSOL")
async def call_crosschain_frsolana_tocardano(call: types.CallbackQuery):
    await FormCRSSOLtoCARDANO.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSSOLtoCARDANO.number)
async def process_numberCRS_soltocardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[5]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSSOLtoCARDANO.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSSOLtoCARDANO.type)
async def process_typeCRS_soltocardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *SOL*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(CARDANOINRUB) * num)}` *CARDANO*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSSOLtoCARDANO.next()
            await FormCRSSOLtoCARDANO.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSSOLtoCARDANO.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSSOLtoCARDANO.adress)
async def process_adressCRS_soltocardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *SOL*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(CARDANOINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *SOL*\n*Реквизиты для оплаты:* `{config.walletSolana}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSSOLtoCARDANO.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSSOLtoCARDANO.comfirm)
async def process_comfirmCRS_soltocardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *SOL*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(CARDANOINRUB) * num)}` *CARDANO*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay solana -{num} {user_id}` & `/pay cardano {'{:0.4f}'.format(float(ex.rubinsol) * float(CARDANOINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *SOL*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(CARDANOINRUB) * num)}` *CARDANO*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay cardano {'{:0.4f}'.format(float(ex.rubinsol) * float(CARDANOINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSSOLtoCARDANO.comfirm)
async def process_comfirmCRS_soltocardano(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *SOL*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(CARDANOINRUB) * num)}` *CARDANO*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay solana -{num} {user_id}` & `/pay cardano {'{:0.4f}'.format(float(ex.rubinsol) * float(CARDANOINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM SOL TO TRON = = = = = #
@dp.callback_query_handler(text="call_tocrstronSOL")
async def call_crosschain_frsolana_totron(call: types.CallbackQuery):
    await FormCRSSOLtoTRON.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSSOLtoTRON.number)
async def process_numberCRS_soltotron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[5]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSSOLtoTRON.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSSOLtoTRON.type)
async def process_typeCRS_soltotron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *SOL*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(TRONINRUB) * num)}` *TRON*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSSOLtoTRON.next()
            await FormCRSSOLtoTRON.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSSOLtoTRON.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSSOLtoTRON.adress)
async def process_adressCRS_soltotron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *SOL*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(TRONINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *SOL*\n*Реквизиты для оплаты:* `{config.walletSolana}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSSOLtoTRON.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSSOLtoTRON.comfirm)
async def process_comfirmCRS_soltotron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *SOL*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(TRONINRUB) * num)}` *TRON*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay solana -{num} {user_id}` & `/pay tron {'{:0.4f}'.format(float(ex.rubinsol) * float(TRONINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *SOL*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(TRONINRUB) * num)}` *TRON*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay tron {'{:0.4f}'.format(float(ex.rubinsol) * float(TRONINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSSOLtoTRON.comfirm)
async def process_comfirmCRS_soltotron(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *SOL*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(TRONINRUB) * num)}` *TRON*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay solana -{num} {user_id}` & `/pay tron {'{:0.4f}'.format(float(ex.rubinsol) * float(TRONINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM SOL TO BUSD = = = = = #
@dp.callback_query_handler(text="call_tocrsbusdSOL")
async def call_crosschain_frsolana_tobusd(call: types.CallbackQuery):
    await FormCRSSOLtoBUSD.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSSOLtoBUSD.number)
async def process_numberCRS_soltobusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[5]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSSOLtoBUSD.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSSOLtoBUSD.type)
async def process_typeCRS_soltobusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *SOL*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(BUSDINRUB) * num)}` *BUSD*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSSOLtoBUSD.next()
            await FormCRSSOLtoBUSD.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSSOLtoBUSD.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSSOLtoBUSD.adress)
async def process_adressCRS_soltobusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *SOL*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(BUSDINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *SOL*\n*Реквизиты для оплаты:* `{config.walletSolana}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSSOLtoBUSD.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSSOLtoBUSD.comfirm)
async def process_comfirmCRS_soltobusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *SOL*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(BUSDINRUB) * num)}` *BUSD*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay solana -{num} {user_id}` & `/pay busd {'{:0.4f}'.format(float(ex.rubinsol) * float(BUSDINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *SOL*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(BUSDINRUB) * num)}` *BUSD*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay busd {'{:0.4f}'.format(float(ex.rubinsol) * float(BUSDINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSSOLtoBUSD.comfirm)
async def process_comfirmCRS_soltobusd(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *SOL*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(BUSDINRUB) * num)}` *BUSD*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay solana -{num} {user_id}` & `/pay busd {'{:0.4f}'.format(float(ex.rubinsol) * float(BUSDINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM SOL TO POLKADOT = = = = = #
@dp.callback_query_handler(text="call_tocrspolkadotSOL")
async def call_crosschain_frsolana_topolkadot(call: types.CallbackQuery):
    await FormCRSSOLtoPOLKADOT.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSSOLtoPOLKADOT.number)
async def process_numberCRS_soltopolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[5]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSSOLtoPOLKADOT.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSSOLtoPOLKADOT.type)
async def process_typeCRS_soltopolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *SOL*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(POLKADOTINRUB) * num)}` *POLKADOT*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSSOLtoPOLKADOT.next()
            await FormCRSSOLtoPOLKADOT.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSSOLtoPOLKADOT.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSSOLtoPOLKADOT.adress)
async def process_adressCRS_soltopolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *SOL*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(POLKADOTINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *SOL*\n*Реквизиты для оплаты:* `{config.walletSolana}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSSOLtoPOLKADOT.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSSOLtoPOLKADOT.comfirm)
async def process_comfirmCRS_soltopolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *SOL*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(POLKADOTINRUB) * num)}` *POLKADOT*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay solana -{num} {user_id}` & `/pay polkadot {'{:0.4f}'.format(float(ex.rubinsol) * float(POLKADOTINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *SOL*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(POLKADOTINRUB) * num)}` *POLKADOT*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay polkadot {'{:0.4f}'.format(float(ex.rubinsol) * float(POLKADOTINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSSOLtoPOLKADOT.comfirm)
async def process_comfirmCRS_soltopolkadot(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *SOL*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(POLKADOTINRUB) * num)}` *POLKADOT*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay solana -{num} {user_id}` & `/pay polkadot {'{:0.4f}'.format(float(ex.rubinsol) * float(POLKADOTINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM SOL TO MATIC = = = = = #
@dp.callback_query_handler(text="call_tocrsmaticSOL")
async def call_crosschain_frsolana_tomatic(call: types.CallbackQuery):
    await FormCRSSOLtoMATIC.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSSOLtoMATIC.number)
async def process_numberCRS_soltomatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[5]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSSOLtoMATIC.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSSOLtoMATIC.type)
async def process_typeCRS_soltomatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *SOL*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(MATICINRUB) * num)}` *MATIC*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSSOLtoMATIC.next()
            await FormCRSSOLtoMATIC.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSSOLtoMATIC.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSSOLtoMATIC.adress)
async def process_adressCRS_soltomatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *SOL*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(MATICINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *SOL*\n*Реквизиты для оплаты:* `{config.walletSolana}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSSOLtoMATIC.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSSOLtoMATIC.comfirm)
async def process_comfirmCRS_soltomatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *SOL*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(MATICINRUB) * num)}` *MATIC*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay solana -{num} {user_id}` & `/pay matic {'{:0.4f}'.format(float(ex.rubinsol) * float(MATICINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *SOL*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(MATICINRUB) * num)}` *MATIC*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay matic {'{:0.4f}'.format(float(ex.rubinsol) * float(MATICINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSSOLtoMATIC.comfirm)
async def process_comfirmCRS_soltomatic(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *SOL*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinsol) * float(MATICINRUB) * num)}` *MATIC*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay solana -{num} {user_id}` & `/pay matic {'{:0.4f}'.format(float(ex.rubinsol) * float(MATICINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = FROM USDT = = = = = = = #
@dp.callback_query_handler(text="call_frcrsusdt")
async def call_crosschain_frusdt(call: types.CallbackQuery):
    await call.message.answer("🪙 Выберите криптовалюту, которую хотите получить:", reply_markup=maincrstoUSDT)
    await call.message.delete()


# = = = = = FROM USDT TO BTC = = = = = #
@dp.callback_query_handler(text="call_tocrsbitcoinUSDT")
async def call_crosschain_frusdt_tobtc(call: types.CallbackQuery):
    await FormCRSUSDTtoBTC.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSUSDTtoBTC.number)
async def process_numberCRS_usdttobtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[6]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSUSDTtoBTC.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSUSDTtoBTC.type)
async def process_typeCRS_usdttobtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *USDT*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(BTCINRUB) * num)}` *BTC*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSUSDTtoBTC.next()
            await FormCRSUSDTtoBTC.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSUSDTtoBTC.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSUSDTtoBTC.adress)
async def process_adressCRS_usdttobtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *USDT*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(BTCINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *USDT*\n*Реквизиты для оплаты:* ERC-20 -`{config.walletUSDT_ERC20}`\nTRC-20 -`{config.walletUSDT_TRC20}`\nPOLYGON -`{config.walletUSDT_POLYGON}`\nBEP-20 -`{config.walletUSDT_BEP20}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSUSDTtoBTC.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSUSDTtoBTC.comfirm)
async def process_comfirmCRS_usdttobtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *USDT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(BTCINRUB) * num)}` *BTC*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay usdt -{num} {user_id}` & `/pay bitcoin {'{:0.4f}'.format(float(ex.rubinusdt) * float(BTCINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *USDT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(BTCINRUB) * num)}` *BTC*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay bitcoin {'{:0.4f}'.format(float(ex.rubinusdt) * float(BTCINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSUSDTtoBTC.comfirm)
async def process_comfirmCRS_usdttobtc(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *USDT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(BTCINRUB) * num)}` *BTC*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay usdt -{num} {user_id}` & `/pay bitcoin {'{:0.4f}'.format(float(ex.rubinusdt) * float(BTCINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM USDT TO ETH = = = = = #
@dp.callback_query_handler(text="call_tocrsethereumUSDT")
async def call_crosschain_frusdt_toeth(call: types.CallbackQuery):
    await FormCRSUSDTtoETH.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSUSDTtoETH.number)
async def process_numberCRS_usdttoeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[6]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSUSDTtoETH.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSUSDTtoETH.type)
async def process_typeCRS_usdttoeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *USDT*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(ETHINRUB) * num)}` *ETH*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSUSDTtoETH.next()
            await FormCRSUSDTtoETH.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSUSDTtoETH.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSUSDTtoETH.adress)
async def process_adressCRS_usdttoeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *USDT*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(ETHINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *USDT*\n*Реквизиты для оплаты:* ERC-20 -`{config.walletUSDT_ERC20}`\nTRC-20 -`{config.walletUSDT_TRC20}`\nPOLYGON -`{config.walletUSDT_POLYGON}`\nBEP-20 -`{config.walletUSDT_BEP20}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSUSDTtoETH.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSUSDTtoETH.comfirm)
async def process_comfirmCRS_usdttoeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *USDT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(ETHINRUB) * num)}` *ETH*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay usdt -{num} {user_id}` & `/pay ethereum {'{:0.4f}'.format(float(ex.rubinusdt) * float(ETHINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *USDT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(ETHINRUB) * num)}` *ETH*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay ethereum {'{:0.4f}'.format(float(ex.rubinusdt) * float(ETHINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSUSDTtoETH.comfirm)
async def process_comfirmCRS_usdttoeth(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *USDT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(ETHINRUB) * num)}` *ETH*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay usdt -{num} {user_id}` & `/pay ethereum {'{:0.4f}'.format(float(ex.rubinusdt) * float(ETHINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM USDT TO SOL = = = = = #
@dp.callback_query_handler(text="call_tocrssolUSDT")
async def call_crosschain_frusdt_tosol(call: types.CallbackQuery):
    await FormCRSUSDTtoSOL.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSUSDTtoSOL.number)
async def process_numberCRS_usdttosol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[6]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSUSDTtoSOL.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSUSDTtoSOL.type)
async def process_typeCRS_usdttosol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *USDT*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(SOLINRUB) * num)}` *SOL*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSUSDTtoSOL.next()
            await FormCRSUSDTtoSOL.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSUSDTtoSOL.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSUSDTtoSOL.adress)
async def process_adressCRS_usdttosol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *USDT*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(SOLINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *USDT*\n*Реквизиты для оплаты:* ERC-20 -`{config.walletUSDT_ERC20}`\nTRC-20 -`{config.walletUSDT_TRC20}`\nPOLYGON -`{config.walletUSDT_POLYGON}`\nBEP-20 -`{config.walletUSDT_BEP20}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSUSDTtoSOL.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSUSDTtoSOL.comfirm)
async def process_comfirmCRS_usdttosol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *USDT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(SOLINRUB) * num)}` *SOL*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay usdt -{num} {user_id}` & `/pay solana {'{:0.4f}'.format(float(ex.rubinusdt) * float(SOLINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *USDT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(SOLINRUB) * num)}` *SOL*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay solana {'{:0.4f}'.format(float(ex.rubinusdt) * float(SOLINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM USDT TO BNB = = = = = #
@dp.callback_query_handler(text="call_tocrsbnbUSDT")
async def call_crosschain_frusdt_tobnb(call: types.CallbackQuery):
    await FormCRSUSDTtoBNB.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSUSDTtoBNB.number)
async def process_numberCRS_usdttobnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[6]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSUSDTtoBNB.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSUSDTtoBNB.type)
async def process_typeCRS_usdttobnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *USDT*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(BNBINRUB) * num)}` *BNB*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSUSDTtoBNB.next()
            await FormCRSUSDTtoBNB.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSUSDTtoBNB.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSUSDTtoBNB.adress)
async def process_adressCRS_usdttobnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *USDT*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(BNBINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *USDT*\n*Реквизиты для оплаты:* ERC-20 -`{config.walletUSDT_ERC20}`\nTRC-20 -`{config.walletUSDT_TRC20}`\nPOLYGON -`{config.walletUSDT_POLYGON}`\nBEP-20 -`{config.walletUSDT_BEP20}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSUSDTtoBNB.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSUSDTtoBNB.comfirm)
async def process_comfirmCRS_usdttobnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *USDT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(BNBINRUB) * num)}` *BNB*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay usdt -{num} {user_id}` & `/pay bnb {'{:0.4f}'.format(float(ex.rubinusdt) * float(BNBINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *USDT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(BNBINRUB) * num)}` *BNB*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay bnb {'{:0.4f}'.format(float(ex.rubinusdt) * float(BNBINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSUSDTtoBNB.comfirm)
async def process_comfirmCRS_usdttobnb(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *USDT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(BNBINRUB) * num)}` *BNB*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay usdt -{num} {user_id}` & `/pay bnb {'{:0.4f}'.format(float(ex.rubinusdt) * float(BNBINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM USDT TO CARDANO = = = = = #
@dp.callback_query_handler(text="call_tocrscardanoUSDT")
async def call_crosschain_frusdt_tocardano(call: types.CallbackQuery):
    await FormCRSUSDTtoCARDANO.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSUSDTtoCARDANO.number)
async def process_numberCRS_usdttocardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[6]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSUSDTtoCARDANO.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSUSDTtoCARDANO.type)
async def process_typeCRS_usdttocardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *USDT*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(CARDANOINRUB) * num)}` *CARDANO*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSUSDTtoCARDANO.next()
            await FormCRSUSDTtoCARDANO.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSUSDTtoCARDANO.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSUSDTtoCARDANO.adress)
async def process_adressCRS_usdttocardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *USDT*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(CARDANOINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *USDT*\n*Реквизиты для оплаты:* ERC-20 -`{config.walletUSDT_ERC20}`\nTRC-20 -`{config.walletUSDT_TRC20}`\nPOLYGON -`{config.walletUSDT_POLYGON}`\nBEP-20 -`{config.walletUSDT_BEP20}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSUSDTtoCARDANO.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSUSDTtoCARDANO.comfirm)
async def process_comfirmCRS_usdttocardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *USDT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(CARDANOINRUB) * num)}` *CARDANO*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay usdt -{num} {user_id}` & `/pay cardano {'{:0.4f}'.format(float(ex.rubinusdt) * float(CARDANOINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *USDT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(CARDANOINRUB) * num)}` *CARDANO*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay cardano {'{:0.4f}'.format(float(ex.rubinusdt) * float(CARDANOINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSUSDTtoCARDANO.comfirm)
async def process_comfirmCRS_usdttocardano(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *USDT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(CARDANOINRUB) * num)}` *CARDANO*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay usdt -{num} {user_id}` & `/pay cardano {'{:0.4f}'.format(float(ex.rubinusdt) * float(CARDANOINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM USDT TO TRON = = = = = #
@dp.callback_query_handler(text="call_tocrstronUSDT")
async def call_crosschain_frusdt_totron(call: types.CallbackQuery):
    await FormCRSUSDTtoTRON.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSUSDTtoTRON.number)
async def process_numberCRS_usdttotron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[6]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSUSDTtoTRON.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSUSDTtoTRON.type)
async def process_typeCRS_usdttotron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *USDT*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(TRONINRUB) * num)}` *TRON*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSUSDTtoTRON.next()
            await FormCRSUSDTtoTRON.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSUSDTtoTRON.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSUSDTtoTRON.adress)
async def process_adressCRS_usdttotron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *USDT*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(TRONINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *USDT*\n*Реквизиты для оплаты:* ERC-20 -`{config.walletUSDT_ERC20}`\nTRC-20 -`{config.walletUSDT_TRC20}`\nPOLYGON -`{config.walletUSDT_POLYGON}`\nBEP-20 -`{config.walletUSDT_BEP20}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSUSDTtoTRON.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSUSDTtoTRON.comfirm)
async def process_comfirmCRS_usdttotron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *USDT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(TRONINRUB) * num)}` *TRON*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay usdt -{num} {user_id}` & `/pay tron {'{:0.4f}'.format(float(ex.rubinusdt) * float(TRONINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *USDT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(TRONINRUB) * num)}` *TRON*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay tron {'{:0.4f}'.format(float(ex.rubinusdt) * float(TRONINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSUSDTtoTRON.comfirm)
async def process_comfirmCRS_usdttotron(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *USDT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(TRONINRUB) * num)}` *TRON*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay usdt -{num} {user_id}` & `/pay tron {'{:0.4f}'.format(float(ex.rubinusdt) * float(TRONINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM USDT TO BUSD = = = = = #
@dp.callback_query_handler(text="call_tocrsbusdUSDT")
async def call_crosschain_frusdt_tobusd(call: types.CallbackQuery):
    await FormCRSUSDTtoBUSD.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSUSDTtoBUSD.number)
async def process_numberCRS_usdttobusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[6]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSUSDTtoBUSD.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSUSDTtoBUSD.type)
async def process_typeCRS_usdttobusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *USDT*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(BUSDINRUB) * num)}` *BUSD*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSUSDTtoBUSD.next()
            await FormCRSUSDTtoBUSD.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSUSDTtoBUSD.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSUSDTtoBUSD.adress)
async def process_adressCRS_usdttobusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *USDT*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(BUSDINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *USDT*\n*Реквизиты для оплаты:* ERC-20 -`{config.walletUSDT_ERC20}`\nTRC-20 -`{config.walletUSDT_TRC20}`\nPOLYGON -`{config.walletUSDT_POLYGON}`\nBEP-20 -`{config.walletUSDT_BEP20}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSUSDTtoBUSD.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSUSDTtoBUSD.comfirm)
async def process_comfirmCRS_usdttobusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *USDT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(BUSDINRUB) * num)}` *BUSD*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay usdt -{num} {user_id}` & `/pay busd {'{:0.4f}'.format(float(ex.rubinusdt) * float(BUSDINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *USDT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(BUSDINRUB) * num)}` *BUSD*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay busd {'{:0.4f}'.format(float(ex.rubinusdt) * float(BUSDINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSUSDTtoBUSD.comfirm)
async def process_comfirmCRS_usdttobusd(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *USDT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(BUSDINRUB) * num)}` *BUSD*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay usdt -{num} {user_id}` & `/pay busd {'{:0.4f}'.format(float(ex.rubinusdt) * float(BUSDINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM USDT TO POLKADOT = = = = = #
@dp.callback_query_handler(text="call_tocrspolkadotUSDT")
async def call_crosschain_frusdt_topolkadot(call: types.CallbackQuery):
    await FormCRSUSDTtoPOLKADOT.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSUSDTtoPOLKADOT.number)
async def process_numberCRS_usdttopolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[6]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSUSDTtoPOLKADOT.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSUSDTtoPOLKADOT.type)
async def process_typeCRS_usdttopolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *USDT*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(POLKADOTINRUB) * num)}` *POLKADOT*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSUSDTtoPOLKADOT.next()
            await FormCRSUSDTtoPOLKADOT.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSUSDTtoPOLKADOT.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSUSDTtoPOLKADOT.adress)
async def process_adressCRS_usdttopolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *USDT*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(POLKADOTINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *USDT*\n*Реквизиты для оплаты:* ERC-20 -`{config.walletUSDT_ERC20}`\nTRC-20 -`{config.walletUSDT_TRC20}`\nPOLYGON -`{config.walletUSDT_POLYGON}`\nBEP-20 -`{config.walletUSDT_BEP20}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSUSDTtoPOLKADOT.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSUSDTtoPOLKADOT.comfirm)
async def process_comfirmCRS_usdttopolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *USDT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(POLKADOTINRUB) * num)}` *POLKADOT*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay usdt -{num} {user_id}` & `/pay polkadot {'{:0.4f}'.format(float(ex.rubinusdt) * float(POLKADOTINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *USDT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(POLKADOTINRUB) * num)}` *POLKADOT*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay polkadot {'{:0.4f}'.format(float(ex.rubinusdt) * float(POLKADOTINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSUSDTtoPOLKADOT.comfirm)
async def process_comfirmCRS_usdttopolkadot(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *USDT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(POLKADOTINRUB) * num)}` *POLKADOT*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay usdt -{num} {user_id}` & `/pay polkadot {'{:0.4f}'.format(float(ex.rubinusdt) * float(POLKADOTINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM USDT TO MATIC = = = = = #
@dp.callback_query_handler(text="call_tocrsmaticUSDT")
async def call_crosschain_frusdt_tomatic(call: types.CallbackQuery):
    await FormCRSUSDTtoMATIC.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSUSDTtoMATIC.number)
async def process_numberCRS_usdttomatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[6]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSUSDTtoMATIC.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSUSDTtoMATIC.type)
async def process_typeCRS_usdttomatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *USDT*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(MATICINRUB) * num)}` *MATIC*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSUSDTtoMATIC.next()
            await FormCRSUSDTtoMATIC.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSUSDTtoMATIC.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSUSDTtoMATIC.adress)
async def process_adressCRS_usdttomatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *USDT*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(MATICINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *USDT*\n*Реквизиты для оплаты:* ERC-20 -`{config.walletUSDT_ERC20}`\nTRC-20 -`{config.walletUSDT_TRC20}`\nPOLYGON -`{config.walletUSDT_POLYGON}`\nBEP-20 -`{config.walletUSDT_BEP20}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSUSDTtoMATIC.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSUSDTtoMATIC.comfirm)
async def process_comfirmCRS_usdttomatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *USDT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(MATICINRUB) * num)}` *MATIC*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay usdt -{num} {user_id}` & `/pay matic {'{:0.4f}'.format(float(ex.rubinusdt) * float(MATICINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *USDT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(MATICINRUB) * num)}` *MATIC*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay matic {'{:0.4f}'.format(float(ex.rubinusdt) * float(MATICINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSUSDTtoMATIC.comfirm)
async def process_comfirmCRS_usdttomatic(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *USDT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinusdt) * float(MATICINRUB) * num)}` *MATIC*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay usdt -{num} {user_id}` & `/pay matic {'{:0.4f}'.format(float(ex.rubinusdt) * float(MATICINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = FROM BNB = = = = = = = #
@dp.callback_query_handler(text="call_frcrsbnb")
async def call_crosschain_frbnb(call: types.CallbackQuery):
    await call.message.answer("🪙 Выберите криптовалюту, которую хотите получить:", reply_markup=maincrstoBNB)
    await call.message.delete()


# = = = = = FROM BNB TO BTC = = = = = #
@dp.callback_query_handler(text="call_tocrsbitcoinBNB")
async def call_crosschain_frbnb_tobtc(call: types.CallbackQuery):
    await FormCRSBNBtoBTC.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSBNBtoBTC.number)
async def process_numberCRS_bnbtobtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[7]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSBNBtoBTC.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSBNBtoBTC.type)
async def process_typeCRS_bnbtobtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *BNB*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(BTCINRUB) * num)}` *BTC*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSBNBtoBTC.next()
            await FormCRSBNBtoBTC.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSBNBtoBTC.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSBNBtoBTC.adress)
async def process_adressCRS_bnbtobtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *BNB*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(BTCINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *BNB*\n*Реквизиты для оплаты:* `{config.walletBNB}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSBNBtoBTC.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSBNBtoBTC.comfirm)
async def process_comfirmCRS_bnbtobtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BNB*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(BTCINRUB) * num)}` *BTC*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay bnb -{num} {user_id}` & `/pay bitcoin {'{:0.4f}'.format(float(ex.rubinbnb) * float(BTCINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BNB*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(BTCINRUB) * num)}` *BTC*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay bitcoin {'{:0.4f}'.format(float(ex.rubinbnb) * float(BTCINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSBNBtoBTC.comfirm)
async def process_comfirmCRS_bnbtobtc(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BNB*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(BTCINRUB) * num)}` *BTC*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay bnb -{num} {user_id}` & `/pay bitcoin {'{:0.4f}'.format(float(ex.rubinbnb) * float(BTCINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM BNB TO ETH = = = = = #
@dp.callback_query_handler(text="call_tocrsethereumBNB")
async def call_crosschain_frbnb_toeth(call: types.CallbackQuery):
    await FormCRSBNBtoETH.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSBNBtoETH.number)
async def process_numberCRS_bnbtoeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[7]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSBNBtoETH.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSBNBtoETH.type)
async def process_typeCRS_bnbtoeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *BNB*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(ETHINRUB) * num)}` *ETH*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSBNBtoETH.next()
            await FormCRSBNBtoETH.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSBNBtoETH.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSBNBtoETH.adress)
async def process_adressCRS_bnbtoeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *BNB*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(ETHINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *BNB*\n*Реквизиты для оплаты:* `{config.walletBNB}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSBNBtoETH.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSBNBtoETH.comfirm)
async def process_comfirmCRS_bnbtoeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BNB*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(ETHINRUB) * num)}` *ETH*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay bnb -{num} {user_id}` & `/pay ethereum {'{:0.4f}'.format(float(ex.rubinbnb) * float(ETHINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BNB*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(ETHINRUB) * num)}` *ETH*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay ethereum {'{:0.4f}'.format(float(ex.rubinbnb) * float(ETHINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSBNBtoETH.comfirm)
async def process_comfirmCRS_bnbtoeth(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BNB*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(ETHINRUB) * num)}` *ETH*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay bnb -{num} {user_id}` & `/pay ethereum {'{:0.4f}'.format(float(ex.rubinbnb) * float(ETHINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM BNB TO SOL = = = = = #
@dp.callback_query_handler(text="call_tocrssolBNB")
async def call_crosschain_frbnb_tosol(call: types.CallbackQuery):
    await FormCRSBNBtoSOL.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSBNBtoSOL.number)
async def process_numberCRS_bnbtosol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[7]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSBNBtoSOL.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSBNBtoSOL.type)
async def process_typeCRS_bnbtosol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *BNB*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(SOLINRUB) * num)}` *SOL*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSBNBtoSOL.next()
            await FormCRSBNBtoSOL.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSBNBtoSOL.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSBNBtoSOL.adress)
async def process_adressCRS_bnbtosol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *BNB*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(SOLINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *BNB*\n*Реквизиты для оплаты:* `{config.walletBNB}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSBNBtoSOL.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSBNBtoSOL.comfirm)
async def process_comfirmCRS_bnbtosol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BNB*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(SOLINRUB) * num)}` *SOL*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay bnb -{num} {user_id}` & `/pay solana {'{:0.4f}'.format(float(ex.rubinbnb) * float(SOLINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BNB*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(SOLINRUB) * num)}` *SOL*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay solana {'{:0.4f}'.format(float(ex.rubinbnb) * float(SOLINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSBNBtoSOL.comfirm)
async def process_comfirmCRS_bnbtosol(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BNB*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(SOLINRUB) * num)}` *SOL*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay bnb -{num} {user_id}` & `/pay solana {'{:0.4f}'.format(float(ex.rubinbnb) * float(SOLINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM BNB TO USDT = = = = = #
@dp.callback_query_handler(text="call_tocrsusdtBNB")
async def call_crosschain_frbnb_tousdt(call: types.CallbackQuery):
    await FormCRSBNBtoUSDT.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSBNBtoUSDT.number)
async def process_numberCRS_bnbtousdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[7]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSBNBtoUSDT.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSBNBtoUSDT.type)
async def process_typeCRS_bnbtousdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *BNB*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(USDTINRUB) * num)}` *USDT*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSBNBtoUSDT.next()
            await FormCRSBNBtoUSDT.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSBNBtoUSDT.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSBNBtoUSDT.adress)
async def process_adressCRS_bnbtousdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *BNB*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(USDTINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *BNB*\n*Реквизиты для оплаты:* `{config.walletBNB}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSBNBtoUSDT.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSBNBtoUSDT.comfirm)
async def process_comfirmCRS_bnbtousdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BNB*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(USDTINRUB) * num)}` *USDT*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay bnb -{num} {user_id}` & `/pay usdt {'{:0.4f}'.format(float(ex.rubinbnb) * float(USDTINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BNB*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(USDTINRUB) * num)}` *USDT*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay usdt {'{:0.4f}'.format(float(ex.rubinbnb) * float(USDTINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSBNBtoUSDT.comfirm)
async def process_comfirmCRS_bnbtousdt(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BNB*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(USDTINRUB) * num)}` *USDT*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay bnb -{num} {user_id}` & `/pay usdt {'{:0.4f}'.format(float(ex.rubinbnb) * float(USDTINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM BNB TO CARDANO = = = = = #
@dp.callback_query_handler(text="call_tocrscardanoBNB")
async def call_crosschain_frbnb_tocardano(call: types.CallbackQuery):
    await FormCRSBNBtoCARDANO.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSBNBtoCARDANO.number)
async def process_numberCRS_bnbtocardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[7]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSBNBtoCARDANO.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSBNBtoCARDANO.type)
async def process_typeCRS_bnbtocardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *BNB*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(CARDANOINRUB) * num)}` *CARDANO*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSBNBtoCARDANO.next()
            await FormCRSBNBtoCARDANO.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSBNBtoCARDANO.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSBNBtoCARDANO.adress)
async def process_adressCRS_bnbtocardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *BNB*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(CARDANOINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *BNB*\n*Реквизиты для оплаты:* `{config.walletBNB}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSBNBtoCARDANO.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSBNBtoCARDANO.comfirm)
async def process_comfirmCRS_bnbtocardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BNB*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(CARDANOINRUB) * num)}` *CARDANO*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay bnb -{num} {user_id}` & `/pay cardano {'{:0.4f}'.format(float(ex.rubinbnb) * float(CARDANOINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BNB*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(CARDANOINRUB) * num)}` *CARDANO*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay cardano {'{:0.4f}'.format(float(ex.rubinbnb) * float(CARDANOINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSBNBtoCARDANO.comfirm)
async def process_comfirmCRS_bnbtocardano(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BNB*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(CARDANOINRUB) * num)}` *CARDANO*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay bnb -{num} {user_id}` & `/pay cardano {'{:0.4f}'.format(float(ex.rubinbnb) * float(CARDANOINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM BNB TO TRON = = = = = #
@dp.callback_query_handler(text="call_tocrstronBNB")
async def call_crosschain_frbnb_totron(call: types.CallbackQuery):
    await FormCRSBNBtoTRON.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSBNBtoTRON.number)
async def process_numberCRS_bnbtotron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[7]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSBNBtoTRON.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSBNBtoTRON.type)
async def process_typeCRS_bnbtotron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *BNB*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(TRONINRUB) * num)}` *TRON*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSBNBtoTRON.next()
            await FormCRSBNBtoTRON.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSBNBtoTRON.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSBNBtoTRON.adress)
async def process_adressCRS_bnbtotron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *BNB*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(TRONINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *BNB*\n*Реквизиты для оплаты:* `{config.walletBNB}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSBNBtoTRON.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSBNBtoTRON.comfirm)
async def process_comfirmCRS_bnbtotron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BNB*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(TRONINRUB) * num)}` *TRON*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay bnb -{num} {user_id}` & `/pay tron {'{:0.4f}'.format(float(ex.rubinbnb) * float(TRONINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BNB*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(TRONINRUB) * num)}` *TRON*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay tron {'{:0.4f}'.format(float(ex.rubinbnb) * float(TRONINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSBNBtoTRON.comfirm)
async def process_comfirmCRS_bnbtotron(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BNB*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(TRONINRUB) * num)}` *TRON*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay bnb -{num} {user_id}` & `/pay tron {'{:0.4f}'.format(float(ex.rubinbnb) * float(TRONINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM BNB TO BUSD = = = = = #
@dp.callback_query_handler(text="call_tocrsbusdBNB")
async def call_crosschain_frbnb_tobusd(call: types.CallbackQuery):
    await FormCRSBNBtoBUSD.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSBNBtoBUSD.number)
async def process_numberCRS_bnbtobusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[7]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSBNBtoBUSD.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSBNBtoBUSD.type)
async def process_typeCRS_bnbtobusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *BNB*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(BUSDINRUB) * num)}` *BUSD*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSBNBtoBUSD.next()
            await FormCRSBNBtoBUSD.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSBNBtoBUSD.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSBNBtoBUSD.adress)
async def process_adressCRS_bnbtobusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *BNB*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(BUSDINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *BNB*\n*Реквизиты для оплаты:* `{config.walletBNB}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSBNBtoBUSD.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSBNBtoBUSD.comfirm)
async def process_comfirmCRS_bnbtobusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BNB*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(BUSDINRUB) * num)}` *BUSD*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay bnb -{num} {user_id}` & `/pay busd {'{:0.4f}'.format(float(ex.rubinbnb) * float(BUSDINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BNB*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(BUSDINRUB) * num)}` *BUSD*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay busd {'{:0.4f}'.format(float(ex.rubinbnb) * float(BUSDINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSBNBtoBUSD.comfirm)
async def process_comfirmCRS_bnbtobusd(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BNB*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(BUSDINRUB) * num)}` *BUSD*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay bnb -{num} {user_id}` & `/pay busd {'{:0.4f}'.format(float(ex.rubinbnb) * float(BUSDINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM BNB TO POLKADOT = = = = = #
@dp.callback_query_handler(text="call_tocrspolkadotBNB")
async def call_crosschain_frbnb_topolkadot(call: types.CallbackQuery):
    await FormCRSBNBtoPOLKADOT.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSBNBtoPOLKADOT.number)
async def process_numberCRS_bnbtopolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[7]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSBNBtoPOLKADOT.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSBNBtoPOLKADOT.type)
async def process_typeCRS_bnbtopolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *BNB*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(POLKADOTINRUB) * num)}` *POLKADOT*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSBNBtoPOLKADOT.next()
            await FormCRSBNBtoPOLKADOT.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSBNBtoPOLKADOT.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSBNBtoPOLKADOT.adress)
async def process_adressCRS_bnbtopolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *BNB*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(POLKADOTINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *BNB*\n*Реквизиты для оплаты:* `{config.walletBNB}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSBNBtoPOLKADOT.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSBNBtoPOLKADOT.comfirm)
async def process_comfirmCRS_bnbtopolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BNB*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(POLKADOTINRUB) * num)}` *POLKADOT*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay bnb -{num} {user_id}` & `/pay polkadot {'{:0.4f}'.format(float(ex.rubinbnb) * float(POLKADOTINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BNB*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(POLKADOTINRUB) * num)}` *POLKADOT*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay polkadot {'{:0.4f}'.format(float(ex.rubinbnb) * float(POLKADOTINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSBNBtoPOLKADOT.comfirm)
async def process_comfirmCRS_bnbtopolkadot(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BNB*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(POLKADOTINRUB) * num)}` *POLKADOT*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay bnb -{num} {user_id}` & `/pay polkadot {'{:0.4f}'.format(float(ex.rubinbnb) * float(POLKADOTINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM BNB TO MATIC = = = = = #
@dp.callback_query_handler(text="call_tocrsmaticBNB")
async def call_crosschain_frbnb_tomatic(call: types.CallbackQuery):
    await FormCRSBNBtoMATIC.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSBNBtoMATIC.number)
async def process_numberCRS_bnbtomatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[7]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSBNBtoMATIC.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSBNBtoMATIC.type)
async def process_typeCRS_bnbtomatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *BNB*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(MATICINRUB) * num)}` *MATIC*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSBNBtoMATIC.next()
            await FormCRSBNBtoMATIC.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSBNBtoMATIC.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSBNBtoMATIC.adress)
async def process_adressCRS_bnbtomatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *BNB*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(MATICINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *BNB*\n*Реквизиты для оплаты:* `{config.walletBNB}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSBNBtoMATIC.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSBNBtoMATIC.comfirm)
async def process_comfirmCRS_bnbtomatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BNB*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(MATICINRUB) * num)}` *MATIC*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay bnb -{num} {user_id}` & `/pay matic {'{:0.4f}'.format(float(ex.rubinbnb) * float(MATICINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BNB*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(MATICINRUB) * num)}` *MATIC*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay matic {'{:0.4f}'.format(float(ex.rubinbnb) * float(MATICINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSBNBtoMATIC.comfirm)
async def process_comfirmCRS_bnbtomatic(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BNB*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbnb) * float(MATICINRUB) * num)}` *MATIC*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay bnb -{num} {user_id}` & `/pay matic {'{:0.4f}'.format(float(ex.rubinbnb) * float(MATICINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = FROM CARDANO = = = = = = = #
@dp.callback_query_handler(text="call_frcrscardano")
async def call_crosschain_frcardano(call: types.CallbackQuery):
    await call.message.answer("🪙 Выберите криптовалюту, которую хотите получить:", reply_markup=maincrstoCARDANO)
    await call.message.delete()


# = = = = = FROM CARDANO TO BTC = = = = = #
@dp.callback_query_handler(text="call_tocrsbtcCARDANO")
async def call_crosschain_frcardano_tobtc(call: types.CallbackQuery):
    await FormCRSCARDANOtoBTC.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSCARDANOtoBTC.number)
async def process_numberCRS_cardanotobtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[8]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSCARDANOtoBTC.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSCARDANOtoBTC.type)
async def process_typeCRS_cardanotobtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *CARDANO*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(BTCINRUB) * num)}` *BTC*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSCARDANOtoBTC.next()
            await FormCRSCARDANOtoBTC.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSCARDANOtoBTC.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSCARDANOtoBTC.adress)
async def process_adressCRS_cardanotobtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *CARDANO*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(BTCINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *CARDANO*\n*Реквизиты для оплаты:* `{config.walletCardano}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSCARDANOtoBTC.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSCARDANOtoBTC.comfirm)
async def process_comfirmCRS_cardanotobtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *CARDANO*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(BTCINRUB) * num)}` *BTC*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay cardano -{num} {user_id}` & `/pay bitcoin {'{:0.4f}'.format(float(ex.rubincardano) * float(BTCINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *CARDANO*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(BTCINRUB) * num)}` *BTC*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay bitcoin {'{:0.4f}'.format(float(ex.rubincardano) * float(BTCINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSCARDANOtoBTC.comfirm)
async def process_comfirmCRS_cardanotobtc(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *CARDANO*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(BTCINRUB) * num)}` *BTC*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay cardano -{num} {user_id}` & `/pay bitcoin {'{:0.4f}'.format(float(ex.rubincardano) * float(BTCINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM CARDANO TO ETH = = = = = #
@dp.callback_query_handler(text="call_tocrsethCARDANO")
async def call_crosschain_frcardano_toeth(call: types.CallbackQuery):
    await FormCRSCARDANOtoETH.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSCARDANOtoETH.number)
async def process_numberCRS_cardanotoeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[8]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSCARDANOtoETH.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSCARDANOtoETH.type)
async def process_typeCRS_cardanotoeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *CARDANO*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(ETHINRUB) * num)}` *ETH*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSCARDANOtoETH.next()
            await FormCRSCARDANOtoETH.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSCARDANOtoETH.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSCARDANOtoETH.adress)
async def process_adressCRS_cardanotoeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *CARDANO*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(ETHINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *CARDANO*\n*Реквизиты для оплаты:* `{config.walletCardano}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSCARDANOtoETH.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSCARDANOtoETH.comfirm)
async def process_comfirmCRS_cardanotoeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *CARDANO*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(ETHINRUB) * num)}` *ETH*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay cardano -{num} {user_id}` & `/pay ethereum {'{:0.4f}'.format(float(ex.rubincardano) * float(ETHINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *CARDANO*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(ETHINRUB) * num)}` *ETH*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay ethereum {'{:0.4f}'.format(float(ex.rubincardano) * float(ETHINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSCARDANOtoETH.comfirm)
async def process_comfirmCRS_cardanotoeth(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *CARDANO*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(ETHINRUB) * num)}` *ETH*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay cardano -{num} {user_id}` & `/pay ethereum {'{:0.4f}'.format(float(ex.rubincardano) * float(ETHINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM CARDANO TO SOL = = = = = #
@dp.callback_query_handler(text="call_tocrssolCARDANO")
async def call_crosschain_frcardano_tosol(call: types.CallbackQuery):
    await FormCRSCARDANOtoSOL.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSCARDANOtoSOL.number)
async def process_numberCRS_cardanotosol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[8]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSCARDANOtoSOL.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSCARDANOtoSOL.type)
async def process_typeCRS_cardanotosol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *CARDANO*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(SOLINRUB) * num)}` *SOL*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSCARDANOtoSOL.next()
            await FormCRSCARDANOtoSOL.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSCARDANOtoSOL.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSCARDANOtoSOL.adress)
async def process_adressCRS_cardanotosol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *CARDANO*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(SOLINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *CARDANO*\n*Реквизиты для оплаты:* `{config.walletCardano}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSCARDANOtoSOL.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSCARDANOtoSOL.comfirm)
async def process_comfirmCRS_cardanotosol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *CARDANO*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(SOLINRUB) * num)}` *SOL*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay cardano -{num} {user_id}` & `/pay sol {'{:0.4f}'.format(float(ex.rubincardano) * float(SOLINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *CARDANO*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(SOLINRUB) * num)}` *SOL*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay sol {'{:0.4f}'.format(float(ex.rubincardano) * float(SOLINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSCARDANOtoSOL.comfirm)
async def process_comfirmCRS_cardanotosol(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *CARDANO*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(SOLINRUB) * num)}` *SOL*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay cardano -{num} {user_id}` & `/pay sol {'{:0.4f}'.format(float(ex.rubincardano) * float(SOLINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM CARDANO TO USDT = = = = = #
@dp.callback_query_handler(text="call_tocrsusdtCARDANO")
async def call_crosschain_frcardano_tousdt(call: types.CallbackQuery):
    await FormCRSCARDANOtoUSDT.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSCARDANOtoUSDT.number)
async def process_numberCRS_cardanotousdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[8]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSCARDANOtoUSDT.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSCARDANOtoUSDT.type)
async def process_typeCRS_cardanotousdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *CARDANO*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(USDTINRUB) * num)}` *USDT*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSCARDANOtoUSDT.next()
            await FormCRSCARDANOtoUSDT.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSCARDANOtoUSDT.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSCARDANOtoUSDT.adress)
async def process_adressCRS_cardanotousdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *CARDANO*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(USDTINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *CARDANO*\n*Реквизиты для оплаты:* `{config.walletCardano}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSCARDANOtoUSDT.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSCARDANOtoUSDT.comfirm)
async def process_comfirmCRS_cardanotousdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *CARDANO*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(USDTINRUB) * num)}` *USDT*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay cardano -{num} {user_id}` & `/pay usdt {'{:0.4f}'.format(float(ex.rubincardano) * float(USDTINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *CARDANO*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(USDTINRUB) * num)}` *USDT*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay usdt {'{:0.4f}'.format(float(ex.rubincardano) * float(USDTINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSCARDANOtoUSDT.comfirm)
async def process_comfirmCRS_cardanotousdt(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *CARDANO*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(USDTINRUB) * num)}` *USDT*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay cardano -{num} {user_id}` & `/pay usdt {'{:0.4f}'.format(float(ex.rubincardano) * float(USDTINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM CARDANO TO BNB = = = = = #
@dp.callback_query_handler(text="call_tocrsbnbCARDANO")
async def call_crosschain_frcardano_tobnb(call: types.CallbackQuery):
    await FormCRSCARDANOtoBNB.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSCARDANOtoBNB.number)
async def process_numberCRS_cardanotobnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[8]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSCARDANOtoBNB.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSCARDANOtoBNB.type)
async def process_typeCRS_cardanotobnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *CARDANO*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(BNBINRUB) * num)}` *BNB*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSCARDANOtoBNB.next()
            await FormCRSCARDANOtoBNB.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSCARDANOtoBNB.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSCARDANOtoBNB.adress)
async def process_adressCRS_cardanotobnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *CARDANO*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(BNBINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *CARDANO*\n*Реквизиты для оплаты:* `{config.walletCardano}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSCARDANOtoBNB.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSCARDANOtoBNB.comfirm)
async def process_comfirmCRS_cardanotobnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *CARDANO*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(BNBINRUB) * num)}` *BNB*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay cardano -{num} {user_id}` & `/pay bnb {'{:0.4f}'.format(float(ex.rubincardano) * float(BNBINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *CARDANO*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(BNBINRUB) * num)}` *BNB*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay bnb {'{:0.4f}'.format(float(ex.rubincardano) * float(BNBINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSCARDANOtoBNB.comfirm)
async def process_comfirmCRS_cardanotobnb(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *CARDANO*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(BNBINRUB) * num)}` *BNB*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay cardano -{num} {user_id}` & `/pay bnb {'{:0.4f}'.format(float(ex.rubincardano) * float(BNBINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM CARDANO TO TRON = = = = = #
@dp.callback_query_handler(text="call_tocrstronCARDANO")
async def call_crosschain_frcardano_totron(call: types.CallbackQuery):
    await FormCRSCARDANOtoTRON.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSCARDANOtoTRON.number)
async def process_numberCRS_cardanototron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[8]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSCARDANOtoTRON.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSCARDANOtoTRON.type)
async def process_typeCRS_cardanototron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *CARDANO*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(TRONINRUB) * num)}` *TRON*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSCARDANOtoTRON.next()
            await FormCRSCARDANOtoTRON.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSCARDANOtoTRON.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSCARDANOtoTRON.adress)
async def process_adressCRS_cardanototron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *CARDANO*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(TRONINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *CARDANO*\n*Реквизиты для оплаты:* `{config.walletCardano}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSCARDANOtoTRON.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSCARDANOtoTRON.comfirm)
async def process_comfirmCRS_cardanototron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *CARDANO*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(TRONINRUB) * num)}` *TRON*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay cardano -{num} {user_id}` & `/pay tron {'{:0.4f}'.format(float(ex.rubincardano) * float(TRONINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *CARDANO*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(TRONINRUB) * num)}` *TRON*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay tron {'{:0.4f}'.format(float(ex.rubincardano) * float(TRONINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSCARDANOtoTRON.comfirm)
async def process_comfirmCRS_cardanototron(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *CARDANO*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(TRONINRUB) * num)}` *TRON*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay cardano -{num} {user_id}` & `/pay tron {'{:0.4f}'.format(float(ex.rubincardano) * float(TRONINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM CARDANO TO BUSD = = = = = #
@dp.callback_query_handler(text="call_tocrsbusdCARDANO")
async def call_crosschain_frcardano_tobusd(call: types.CallbackQuery):
    await FormCRSCARDANOtoBUSD.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSCARDANOtoBUSD.number)
async def process_numberCRS_cardanotobusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[8]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSCARDANOtoBUSD.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSCARDANOtoBUSD.type)
async def process_typeCRS_cardanotobusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *CARDANO*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(BUSDINRUB) * num)}` *BUSD*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSCARDANOtoBUSD.next()
            await FormCRSCARDANOtoBUSD.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSCARDANOtoBUSD.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSCARDANOtoBUSD.adress)
async def process_adressCRS_cardanotobusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *CARDANO*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(BUSDINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *CARDANO*\n*Реквизиты для оплаты:* `{config.walletCardano}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSCARDANOtoBUSD.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSCARDANOtoBUSD.comfirm)
async def process_comfirmCRS_cardanotobusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *CARDANO*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(BUSDINRUB) * num)}` *BUSD*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay cardano -{num} {user_id}` & `/pay busd {'{:0.4f}'.format(float(ex.rubincardano) * float(BUSDINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *CARDANO*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(BUSDINRUB) * num)}` *BUSD*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay busd {'{:0.4f}'.format(float(ex.rubincardano) * float(BUSDINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSCARDANOtoBUSD.comfirm)
async def process_comfirmCRS_cardanotobusd(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *CARDANO*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(BUSDINRUB) * num)}` *BUSD*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay cardano -{num} {user_id}` & `/pay busd {'{:0.4f}'.format(float(ex.rubincardano) * float(BUSDINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM CARDANO TO POLKADOT = = = = = #
@dp.callback_query_handler(text="call_tocrspolkadotCARDANO")
async def call_crosschain_frcardano_topolkadot(call: types.CallbackQuery):
    await FormCRSCARDANOtoPOLKADOT.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSCARDANOtoPOLKADOT.number)
async def process_numberCRS_cardanotopolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[8]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSCARDANOtoPOLKADOT.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSCARDANOtoPOLKADOT.type)
async def process_typeCRS_cardanotopolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *CARDANO*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(POLKADOTINRUB) * num)}` *POLKADOT*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSCARDANOtoPOLKADOT.next()
            await FormCRSCARDANOtoPOLKADOT.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSCARDANOtoPOLKADOT.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSCARDANOtoPOLKADOT.adress)
async def process_adressCRS_cardanotopolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *CARDANO*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(POLKADOTINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *CARDANO*\n*Реквизиты для оплаты:* `{config.walletCardano}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSCARDANOtoPOLKADOT.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSCARDANOtoPOLKADOT.comfirm)
async def process_comfirmCRS_cardanotopolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *CARDANO*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(POLKADOTINRUB) * num)}` *POLKADOT*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay cardano -{num} {user_id}` & `/pay polkadot {'{:0.4f}'.format(float(ex.rubincardano) * float(POLKADOTINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *CARDANO*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(POLKADOTINRUB) * num)}` *POLKADOT*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay polkadot {'{:0.4f}'.format(float(ex.rubincardano) * float(POLKADOTINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSCARDANOtoPOLKADOT.comfirm)
async def process_comfirmCRS_cardanotopolkadot(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *CARDANO*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(POLKADOTINRUB) * num)}` *POLKADOT*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay cardano -{num} {user_id}` & `/pay polkadot {'{:0.4f}'.format(float(ex.rubincardano) * float(POLKADOTINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM CARDANO TO MATIC = = = = = #
@dp.callback_query_handler(text="call_tocrsmaticCARDANO")
async def call_crosschain_frcardano_tomatic(call: types.CallbackQuery):
    await FormCRSCARDANOtoMATIC.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSCARDANOtoMATIC.number)
async def process_numberCRS_cardanotomatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[8]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSCARDANOtoMATIC.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSCARDANOtoMATIC.type)
async def process_typeCRS_cardanotomatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *CARDANO*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(MATICINRUB) * num)}` *MATIC*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSCARDANOtoMATIC.next()
            await FormCRSCARDANOtoMATIC.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSCARDANOtoMATIC.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSCARDANOtoMATIC.adress)
async def process_adressCRS_cardanotomatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *CARDANO*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(MATICINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *CARDANO*\n*Реквизиты для оплаты:* `{config.walletCardano}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSCARDANOtoMATIC.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSCARDANOtoMATIC.comfirm)
async def process_comfirmCRS_cardanotomatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *CARDANO*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(MATICINRUB) * num)}` *MATIC*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay cardano -{num} {user_id}` & `/pay matic {'{:0.4f}'.format(float(ex.rubincardano) * float(MATICINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *CARDANO*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubincardano) * float(MATICINRUB) * num)}` *MATIC*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay matic {'{:0.4f}'.format(float(ex.rubincardano) * float(MATICINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = FROM TRON = = = = = = = #
@dp.callback_query_handler(text="call_frcrstron")
async def call_crosschain_frtron(call: types.CallbackQuery):
    await call.message.answer("🪙 Выберите криптовалюту, которую хотите получить:", reply_markup=maincrstoTRON)
    await call.message.delete()


# = = = = = FROM TRON TO BTC = = = = = #
@dp.callback_query_handler(text="call_tocrsbitcoinTRON")
async def call_crosschain_frtron_tobitcoin(call: types.CallbackQuery):
    await FormCRSTRONtoBTC.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSTRONtoBTC.number)
async def process_numberCRS_trontobtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[9]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSTRONtoBTC.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSTRONtoBTC.type)
async def process_typeCRS_trontobtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *TRON*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubintron) * float(BTCINRUB) * num)}` *BTC*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSTRONtoBTC.next()
            await FormCRSTRONtoBTC.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSTRONtoBTC.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSTRONtoBTC.adress)
async def process_adressCRS_trontobtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *TRON*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubintron) * float(BTCINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *TRON*\n*Реквизиты для оплаты:* `{config.walletTron}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSTRONtoBTC.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSTRONtoBTC.comfirm)
async def process_comfirmCRS_trontobtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *TRON*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubintron) * float(BTCINRUB) * num)}` *BTC*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay tron -{num} {user_id}` & `/pay bitcoin {'{:0.4f}'.format(float(ex.rubintron) * float(BTCINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *TRON*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubintron) * float(BTCINRUB) * num)}` *BTC*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay bitcoin {'{:0.4f}'.format(float(ex.rubintron) * float(BTCINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSTRONtoBTC.comfirm)
async def process_comfirmCRS_trontobtc(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *TRON*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubintron) * float(BTCINRUB) * num)}` *BTC*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay tron -{num} {user_id}` & `/pay bitcoin {'{:0.4f}'.format(float(ex.rubintron) * float(BTCINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM TRON TO ETH = = = = = #
@dp.callback_query_handler(text="call_tocrsethereumTRON")
async def call_crosschain_frtron_toethereum(call: types.CallbackQuery):
    await FormCRSTRONtoETH.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSTRONtoETH.number)
async def process_numberCRS_trontoeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[9]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSTRONtoETH.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSTRONtoETH.type)
async def process_typeCRS_trontoeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *TRON*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubintron) * float(ETHINRUB) * num)}` *ETH*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSTRONtoETH.next()
            await FormCRSTRONtoETH.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSTRONtoETH.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSTRONtoETH.adress)
async def process_adressCRS_trontoeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *TRON*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubintron) * float(ETHINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *TRON*\n*Реквизиты для оплаты:* `{config.walletTron}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSTRONtoETH.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSTRONtoETH.comfirm)
async def process_comfirmCRS_trontoeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *TRON*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubintron) * float(ETHINRUB) * num)}` *ETH*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay tron -{num} {user_id}` & `/pay ethereum {'{:0.4f}'.format(float(ex.rubintron) * float(ETHINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *TRON*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubintron) * float(ETHINRUB) * num)}` *ETH*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay ethereum {'{:0.4f}'.format(float(ex.rubintron) * float(ETHINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSTRONtoETH.comfirm)
async def process_comfirmCRS_trontoeth(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *TRON*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubintron) * float(ETHINRUB) * num)}` *ETH*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay tron -{num} {user_id}` & `/pay ethereum {'{:0.4f}'.format(float(ex.rubintron) * float(ETHINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM TRON TO SOL = = = = = #
@dp.callback_query_handler(text="call_tocrssolTRON")
async def call_crosschain_frtron_tosol(call: types.CallbackQuery):
    await FormCRSTRONtoSOL.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSTRONtoSOL.number)
async def process_numberCRS_trontosol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[9]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSTRONtoSOL.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSTRONtoSOL.type)
async def process_typeCRS_trontosol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *TRON*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubintron) * float(SOLINRUB) * num)}` *SOL*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSTRONtoSOL.next()
            await FormCRSTRONtoSOL.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSTRONtoSOL.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSTRONtoSOL.adress)
async def process_adressCRS_trontosol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *TRON*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubintron) * float(SOLINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *TRON*\n*Реквизиты для оплаты:* `{config.walletTron}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSTRONtoSOL.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSTRONtoSOL.comfirm)
async def process_comfirmCRS_trontosol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *TRON*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubintron) * float(SOLINRUB) * num)}` *SOL*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay tron -{num} {user_id}` & `/pay sol {'{:0.4f}'.format(float(ex.rubintron) * float(SOLINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *TRON*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubintron) * float(SOLINRUB) * num)}` *SOL*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay sol {'{:0.4f}'.format(float(ex.rubintron) * float(SOLINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSTRONtoSOL.comfirm)
async def process_comfirmCRS_trontosol(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *TRON*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubintron) * float(SOLINRUB) * num)}` *SOL*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay tron -{num} {user_id}` & `/pay sol {'{:0.4f}'.format(float(ex.rubintron) * float(SOLINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM TRON TO USDT = = = = = #
@dp.callback_query_handler(text="call_tocrsusdtTRON")
async def call_crosschain_frtron_tousdt(call: types.CallbackQuery):
    await FormCRSTRONtoUSDT.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSTRONtoUSDT.number)
async def process_numberCRS_trontousdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[9]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSTRONtoUSDT.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSTRONtoUSDT.type)
async def process_typeCRS_trontousdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *TRON*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubintron) * float(USDTINRUB) * num)}` *USDT*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSTRONtoUSDT.next()
            await FormCRSTRONtoUSDT.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSTRONtoUSDT.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSTRONtoUSDT.adress)
async def process_adressCRS_trontousdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *TRON*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubintron) * float(USDTINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *TRON*\n*Реквизиты для оплаты:* `{config.walletTron}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSTRONtoUSDT.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSTRONtoUSDT.comfirm)
async def process_comfirmCRS_trontousdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *TRON*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubintron) * float(USDTINRUB) * num)}` *USDT*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay tron -{num} {user_id}` & `/pay usdt {'{:0.4f}'.format(float(ex.rubintron) * float(USDTINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *TRON*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubintron) * float(USDTINRUB) * num)}` *USDT*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay usdt {'{:0.4f}'.format(float(ex.rubintron) * float(USDTINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSTRONtoUSDT.comfirm)
async def process_comfirmCRS_trontousdt(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *TRON*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubintron) * float(USDTINRUB) * num)}` *USDT*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay tron -{num} {user_id}` & `/pay usdt {'{:0.4f}'.format(float(ex.rubintron) * float(USDTINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM TRON TO BNB = = = = = #
@dp.callback_query_handler(text="call_tocrsbnbTRON")
async def call_crosschain_frtron_tobnb(call: types.CallbackQuery):
    await FormCRSTRONtoBNB.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSTRONtoBNB.number)
async def process_numberCRS_trontobnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[9]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSTRONtoBNB.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSTRONtoBNB.type)
async def process_typeCRS_trontobnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *TRON*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubintron) * float(BNBINRUB) * num)}` *BNB*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSTRONtoBNB.next()
            await FormCRSTRONtoBNB.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSTRONtoBNB.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSTRONtoBNB.adress)
async def process_adressCRS_trontobnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *TRON*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubintron) * float(BNBINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *TRON*\n*Реквизиты для оплаты:* `{config.walletTron}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSTRONtoBNB.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSTRONtoBNB.comfirm)
async def process_comfirmCRS_trontobnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *TRON*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubintron) * float(BNBINRUB) * num)}` *BNB*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay tron -{num} {user_id}` & `/pay bnb {'{:0.4f}'.format(float(ex.rubintron) * float(BNBINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *TRON*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubintron) * float(BNBINRUB) * num)}` *BNB*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay bnb {'{:0.4f}'.format(float(ex.rubintron) * float(BNBINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSTRONtoBNB.comfirm)
async def process_comfirmCRS_trontobnb(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *TRON*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubintron) * float(BNBINRUB) * num)}` *BNB*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay tron -{num} {user_id}` & `/pay bnb {'{:0.4f}'.format(float(ex.rubintron) * float(BNBINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM TRON TO CARDANO = = = = = #
@dp.callback_query_handler(text="call_tocrscardanoTRON")
async def call_crosschain_frtron_tocardano(call: types.CallbackQuery):
    await FormCRSTRONtoCARDANO.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSTRONtoCARDANO.number)
async def process_numberCRS_trontocardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[9]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSTRONtoCARDANO.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSTRONtoCARDANO.type)
async def process_typeCRS_trontocardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *TRON*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubintron) * float(CARDANOINRUB) * num)}` *CARDANO*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSTRONtoCARDANO.next()
            await FormCRSTRONtoCARDANO.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSTRONtoCARDANO.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSTRONtoCARDANO.adress)
async def process_adressCRS_trontocardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *TRON*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubintron) * float(CARDANOINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *TRON*\n*Реквизиты для оплаты:* `{config.walletTron}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSTRONtoCARDANO.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSTRONtoCARDANO.comfirm)
async def process_comfirmCRS_trontocardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *TRON*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubintron) * float(CARDANOINRUB) * num)}` *CARDANO*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay tron -{num} {user_id}` & `/pay cardano {'{:0.4f}'.format(float(ex.rubintron) * float(CARDANOINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *TRON*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubintron) * float(CARDANOINRUB) * num)}` *CARDANO*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay cardano {'{:0.4f}'.format(float(ex.rubintron) * float(CARDANOINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSTRONtoCARDANO.comfirm)
async def process_comfirmCRS_trontocardano(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *TRON*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubintron) * float(CARDANOINRUB) * num)}` *CARDANO*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay tron -{num} {user_id}` & `/pay cardano {'{:0.4f}'.format(float(ex.rubintron) * float(CARDANOINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM TRON TO BUSD = = = = = #
@dp.callback_query_handler(text="call_tocrsbusdTRON")
async def call_crosschain_frtron_tobusd(call: types.CallbackQuery):
    await FormCRSTRONtoBUSD.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSTRONtoBUSD.number)
async def process_numberCRS_trontobusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[9]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSTRONtoBUSD.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSTRONtoBUSD.type)
async def process_typeCRS_trontobusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *TRON*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubintron) * float(BUSDINRUB) * num)}` *BUSD*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSTRONtoBUSD.next()
            await FormCRSTRONtoBUSD.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSTRONtoBUSD.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSTRONtoBUSD.adress)
async def process_adressCRS_trontobusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *TRON*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubintron) * float(BUSDINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *TRON*\n*Реквизиты для оплаты:* `{config.walletTron}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSTRONtoBUSD.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSTRONtoBUSD.comfirm)
async def process_comfirmCRS_trontobusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *TRON*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubintron) * float(BUSDINRUB) * num)}` *BUSD*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay tron -{num} {user_id}` & `/pay busd {'{:0.4f}'.format(float(ex.rubintron) * float(BUSDINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *TRON*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubintron) * float(BUSDINRUB) * num)}` *BUSD*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay busd {'{:0.4f}'.format(float(ex.rubintron) * float(BUSDINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSTRONtoBUSD.comfirm)
async def process_comfirmCRS_trontobusd(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *TRON*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubintron) * float(BUSDINRUB) * num)}` *BUSD*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay tron -{num} {user_id}` & `/pay busd {'{:0.4f}'.format(float(ex.rubintron) * float(BUSDINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM TRON TO POLKADOT = = = = = #
@dp.callback_query_handler(text="call_tocrspolkadotTRON")
async def call_crosschain_frtron_topolkadot(call: types.CallbackQuery):
    await FormCRSTRONtoPOLKADOT.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSTRONtoPOLKADOT.number)
async def process_numberCRS_trontopolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[9]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSTRONtoPOLKADOT.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSTRONtoPOLKADOT.type)
async def process_typeCRS_trontopolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *TRON*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubintron) * float(POLKADOTINRUB) * num)}` *POLKADOT*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSTRONtoPOLKADOT.next()
            await FormCRSTRONtoPOLKADOT.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSTRONtoPOLKADOT.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSTRONtoPOLKADOT.adress)
async def process_adressCRS_trontopolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *TRON*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubintron) * float(POLKADOTINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *TRON*\n*Реквизиты для оплаты:* `{config.walletTron}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSTRONtoPOLKADOT.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSTRONtoPOLKADOT.comfirm)
async def process_comfirmCRS_trontopolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *TRON*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubintron) * float(POLKADOTINRUB) * num)}` *POLKADOT*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay tron -{num} {user_id}` & `/pay polkadot {'{:0.4f}'.format(float(ex.rubintron) * float(POLKADOTINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *TRON*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubintron) * float(POLKADOTINRUB) * num)}` *POLKADOT*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay polkadot {'{:0.4f}'.format(float(ex.rubintron) * float(POLKADOTINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSTRONtoPOLKADOT.comfirm)
async def process_comfirmCRS_trontopolkadot(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *TRON*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubintron) * float(POLKADOTINRUB) * num)}` *POLKADOT*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay tron -{num} {user_id}` & `/pay polkadot {'{:0.4f}'.format(float(ex.rubintron) * float(POLKADOTINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM TRON TO MATIC = = = = = #
@dp.callback_query_handler(text="call_tocrsmaticTRON")
async def call_crosschain_frtron_tomatic(call: types.CallbackQuery):
    await FormCRSTRONtoMATIC.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSTRONtoMATIC.number)
async def process_numberCRS_trontomatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[9]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSTRONtoMATIC.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSTRONtoMATIC.type)
async def process_typeCRS_trontomatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *TRON*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubintron) * float(MATICINRUB) * num)}` *MATIC*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSTRONtoMATIC.next()
            await FormCRSTRONtoMATIC.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSTRONtoMATIC.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSTRONtoMATIC.adress)
async def process_adressCRS_trontomatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *TRON*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubintron) * float(MATICINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *TRON*\n*Реквизиты для оплаты:* `{config.walletTron}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSTRONtoMATIC.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSTRONtoMATIC.comfirm)
async def process_comfirmCRS_trontomatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *TRON*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubintron) * float(MATICINRUB) * num)}` *MATIC*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay tron -{num} {user_id}` & `/pay matic {'{:0.4f}'.format(float(ex.rubintron) * float(MATICINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *TRON*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubintron) * float(MATICINRUB) * num)}` *MATIC*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay matic {'{:0.4f}'.format(float(ex.rubintron) * float(MATICINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSTRONtoMATIC.comfirm)
async def process_comfirmCRS_trontomatic(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *TRON*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubintron) * float(MATICINRUB) * num)}` *MATIC*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay tron -{num} {user_id}` & `/pay matic {'{:0.4f}'.format(float(ex.rubintron) * float(MATICINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = FROM BUSD = = = = = = = #
@dp.callback_query_handler(text="call_frcrsbusd")
async def call_crosschain_frbusd(call: types.CallbackQuery):
    await call.message.answer("🪙 Выберите криптовалюту, которую хотите получить:", reply_markup=maincrstoBUSD)
    await call.message.delete()


# = = = = = FROM BUSD TO BTC = = = = = #
@dp.callback_query_handler(text="call_tocrsbitcoinBUSD")
async def call_crosschain_frbusd_tobtc(call: types.CallbackQuery):
    await FormCRSBUSDtoBTC.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSBUSDtoBTC.number)
async def process_numberCRS_busdtobtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[10]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSBUSDtoBTC.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSBUSDtoBTC.type)
async def process_typeCRS_busdtobtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *BUSD*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinbusd) * float(BTCINRUB) * num)}` *BTC*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSBUSDtoBTC.next()
            await FormCRSBUSDtoBTC.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSBUSDtoBTC.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSBUSDtoBTC.adress)
async def process_adressCRS_busdtobtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *BUSD*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinbusd) * float(BTCINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *BUSD*\n*Реквизиты для оплаты:* ERC-20 -`{config.walletBUSD_ERC20}`\nBEP-20 -`{config.walletBUSD_BEP20}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSBUSDtoBTC.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSBUSDtoBTC.comfirm)
async def process_comfirmCRS_busdtobtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BUSD*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbusd) * float(BTCINRUB) * num)}` *BTC*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay busd -{num} {user_id}` & `/pay bitcoin {'{:0.4f}'.format(float(ex.rubinbusd) * float(BTCINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BUSD*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbusd) * float(BTCINRUB) * num)}` *BTC*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay bitcoin {'{:0.4f}'.format(float(ex.rubinbusd) * float(BTCINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSBUSDtoBTC.comfirm)
async def process_comfirmCRS_busdtobtc(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BUSD*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbusd) * float(BTCINRUB) * num)}` *BTC*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay busd -{num} {user_id}` & `/pay bitcoin {'{:0.4f}'.format(float(ex.rubinbusd) * float(BTCINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM BUSD TO ETH = = = = = #
@dp.callback_query_handler(text="call_tocrsethereumBUSD")
async def call_crosschain_frbusd_toeth(call: types.CallbackQuery):
    await FormCRSBUSDtoETH.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSBUSDtoETH.number)
async def process_numberCRS_busdtoeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[10]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSBUSDtoETH.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSBUSDtoETH.type)
async def process_typeCRS_busdtoeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *BUSD*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinbusd) * float(ETHINRUB) * num)}` *ETH*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSBUSDtoETH.next()
            await FormCRSBUSDtoETH.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSBUSDtoETH.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSBUSDtoETH.adress)
async def process_adressCRS_busdtoeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *BUSD*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinbusd) * float(ETHINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *BUSD*\n*Реквизиты для оплаты:* ERC-20 -`{config.walletBUSD_ERC20}`\nBEP-20 -`{config.walletBUSD_BEP20}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSBUSDtoETH.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSBUSDtoETH.comfirm)
async def process_comfirmCRS_busdtoeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BUSD*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbusd) * float(ETHINRUB) * num)}` *ETH*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay busd -{num} {user_id}` & `/pay ethereum {'{:0.4f}'.format(float(ex.rubinbusd) * float(ETHINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BUSD*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbusd) * float(ETHINRUB) * num)}` *ETH*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay ethereum {'{:0.4f}'.format(float(ex.rubinbusd) * float(ETHINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSBUSDtoETH.comfirm)
async def process_comfirmCRS_busdtoeth(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BUSD*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbusd) * float(ETHINRUB) * num)}` *ETH*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay busd -{num} {user_id}` & `/pay ethereum {'{:0.4f}'.format(float(ex.rubinbusd) * float(ETHINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM BUSD TO SOL = = = = = #
@dp.callback_query_handler(text="call_tocrssolBUSD")
async def call_crosschain_frbusd_tosol(call: types.CallbackQuery):
    await FormCRSBUSDtoSOL.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSBUSDtoSOL.number)
async def process_numberCRS_busdtosol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[10]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSBUSDtoSOL.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSBUSDtoSOL.type)
async def process_typeCRS_busdtosol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *BUSD*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinbusd) * float(SOLINRUB) * num)}` *SOL*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSBUSDtoSOL.next()
            await FormCRSBUSDtoSOL.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSBUSDtoSOL.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSBUSDtoSOL.adress)
async def process_adressCRS_busdtosol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *BUSD*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinbusd) * float(SOLINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *BUSD*\n*Реквизиты для оплаты:* ERC-20 -`{config.walletBUSD_ERC20}`\nBEP-20 -`{config.walletBUSD_BEP20}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSBUSDtoSOL.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSBUSDtoSOL.comfirm)
async def process_comfirmCRS_busdtosol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BUSD*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbusd) * float(SOLINRUB) * num)}` *SOL*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay busd -{num} {user_id}` & `/pay sol {'{:0.4f}'.format(float(ex.rubinbusd) * float(SOLINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BUSD*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbusd) * float(SOLINRUB) * num)}` *SOL*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay sol {'{:0.4f}'.format(float(ex.rubinbusd) * float(SOLINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSBUSDtoSOL.comfirm)
async def process_comfirmCRS_busdtosol(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BUSD*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbusd) * float(SOLINRUB) * num)}` *SOL*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay busd -{num} {user_id}` & `/pay sol {'{:0.4f}'.format(float(ex.rubinbusd) * float(SOLINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM BUSD TO USDT = = = = = #
@dp.callback_query_handler(text="call_tocrsusdtBUSD")
async def call_crosschain_frbusd_tousdt(call: types.CallbackQuery):
    await FormCRSBUSDtoUSDT.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSBUSDtoUSDT.number)
async def process_numberCRS_busdtousdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[10]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSBUSDtoUSDT.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSBUSDtoUSDT.type)
async def process_typeCRS_busdtousdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *BUSD*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinbusd) * float(USDTINRUB) * num)}` *USDT*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSBUSDtoUSDT.next()
            await FormCRSBUSDtoUSDT.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSBUSDtoUSDT.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSBUSDtoUSDT.adress)
async def process_adressCRS_busdtousdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *BUSD*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinbusd) * float(USDTINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *BUSD*\n*Реквизиты для оплаты:* ERC-20 -`{config.walletBUSD_ERC20}`\nBEP-20 -`{config.walletBUSD_BEP20}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSBUSDtoUSDT.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSBUSDtoUSDT.comfirm)
async def process_comfirmCRS_busdtousdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BUSD*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbusd) * float(USDTINRUB) * num)}` *USDT*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay busd -{num} {user_id}` & `/pay usdt {'{:0.4f}'.format(float(ex.rubinbusd) * float(USDTINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BUSD*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbusd) * float(USDTINRUB) * num)}` *USDT*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay usdt {'{:0.4f}'.format(float(ex.rubinbusd) * float(USDTINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSBUSDtoUSDT.comfirm)
async def process_comfirmCRS_busdtousdt(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BUSD*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbusd) * float(USDTINRUB) * num)}` *USDT*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay busd -{num} {user_id}` & `/pay usdt {'{:0.4f}'.format(float(ex.rubinbusd) * float(USDTINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM BUSD TO BNB = = = = = #
@dp.callback_query_handler(text="call_tocrsbnbBUSD")
async def call_crosschain_frbusd_tobnb(call: types.CallbackQuery):
    await FormCRSBUSDtoBNB.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSBUSDtoBNB.number)
async def process_numberCRS_busdtobnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[10]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSBUSDtoBNB.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSBUSDtoBNB.type)
async def process_typeCRS_busdtobnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *BUSD*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinbusd) * float(BNBINRUB) * num)}` *BNB*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSBUSDtoBNB.next()
            await FormCRSBUSDtoBNB.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSBUSDtoBNB.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSBUSDtoBNB.adress)
async def process_adressCRS_busdtobnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *BUSD*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinbusd) * float(BNBINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *BUSD*\n*Реквизиты для оплаты:* ERC-20 -`{config.walletBUSD_ERC20}`\nBEP-20 -`{config.walletBUSD_BEP20}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSBUSDtoBNB.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSBUSDtoBNB.comfirm)
async def process_comfirmCRS_busdtobnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BUSD*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbusd) * float(BNBINRUB) * num)}` *BNB*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay busd -{num} {user_id}` & `/pay bnb {'{:0.4f}'.format(float(ex.rubinbusd) * float(BNBINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BUSD*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbusd) * float(BNBINRUB) * num)}` *BNB*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay bnb {'{:0.4f}'.format(float(ex.rubinbusd) * float(BNBINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM BUSD TO CARDANO = = = = = #
@dp.callback_query_handler(text="call_tocrscardanoBUSD")
async def call_crosschain_frbusd_tocardano(call: types.CallbackQuery):
    await FormCRSBUSDtoCARDANO.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSBUSDtoCARDANO.number)
async def process_numberCRS_busdtocardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[10]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSBUSDtoCARDANO.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSBUSDtoCARDANO.type)
async def process_typeCRS_busdtocardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *BUSD*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinbusd) * float(CARDANOINRUB) * num)}` *CARDANO*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSBUSDtoCARDANO.next()
            await FormCRSBUSDtoCARDANO.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSBUSDtoCARDANO.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSBUSDtoCARDANO.adress)
async def process_adressCRS_busdtocardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *BUSD*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinbusd) * float(CARDANOINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *BUSD*\n*Реквизиты для оплаты:* ERC-20 -`{config.walletBUSD_ERC20}`\nBEP-20 -`{config.walletBUSD_BEP20}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSBUSDtoCARDANO.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSBUSDtoCARDANO.comfirm)
async def process_comfirmCRS_busdtocardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BUSD*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbusd) * float(CARDANOINRUB) * num)}` *CARDANO*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay busd -{num} {user_id}` & `/pay cardano {'{:0.4f}'.format(float(ex.rubinbusd) * float(CARDANOINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BUSD*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbusd) * float(CARDANOINRUB) * num)}` *CARDANO*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay cardano {'{:0.4f}'.format(float(ex.rubinbusd) * float(CARDANOINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM BUSD TO TRON = = = = = #
@dp.callback_query_handler(text="call_tocrstronBUSD")
async def call_crosschain_frbusd_totron(call: types.CallbackQuery):
    await FormCRSBUSDtoTRON.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSBUSDtoTRON.number)
async def process_numberCRS_busdtotron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[10]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSBUSDtoTRON.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSBUSDtoTRON.type)
async def process_typeCRS_busdtotron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *BUSD*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinbusd) * float(TRONINRUB) * num)}` *TRON*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSBUSDtoTRON.next()
            await FormCRSBUSDtoTRON.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSBUSDtoTRON.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSBUSDtoTRON.adress)
async def process_adressCRS_busdtotron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *BUSD*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinbusd) * float(TRONINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *BUSD*\n*Реквизиты для оплаты:* ERC-20 -`{config.walletBUSD_ERC20}`\nBEP-20 -`{config.walletBUSD_BEP20}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSBUSDtoTRON.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSBUSDtoTRON.comfirm)
async def process_comfirmCRS_busdtotron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BUSD*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbusd) * float(TRONINRUB) * num)}` *TRON*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay busd -{num} {user_id}` & `/pay tron {'{:0.4f}'.format(float(ex.rubinbusd) * float(TRONINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BUSD*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbusd) * float(TRONINRUB) * num)}` *TRON*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay tron {'{:0.4f}'.format(float(ex.rubinbusd) * float(TRONINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM BUSD TO POLKADOT = = = = = #
@dp.callback_query_handler(text="call_tocrspolkadotBUSD")
async def call_crosschain_frbusd_topolkadot(call: types.CallbackQuery):
    await FormCRSBUSDtoPOLKADOT.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSBUSDtoPOLKADOT.number)
async def process_numberCRS_busdtopolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[10]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSBUSDtoPOLKADOT.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSBUSDtoPOLKADOT.type)
async def process_typeCRS_busdtopolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *BUSD*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinbusd) * float(POLKADOTINRUB) * num)}` *POLKADOT*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSBUSDtoPOLKADOT.next()
            await FormCRSBUSDtoPOLKADOT.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSBUSDtoPOLKADOT.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSBUSDtoPOLKADOT.adress)
async def process_adressCRS_busdtopolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *BUSD*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinbusd) * float(POLKADOTINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *BUSD*\n*Реквизиты для оплаты:* ERC-20 -`{config.walletBUSD_ERC20}`\nBEP-20 -`{config.walletBUSD_BEP20}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSBUSDtoPOLKADOT.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSBUSDtoPOLKADOT.comfirm)
async def process_comfirmCRS_busdtopolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BUSD*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbusd) * float(POLKADOTINRUB) * num)}` *POLKADOT*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay busd -{num} {user_id}` & `/pay polkadot {'{:0.4f}'.format(float(ex.rubinbusd) * float(POLKADOTINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BUSD*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbusd) * float(POLKADOTINRUB) * num)}` *POLKADOT*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay polkadot {'{:0.4f}'.format(float(ex.rubinbusd) * float(POLKADOTINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM BUSD TO MATIC = = = = = #
@dp.callback_query_handler(text="call_tocrsmaticBUSD")
async def call_crosschain_frbusd_tomatic(call: types.CallbackQuery):
    await FormCRSBUSDtoMATIC.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSBUSDtoMATIC.number)
async def process_numberCRS_busdtomatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[10]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSBUSDtoMATIC.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSBUSDtoMATIC.type)
async def process_typeCRS_busdtomatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *BUSD*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinbusd) * float(MATICINRUB) * num)}` *MATIC*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSBUSDtoMATIC.next()
            await FormCRSBUSDtoMATIC.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSBUSDtoMATIC.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSBUSDtoMATIC.adress)
async def process_adressCRS_busdtomatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *BUSD*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinbusd) * float(MATICINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *BUSD*\n*Реквизиты для оплаты:* ERC-20 -`{config.walletBUSD_ERC20}`\nBEP-20 -`{config.walletBUSD_BEP20}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSBUSDtoMATIC.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSBUSDtoMATIC.comfirm)
async def process_comfirmCRS_busdtomatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BUSD*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbusd) * float(MATICINRUB) * num)}` *MATIC*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay busd -{num} {user_id}` & `/pay matic {'{:0.4f}'.format(float(ex.rubinbusd) * float(MATICINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *BUSD*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinbusd) * float(MATICINRUB) * num)}` *MATIC*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay matic {'{:0.4f}'.format(float(ex.rubinbusd) * float(MATICINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = FROM POLKADOT = = = = = = = #
@dp.callback_query_handler(text="call_frcrspolkadot")
async def call_crosschain_frpolkadot(call: types.CallbackQuery):
    await call.message.answer("🪙 Выберите криптовалюту, которую хотите получить:", reply_markup=maincrstoPOLKADOT)
    await call.message.delete()


# = = = = = FROM POLKADOT TO BTC = = = = = #
@dp.callback_query_handler(text="call_tocrsbitcoinPOLKADOT")
async def call_crosschain_frpolkadot_tobtc(call: types.CallbackQuery):
    await FormCRSPOLKADOTtoBTC.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSPOLKADOTtoBTC.number)
async def process_numberCRS_polkadottobtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[11]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSPOLKADOTtoBTC.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSPOLKADOTtoBTC.type)
async def process_typeCRS_polkadottobtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *POLKADOT*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(BTCINRUB) * num)}` *BTC*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSPOLKADOTtoBTC.next()
            await FormCRSPOLKADOTtoBTC.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSPOLKADOTtoBTC.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSPOLKADOTtoBTC.adress)
async def process_adressCRS_polkadottobtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *POLKADOT*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(BTCINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *POLKADOT*\n*Реквизиты для оплаты:* `{config.walletPolkadot}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSPOLKADOTtoBTC.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSPOLKADOTtoBTC.comfirm)
async def process_comfirmCRS_polkadottobtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *POLKADOT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(BTCINRUB) * num)}` *BTC*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay polkadot -{num} {user_id}` & `/pay bitcoin {'{:0.4f}'.format(float(ex.rubinpolkadot) * float(BTCINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *POLKADOT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(BTCINRUB) * num)}` *BTC*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay bitcoin {'{:0.4f}'.format(float(ex.rubinpolkadot) * float(BTCINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSPOLKADOTtoBTC.comfirm)
async def process_comfirmCRS_polkadottobtc(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *POLKADOT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(BTCINRUB) * num)}` *BTC*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay polkadot -{num} {user_id}` & `/pay bitcoin {'{:0.4f}'.format(float(ex.rubinpolkadot) * float(BTCINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM POLKADOT TO ETH = = = = = #
@dp.callback_query_handler(text="call_tocrsethereumPOLKADOT")
async def call_crosschain_frpolkadot_toeth(call: types.CallbackQuery):
    await FormCRSPOLKADOTtoETH.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSPOLKADOTtoETH.number)
async def process_numberCRS_polkadottoeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[11]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSPOLKADOTtoETH.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSPOLKADOTtoETH.type)
async def process_typeCRS_polkadottoeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *POLKADOT*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(ETHINRUB) * num)}` *ETH*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSPOLKADOTtoETH.next()
            await FormCRSPOLKADOTtoETH.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSPOLKADOTtoETH.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSPOLKADOTtoETH.adress)
async def process_adressCRS_polkadottoeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *POLKADOT*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(ETHINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *POLKADOT*\n*Реквизиты для оплаты:* `{config.walletPolkadot}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSPOLKADOTtoETH.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSPOLKADOTtoETH.comfirm)
async def process_comfirmCRS_polkadottoeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *POLKADOT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(ETHINRUB) * num)}` *ETH*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay polkadot -{num} {user_id}` & `/pay ethereum {'{:0.4f}'.format(float(ex.rubinpolkadot) * float(ETHINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *POLKADOT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(ETHINRUB) * num)}` *ETH*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay ethereum {'{:0.4f}'.format(float(ex.rubinpolkadot) * float(ETHINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSPOLKADOTtoETH.comfirm)
async def process_comfirmCRS_polkadottoeth(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *POLKADOT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(ETHINRUB) * num)}` *ETH*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay polkadot -{num} {user_id}` & `/pay ethereum {'{:0.4f}'.format(float(ex.rubinpolkadot) * float(ETHINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM POLKADOT TO SOL = = = = = #
@dp.callback_query_handler(text="call_tocrssolPOLKADOT")
async def call_crosschain_frpolkadot_tosol(call: types.CallbackQuery):
    await FormCRSPOLKADOTtoSOL.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSPOLKADOTtoSOL.number)
async def process_numberCRS_polkadottosol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[11]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSPOLKADOTtoSOL.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSPOLKADOTtoSOL.type)
async def process_typeCRS_polkadottosol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *POLKADOT*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(SOLINRUB) * num)}` *SOL*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSPOLKADOTtoSOL.next()
            await FormCRSPOLKADOTtoSOL.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSPOLKADOTtoSOL.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSPOLKADOTtoSOL.adress)
async def process_adressCRS_polkadottosol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *POLKADOT*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(SOLINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *POLKADOT*\n*Реквизиты для оплаты:* `{config.walletPolkadot}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSPOLKADOTtoSOL.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSPOLKADOTtoSOL.comfirm)
async def process_comfirmCRS_polkadottosol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *POLKADOT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(SOLINRUB) * num)}` *SOL*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay polkadot -{num} {user_id}` & `/pay solana {'{:0.4f}'.format(float(ex.rubinpolkadot) * float(SOLINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *POLKADOT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(SOLINRUB) * num)}` *SOL*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay solana {'{:0.4f}'.format(float(ex.rubinpolkadot) * float(SOLINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSPOLKADOTtoSOL.comfirm)
async def process_comfirmCRS_polkadottosol(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *POLKADOT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(SOLINRUB) * num)}` *SOL*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay polkadot -{num} {user_id}` & `/pay solana {'{:0.4f}'.format(float(ex.rubinpolkadot) * float(SOLINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM POLKADOT TO USDT = = = = = #
@dp.callback_query_handler(text="call_tocrsusdtPOLKADOT")
async def call_crosschain_frpolkadot_tousdt(call: types.CallbackQuery):
    await FormCRSPOLKADOTtoUSDT.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSPOLKADOTtoUSDT.number)
async def process_numberCRS_polkadottousdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[11]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSPOLKADOTtoUSDT.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSPOLKADOTtoUSDT.type)
async def process_typeCRS_polkadottousdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *POLKADOT*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(USDTINRUB) * num)}` *USDT*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSPOLKADOTtoUSDT.next()
            await FormCRSPOLKADOTtoUSDT.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSPOLKADOTtoUSDT.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSPOLKADOTtoUSDT.adress)
async def process_adressCRS_polkadottousdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *POLKADOT*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(USDTINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *POLKADOT*\n*Реквизиты для оплаты:* `{config.walletPolkadot}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSPOLKADOTtoUSDT.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSPOLKADOTtoUSDT.comfirm)
async def process_comfirmCRS_polkadottousdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *POLKADOT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(USDTINRUB) * num)}` *USDT*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay polkadot -{num} {user_id}` & `/pay usdt {'{:0.4f}'.format(float(ex.rubinpolkadot) * float(USDTINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *POLKADOT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(USDTINRUB) * num)}` *USDT*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay usdt {'{:0.4f}'.format(float(ex.rubinpolkadot) * float(USDTINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSPOLKADOTtoUSDT.comfirm)
async def process_comfirmCRS_polkadottousdt(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *POLKADOT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(USDTINRUB) * num)}` *USDT*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay polkadot -{num} {user_id}` & `/pay usdt {'{:0.4f}'.format(float(ex.rubinpolkadot) * float(USDTINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM POLKADOT TO BNB = = = = = #
@dp.callback_query_handler(text="call_tocrsbnbPOLKADOT")
async def call_crosschain_frpolkadot_tobnb(call: types.CallbackQuery):
    await FormCRSPOLKADOTtoBNB.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSPOLKADOTtoBNB.number)
async def process_numberCRS_polkadottobnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[11]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSPOLKADOTtoBNB.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSPOLKADOTtoBNB.type)
async def process_typeCRS_polkadottobnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *POLKADOT*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(BNBINRUB) * num)}` *BNB*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSPOLKADOTtoBNB.next()
            await FormCRSPOLKADOTtoBNB.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSPOLKADOTtoBNB.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSPOLKADOTtoBNB.adress)
async def process_adressCRS_polkadottobnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *POLKADOT*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(BNBINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *POLKADOT*\n*Реквизиты для оплаты:* `{config.walletPolkadot}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSPOLKADOTtoBNB.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSPOLKADOTtoBNB.comfirm)
async def process_comfirmCRS_polkadottobnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *POLKADOT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(BNBINRUB) * num)}` *BNB*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay polkadot -{num} {user_id}` & `/pay bnb {'{:0.4f}'.format(float(ex.rubinpolkadot) * float(BNBINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *POLKADOT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(BNBINRUB) * num)}` *BNB*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay bnb {'{:0.4f}'.format(float(ex.rubinpolkadot) * float(BNBINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSPOLKADOTtoBNB.comfirm)
async def process_comfirmCRS_polkadottobnb(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *POLKADOT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(BNBINRUB) * num)}` *BNB*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay polkadot -{num} {user_id}` & `/pay bnb {'{:0.4f}'.format(float(ex.rubinpolkadot) * float(BNBINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM POLKADOT TO CARDANO = = = = = #
@dp.callback_query_handler(text="call_tocrscardanoPOLKADOT")
async def call_crosschain_frpolkadot_tocardano(call: types.CallbackQuery):
    await FormCRSPOLKADOTtoCARDANO.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSPOLKADOTtoCARDANO.number)
async def process_numberCRS_polkadottocardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[11]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSPOLKADOTtoCARDANO.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSPOLKADOTtoCARDANO.type)
async def process_typeCRS_polkadottocardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *POLKADOT*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(CARDANOINRUB) * num)}` *CARDANO*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSPOLKADOTtoCARDANO.next()
            await FormCRSPOLKADOTtoCARDANO.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSPOLKADOTtoCARDANO.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSPOLKADOTtoCARDANO.adress)
async def process_adressCRS_polkadottocardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *POLKADOT*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(CARDANOINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *POLKADOT*\n*Реквизиты для оплаты:* `{config.walletPolkadot}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSPOLKADOTtoCARDANO.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSPOLKADOTtoCARDANO.comfirm)
async def process_comfirmCRS_polkadottocardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *POLKADOT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(CARDANOINRUB) * num)}` *CARDANO*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay polkadot -{num} {user_id}` & `/pay cardano {'{:0.4f}'.format(float(ex.rubinpolkadot) * float(CARDANOINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *POLKADOT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(CARDANOINRUB) * num)}` *CARDANO*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay cardano {'{:0.4f}'.format(float(ex.rubinpolkadot) * float(CARDANOINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSPOLKADOTtoCARDANO.comfirm)
async def process_comfirmCRS_polkadottocardano(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *POLKADOT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(CARDANOINRUB) * num)}` *CARDANO*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay polkadot -{num} {user_id}` & `/pay cardano {'{:0.4f}'.format(float(ex.rubinpolkadot) * float(CARDANOINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM POLKADOT TO TRON = = = = = #
@dp.callback_query_handler(text="call_tocrstronPOLKADOT")
async def call_crosschain_frpolkadot_totron(call: types.CallbackQuery):
    await FormCRSPOLKADOTtoTRON.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSPOLKADOTtoTRON.number)
async def process_numberCRS_polkadottotron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[11]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSPOLKADOTtoTRON.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSPOLKADOTtoTRON.type)
async def process_typeCRS_polkadottotron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *POLKADOT*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(TRONINRUB) * num)}` *TRON*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSPOLKADOTtoTRON.next()
            await FormCRSPOLKADOTtoTRON.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSPOLKADOTtoTRON.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSPOLKADOTtoTRON.adress)
async def process_adressCRS_polkadottotron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *POLKADOT*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(TRONINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *POLKADOT*\n*Реквизиты для оплаты:* `{config.walletPolkadot}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSPOLKADOTtoTRON.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSPOLKADOTtoTRON.comfirm)
async def process_comfirmCRS_polkadottotron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *POLKADOT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(TRONINRUB) * num)}` *TRON*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay polkadot -{num} {user_id}` & `/pay tron {'{:0.4f}'.format(float(ex.rubinpolkadot) * float(TRONINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *POLKADOT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(TRONINRUB) * num)}` *TRON*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay tron {'{:0.4f}'.format(float(ex.rubinpolkadot) * float(TRONINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSPOLKADOTtoTRON.comfirm)
async def process_comfirmCRS_polkadottotron(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *POLKADOT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(TRONINRUB) * num)}` *TRON*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay polkadot -{num} {user_id}` & `/pay tron {'{:0.4f}'.format(float(ex.rubinpolkadot) * float(TRONINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM POLKADOT TO BUSD = = = = = #
@dp.callback_query_handler(text="call_tocrsbusdPOLKADOT")
async def call_crosschain_frpolkadot_tobusd(call: types.CallbackQuery):
    await FormCRSPOLKADOTtoBUSD.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSPOLKADOTtoBUSD.number)
async def process_numberCRS_polkadottobusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[11]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSPOLKADOTtoBUSD.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSPOLKADOTtoBUSD.type)
async def process_typeCRS_polkadottobusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *POLKADOT*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(BUSDINRUB) * num)}` *BUSD*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSPOLKADOTtoBUSD.next()
            await FormCRSPOLKADOTtoBUSD.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSPOLKADOTtoBUSD.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSPOLKADOTtoBUSD.adress)
async def process_adressCRS_polkadottobusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *POLKADOT*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(BUSDINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *POLKADOT*\n*Реквизиты для оплаты:* `{config.walletPolkadot}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSPOLKADOTtoBUSD.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSPOLKADOTtoBUSD.comfirm)
async def process_comfirmCRS_polkadottobusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *POLKADOT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(BUSDINRUB) * num)}` *BUSD*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay polkadot -{num} {user_id}` & `/pay busd {'{:0.4f}'.format(float(ex.rubinpolkadot) * float(BUSDINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *POLKADOT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(BUSDINRUB) * num)}` *BUSD*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay busd {'{:0.4f}'.format(float(ex.rubinpolkadot) * float(BUSDINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSPOLKADOTtoBUSD.comfirm)
async def process_comfirmCRS_polkadottobusd(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *POLKADOT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(BUSDINRUB) * num)}` *BUSD*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay polkadot -{num} {user_id}` & `/pay busd {'{:0.4f}'.format(float(ex.rubinpolkadot) * float(BUSDINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM POLKADOT TO MATIC = = = = = #
@dp.callback_query_handler(text="call_tocrsmaticPOLKADOT")
async def call_crosschain_frpolkadot_tomatic(call: types.CallbackQuery):
    await FormCRSPOLKADOTtoMATIC.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSPOLKADOTtoMATIC.number)
async def process_numberCRS_polkadottomatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[11]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSPOLKADOTtoMATIC.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSPOLKADOTtoMATIC.type)
async def process_typeCRS_polkadottomatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *POLKADOT*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(MATICINRUB) * num)}` *MATIC*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSPOLKADOTtoMATIC.next()
            await FormCRSPOLKADOTtoMATIC.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSPOLKADOTtoMATIC.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSPOLKADOTtoMATIC.adress)
async def process_adressCRS_polkadottomatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *POLKADOT*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(MATICINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *POLKADOT*\n*Реквизиты для оплаты:* `{config.walletPolkadot}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSPOLKADOTtoMATIC.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSPOLKADOTtoMATIC.comfirm)
async def process_comfirmCRS_polkadottomatic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *POLKADOT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(MATICINRUB) * num)}` *MATIC*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay polkadot -{num} {user_id}` & `/pay matic {'{:0.4f}'.format(float(ex.rubinpolkadot) * float(MATICINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *POLKADOT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(MATICINRUB) * num)}` *MATIC*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay matic {'{:0.4f}'.format(float(ex.rubinpolkadot) * float(MATICINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSPOLKADOTtoMATIC.comfirm)
async def process_comfirmCRS_polkadottomatic(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *POLKADOT*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinpolkadot) * float(MATICINRUB) * num)}` *MATIC*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay polkadot -{num} {user_id}` & `/pay matic {'{:0.4f}'.format(float(ex.rubinpolkadot) * float(MATICINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = FROM MATIC = = = = = = = #
@dp.callback_query_handler(text="call_frcrsmatic")
async def call_crosschain_frmatic(call: types.CallbackQuery):
    await call.message.answer("🪙 Выберите криптовалюту, которую хотите получить:", reply_markup=maincrstoMATIC)
    await call.message.delete()


# = = = = = FROM MATIC TO BTC = = = = = #
@dp.callback_query_handler(text="call_tocrsbitcoinMATIC")
async def call_crosschain_frmatic_tobtc(call: types.CallbackQuery):
    await FormCRSMATICtoBTC.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSMATICtoBTC.number)
async def process_numberCRS_matictobtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[12]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSMATICtoBTC.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSMATICtoBTC.type)
async def process_typeCRS_matictobtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *MATIC*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(BTCINRUB) * num)}` *BTC*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSMATICtoBTC.next()
            await FormCRSMATICtoBTC.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSMATICtoBTC.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSMATICtoBTC.adress)
async def process_adressCRS_matictobtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *MATIC*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(BTCINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *MATIC*\n*Реквизиты для оплаты:* `{config.walletMatic}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSMATICtoBTC.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSMATICtoBTC.comfirm)
async def process_comfirmCRS_matictobtc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *MATIC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(BTCINRUB) * num)}` *BTC*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay matic -{num} {user_id}` & `/pay bitcoin {'{:0.4f}'.format(float(ex.rubinmatic) * float(BTCINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *MATIC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(BTCINRUB) * num)}` *BTC*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay bitcoin {'{:0.4f}'.format(float(ex.rubinmatic) * float(BTCINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSMATICtoBTC.comfirm)
async def process_comfirmCRS_matictobtc(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *MATIC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(BTCINRUB) * num)}` *BTC*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay matic -{num} {user_id}` & `/pay bitcoin {'{:0.4f}'.format(float(ex.rubinmatic) * float(BTCINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM MATIC TO ETH = = = = = #
@dp.callback_query_handler(text="call_tocrsethereumMATIC")
async def call_crosschain_frmatic_toeth(call: types.CallbackQuery):
    await FormCRSMATICtoETH.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSMATICtoETH.number)
async def process_numberCRS_matictoeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[12]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSMATICtoETH.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSMATICtoETH.type)
async def process_typeCRS_matictoeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *MATIC*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(ETHINRUB) * num)}` *ETH*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSMATICtoETH.next()
            await FormCRSMATICtoETH.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSMATICtoETH.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSMATICtoETH.adress)
async def process_adressCRS_matictoeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *MATIC*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(ETHINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *MATIC*\n*Реквизиты для оплаты:* `{config.walletMatic}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSMATICtoETH.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSMATICtoETH.comfirm)
async def process_comfirmCRS_matictoeth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *MATIC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(ETHINRUB) * num)}` *ETH*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay matic -{num} {user_id}` & `/pay ethereum {'{:0.4f}'.format(float(ex.rubinmatic) * float(ETHINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *MATIC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(ETHINRUB) * num)}` *ETH*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay ethereum {'{:0.4f}'.format(float(ex.rubinmatic) * float(ETHINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSMATICtoETH.comfirm)
async def process_comfirmCRS_matictoeth(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *MATIC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(ETHINRUB) * num)}` *ETH*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay matic -{num} {user_id}` & `/pay ethereum {'{:0.4f}'.format(float(ex.rubinmatic) * float(ETHINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM MATIC TO SOL = = = = = #
@dp.callback_query_handler(text="call_tocrssolMATIC")
async def call_crosschain_frmatic_tosol(call: types.CallbackQuery):
    await FormCRSMATICtoSOL.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSMATICtoSOL.number)
async def process_numberCRS_matictosol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[12]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSMATICtoSOL.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSMATICtoSOL.type)
async def process_typeCRS_matictosol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *MATIC*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(SOLINRUB) * num)}` *SOL*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSMATICtoSOL.next()
            await FormCRSMATICtoSOL.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSMATICtoSOL.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSMATICtoSOL.adress)
async def process_adressCRS_matictosol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *MATIC*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(SOLINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *MATIC*\n*Реквизиты для оплаты:* `{config.walletMatic}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSMATICtoSOL.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSMATICtoSOL.comfirm)
async def process_comfirmCRS_matictosol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *MATIC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(SOLINRUB) * num)}` *SOL*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay matic -{num} {user_id}` & `/pay sol {'{:0.4f}'.format(float(ex.rubinmatic) * float(SOLINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *MATIC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(SOLINRUB) * num)}` *SOL*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay sol {'{:0.4f}'.format(float(ex.rubinmatic) * float(SOLINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSMATICtoSOL.comfirm)
async def process_comfirmCRS_matictosol(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *MATIC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(SOLINRUB) * num)}` *SOL*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay matic -{num} {user_id}` & `/pay sol {'{:0.4f}'.format(float(ex.rubinmatic) * float(SOLINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM MATIC TO USDT = = = = = #
@dp.callback_query_handler(text="call_tocrsusdtMATIC")
async def call_crosschain_frmatic_tousdt(call: types.CallbackQuery):
    await FormCRSMATICtoUSDT.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSMATICtoUSDT.number)
async def process_numberCRS_matictousdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[12]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSMATICtoUSDT.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSMATICtoUSDT.type)
async def process_typeCRS_matictousdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *MATIC*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(USDTINRUB) * num)}` *USDT*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSMATICtoUSDT.next()
            await FormCRSMATICtoUSDT.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSMATICtoUSDT.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSMATICtoUSDT.adress)
async def process_adressCRS_matictousdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *MATIC*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(USDTINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *MATIC*\n*Реквизиты для оплаты:* `{config.walletMatic}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSMATICtoUSDT.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSMATICtoUSDT.comfirm)
async def process_comfirmCRS_matictousdt(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *MATIC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(USDTINRUB) * num)}` *USDT*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay matic -{num} {user_id}` & `/pay usdt {'{:0.4f}'.format(float(ex.rubinmatic) * float(USDTINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *MATIC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(USDTINRUB) * num)}` *USDT*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay usdt {'{:0.4f}'.format(float(ex.rubinmatic) * float(USDTINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSMATICtoUSDT.comfirm)
async def process_comfirmCRS_matictousdt(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *MATIC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(USDTINRUB) * num)}` *USDT*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay matic -{num} {user_id}` & `/pay usdt {'{:0.4f}'.format(float(ex.rubinmatic) * float(USDTINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM MATIC TO BNB = = = = = #
@dp.callback_query_handler(text="call_tocrsbnbMATIC")
async def call_crosschain_frmatic_tobnb(call: types.CallbackQuery):
    await FormCRSMATICtoBNB.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSMATICtoBNB.number)
async def process_numberCRS_matictobnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[12]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSMATICtoBNB.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSMATICtoBNB.type)
async def process_typeCRS_matictobnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *MATIC*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(BNBINRUB) * num)}` *BNB*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSMATICtoBNB.next()
            await FormCRSMATICtoBNB.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSMATICtoBNB.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSMATICtoBNB.adress)
async def process_adressCRS_matictobnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *MATIC*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(BNBINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *MATIC*\n*Реквизиты для оплаты:* `{config.walletMatic}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSMATICtoBNB.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSMATICtoBNB.comfirm)
async def process_comfirmCRS_matictobnb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *MATIC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(BNBINRUB) * num)}` *BNB*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay matic -{num} {user_id}` & `/pay bnb {'{:0.4f}'.format(float(ex.rubinmatic) * float(BNBINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *MATIC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(BNBINRUB) * num)}` *BNB*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay bnb {'{:0.4f}'.format(float(ex.rubinmatic) * float(BNBINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSMATICtoBNB.comfirm)
async def process_comfirmCRS_matictobnb(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *MATIC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(BNBINRUB) * num)}` *BNB*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay matic -{num} {user_id}` & `/pay bnb {'{:0.4f}'.format(float(ex.rubinmatic) * float(BNBINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM MATIC TO CARDANO = = = = = #
@dp.callback_query_handler(text="call_tocrscardanoMATIC")
async def call_crosschain_frmatic_tocardano(call: types.CallbackQuery):
    await FormCRSMATICtoCARDANO.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSMATICtoCARDANO.number)
async def process_numberCRS_matictocardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[12]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSMATICtoCARDANO.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSMATICtoCARDANO.type)
async def process_typeCRS_matictocardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *MATIC*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(CARDANOINRUB) * num)}` *CARDANO*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSMATICtoCARDANO.next()
            await FormCRSMATICtoCARDANO.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSMATICtoCARDANO.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSMATICtoCARDANO.adress)
async def process_adressCRS_matictocardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *MATIC*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(CARDANOINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *MATIC*\n*Реквизиты для оплаты:* `{config.walletMatic}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSMATICtoCARDANO.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSMATICtoCARDANO.comfirm)
async def process_comfirmCRS_matictocardano(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *MATIC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(CARDANOINRUB) * num)}` *CARDANO*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay matic -{num} {user_id}` & `/pay cardano {'{:0.4f}'.format(float(ex.rubinmatic) * float(CARDANOINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *MATIC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(CARDANOINRUB) * num)}` *CARDANO*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay cardano {'{:0.4f}'.format(float(ex.rubinmatic) * float(CARDANOINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSMATICtoCARDANO.comfirm)
async def process_comfirmCRS_matictocardano(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *MATIC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(CARDANOINRUB) * num)}` *CARDANO*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay matic -{num} {user_id}` & `/pay cardano {'{:0.4f}'.format(float(ex.rubinmatic) * float(CARDANOINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM MATIC TO TRON = = = = = #
@dp.callback_query_handler(text="call_tocrstronMATIC")
async def call_crosschain_frmatic_totron(call: types.CallbackQuery):
    await FormCRSMATICtoTRON.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSMATICtoTRON.number)
async def process_numberCRS_matictotron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[12]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSMATICtoTRON.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSMATICtoTRON.type)
async def process_typeCRS_matictotron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *MATIC*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(TRONINRUB) * num)}` *TRON*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSMATICtoTRON.next()
            await FormCRSMATICtoTRON.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSMATICtoTRON.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSMATICtoTRON.adress)
async def process_adressCRS_matictotron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *MATIC*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(TRONINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *MATIC*\n*Реквизиты для оплаты:* `{config.walletMatic}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSMATICtoTRON.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSMATICtoTRON.comfirm)
async def process_comfirmCRS_matictotron(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *MATIC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(TRONINRUB) * num)}` *TRON*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay matic -{num} {user_id}` & `/pay tron {'{:0.4f}'.format(float(ex.rubinmatic) * float(TRONINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *MATIC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(TRONINRUB) * num)}` *TRON*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay tron {'{:0.4f}'.format(float(ex.rubinmatic) * float(TRONINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSMATICtoTRON.comfirm)
async def process_comfirmCRS_matictotron(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *MATIC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(TRONINRUB) * num)}` *TRON*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay matic -{num} {user_id}` & `/pay tron {'{:0.4f}'.format(float(ex.rubinmatic) * float(TRONINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM MATIC TO BUSD = = = = = #
@dp.callback_query_handler(text="call_tocrsbusdMATIC")
async def call_crosschain_frmatic_tobusd(call: types.CallbackQuery):
    await FormCRSMATICtoBUSD.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSMATICtoBUSD.number)
async def process_numberCRS_matictobusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[12]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSMATICtoBUSD.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSMATICtoBUSD.type)
async def process_typeCRS_matictobusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *MATIC*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(BUSDINRUB) * num)}` *BUSD*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSMATICtoBUSD.next()
            await FormCRSMATICtoBUSD.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSMATICtoBUSD.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSMATICtoBUSD.adress)
async def process_adressCRS_matictobusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *MATIC*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(BUSDINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *MATIC*\n*Реквизиты для оплаты:* `{config.walletMatic}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSMATICtoBUSD.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSMATICtoBUSD.comfirm)
async def process_comfirmCRS_matictobusd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *MATIC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(BUSDINRUB) * num)}` *BUSD*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay matic -{num} {user_id}` & `/pay busd {'{:0.4f}'.format(float(ex.rubinmatic) * float(BUSDINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *MATIC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(BUSDINRUB) * num)}` *BUSD*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay busd {'{:0.4f}'.format(float(ex.rubinmatic) * float(BUSDINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSMATICtoBUSD.comfirm)
async def process_comfirmCRS_matictobusd(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *MATIC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(BUSDINRUB) * num)}` *BUSD*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay matic -{num} {user_id}` & `/pay busd {'{:0.4f}'.format(float(ex.rubinmatic) * float(BUSDINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = FROM MATIC TO POLKADOT = = = = = #
@dp.callback_query_handler(text="call_tocrspolkadotMATIC")
async def call_crosschain_frmatic_topolkadot(call: types.CallbackQuery):
    await FormCRSMATICtoPOLKADOT.number.set()
    await call.message.answer("Введите количество, которое хотите обменять:", reply_markup=menuCancel)


@dp.message_handler(state=FormCRSMATICtoPOLKADOT.number)
async def process_numberCRS_matictopolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)
        for row in db.cursor.execute(f"SELECT * FROM users where id={message.from_user.id}"):
            if message.text == "Отмена 🔴":
                await state.finish()
                await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)
            elif float(data['number']) > row[12]:
                await state.finish()
                await message.answer("На вашем балансе, недостаточно средств. Вы вернулись в главное меню",
                                     reply_markup=st.mainMenu)
            else:
                await FormCRSMATICtoPOLKADOT.next()
                await message.answer("Откуда перевести средства:", reply_markup=menuBuyTo)


@dp.message_handler(state=FormCRSMATICtoPOLKADOT.type)
async def process_typeCRS_matictopolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        if data["type"] == "С баланса бота 📲":
            num = data['number']
            num = num.replace(",", ".")
            num = float(num)
            await message.answer(
                f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{num}` *MATIC*\n*Получаете:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(POLKADOTINRUB) * num)}` *POLKADOT*")
            await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)
            await FormCRSMATICtoPOLKADOT.next()
            await FormCRSMATICtoPOLKADOT.next()

        elif data["type"] == "С другого кошелька 💸":
            await FormCRSMATICtoPOLKADOT.next()
            await message.answer("Введите целевой кошелёк: ", reply_markup=types.ReplyKeyboardRemove())

        elif data['type'] == "Отмена 🔴":
            await state.finish()
            await message.answer("Действие отменено. Вы вернулись в главное меню", reply_markup=st.mainMenu)


@dp.message_handler(state=FormCRSMATICtoPOLKADOT.adress)
async def process_adressCRS_matictopolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
        num = data['number']
        num = num.replace(",", ".")
        num = float(num)

        adress = data['adress']
        await message.answer(
            f"📄 *Ваш Чек*\n\n*Вы отдадите:* `{data['number']}` *MATIC*\n*Вы получите:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(POLKADOTINRUB) * num)}`\n*Целевой адресс:* `{adress}`\n*К оплате:* `{data['number']}` *MATIC*\n*Реквизиты для оплаты:* `{config.walletMatic}`\n\nПосле оплаты не забудьте нажать кнопку «Я оплатил(а)» и ожидайте одобрения Администратора")
        await FormCRSMATICtoPOLKADOT.next()
        await message.answer("Подтвердите ваш платёж", reply_markup=menuConfirm)


@dp.message_handler(state=FormCRSMATICtoPOLKADOT.comfirm)
async def process_comfirmCRS_matictopolkadot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comfirm'] = message.text
        if data['comfirm'] == "Подтверждаю":
            if data["type"] == "С баланса бота 📲":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *MATIC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(POLKADOTINRUB) * num)}` *POLKADOT*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay matic -{num} {user_id}` & `/pay polkadot {'{:0.4f}'.format(float(ex.rubinmatic) * float(POLKADOTINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
            elif data["type"] == "С другого кошелька 💸":
                num = data['number']
                num = num.replace(",", ".")
                num = float(num)
                adress = data['adress']
                user_id = message.from_user.id
                await bot.send_message(config.admin_id,
                                       f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *MATIC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(POLKADOTINRUB) * num)}` *POLKADOT*\n*Целевой кошелёк:* `{adress}`\n*ID пользователя:* `{user_id}`\n\n_Example of use_: `/pay polkadot {'{:0.4f}'.format(float(ex.rubinmatic) * float(POLKADOTINRUB) * num)} {user_id}`")
                await state.finish()
                await message.answer(
                    "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                    reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


@dp.message_handler(state=FormCRSMATICtoPOLKADOT.comfirm)
async def process_comfirmCRS_matictopolkadot(message: types.Message, state: FSMContext):
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
                                   f"_#CROSSCHAIN_\n\n📄 *Чек пользователя*\n\n*Он отдаёт:* `{num}` *MATIC*\n*Получает:* `{'{:0.4f}'.format(float(ex.rubinmatic) * float(POLKADOTINRUB) * num)}` *POLKADOT*\nID пользователя: `{user_id}`\n\n_Example of use_: `/pay matic -{num} {user_id}` & `/pay polkadot {'{:0.4f}'.format(float(ex.rubinmatic) * float(POLKADOTINRUB) * num)} {user_id}`")
            await state.finish()
            await message.answer(
                "Заказ оформлен, ожидайте одобрения и обновления баланса. Вас направлено в главное меню",
                reply_markup=st.mainMenu)
        else:
            await message.answer("Заказ отменён, вы вернулись в главное меню", reply_markup=st.mainMenu)
            await state.finish()


# = = = = = = = REGISTER HANDLERS = = = = = = = #
def register_handlers_crosschain_exchanger(dp: Dispatcher):
    # = = = = = = CROSSCHAIN ACTIVE  = = = = = = #
    dp.register_message_handler(val_crosschain_exchanger, lambda msg: msg.text.startswith("Crosschain обмен💱"))
    dp.register_message_handler(val_cancel, lambda msg: msg.text.startswith("Отмена 🔴"))

    # = = = = EXCHANGE : STATE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frbitcoin, text="call_frcrsbitcoin")
    dp.register_callback_query_handler(call_crosschain_frethereum, text="call_frcrsethereum")
    dp.register_callback_query_handler(call_crosschain_frsolana, text="call_frcrssolana")
    dp.register_callback_query_handler(call_crosschain_frusdt, text="call_frcrsusdt")
    dp.register_callback_query_handler(call_crosschain_frbnb, text="call_frcrsbnb")
    dp.register_callback_query_handler(call_crosschain_frcardano, text="call_frcrscardano")
    dp.register_callback_query_handler(call_crosschain_frtron, text="call_frcrstron")
    dp.register_callback_query_handler(call_crosschain_frbusd, text="call_frcrsbusd")
    dp.register_callback_query_handler(call_crosschain_frpolkadot, text="call_frcrspolkadot")
    dp.register_callback_query_handler(call_crosschain_frmatic, text="call_frcrsmatic")

    # = = = = BTC to ETH : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frbitcoin_toeth, text="call_tocrsethereumBTC")
    dp.register_message_handler(process_numberCRS_btctoeth, state=FormCRSBTCtoETH.number)
    dp.register_message_handler(process_typeCRS_btctoeth, state=FormCRSBTCtoETH.type)
    dp.register_message_handler(process_adressCRS_btctoeth, state=FormCRSBTCtoETH.adress)
    dp.register_message_handler(process_comfirmCRS_btctoeth, state=FormCRSBTCtoETH.comfirm)

    # = = = = BTC to SOL : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frbitcoin_tosol, text="call_tocrssolBTC")
    dp.register_message_handler(process_numberCRS_btctosol, state=FormCRSBTCtoSOL.number)
    dp.register_message_handler(process_typeCRS_btctosol, state=FormCRSBTCtoSOL.type)
    dp.register_message_handler(process_adressCRS_btctosol, state=FormCRSBTCtoSOL.adress)
    dp.register_message_handler(process_comfirmCRS_btctosol, state=FormCRSBTCtoSOL.comfirm)

    # = = = = BTC to USDT : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frbitcoin_tousdt, text="call_tocrsusdtBTC")
    dp.register_message_handler(process_numberCRS_btctousdt, state=FormCRSBTCtoUSDT.number)
    dp.register_message_handler(process_typeCRS_btctousdt, state=FormCRSBTCtoUSDT.type)
    dp.register_message_handler(process_adressCRS_btctousdt, state=FormCRSBTCtoUSDT.adress)
    dp.register_message_handler(process_comfirmCRS_btctousdt, state=FormCRSBTCtoUSDT.comfirm)

    # = = = = BTC to BNB : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frbitcoin_tobnb, text="call_tocrsbnbBTC")
    dp.register_message_handler(process_numberCRS_btctobnb, state=FormCRSBTCtoBNB.number)
    dp.register_message_handler(process_typeCRS_btctobnb, state=FormCRSBTCtoBNB.type)
    dp.register_message_handler(process_adressCRS_btctobnb, state=FormCRSBTCtoBNB.adress)
    dp.register_message_handler(process_comfirmCRS_btctobnb, state=FormCRSBTCtoBNB.comfirm)

    # = = = = BTC to CARDANO : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frbitcoin_tocardano, text="call_tocrscardanoBTC")
    dp.register_message_handler(process_numberCRS_btctocardano, state=FormCRSBTCtoCARDANO.number)
    dp.register_message_handler(process_typeCRS_btctocardano, state=FormCRSBTCtoCARDANO.type)
    dp.register_message_handler(process_adressCRS_btctocardano, state=FormCRSBTCtoCARDANO.adress)
    dp.register_message_handler(process_comfirmCRS_btctocardano, state=FormCRSBTCtoCARDANO.comfirm)

    # = = = = BTC to TRON : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frbitcoin_totron, text="call_tocrstronBTC")
    dp.register_message_handler(process_numberCRS_btctotron, state=FormCRSBTCtoTRON.number)
    dp.register_message_handler(process_typeCRS_btctotron, state=FormCRSBTCtoTRON.type)
    dp.register_message_handler(process_adressCRS_btctotron, state=FormCRSBTCtoTRON.adress)
    dp.register_message_handler(process_comfirmCRS_btctotron, state=FormCRSBTCtoTRON.comfirm)

    # = = = = BTC to BUSD : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frbitcoin_tobusd, text="call_tocrsbusdBTC")
    dp.register_message_handler(process_numberCRS_btctobusd, state=FormCRSBTCtoBUSD.number)
    dp.register_message_handler(process_typeCRS_btctobusd, state=FormCRSBTCtoBUSD.type)
    dp.register_message_handler(process_adressCRS_btctobusd, state=FormCRSBTCtoBUSD.adress)
    dp.register_message_handler(process_comfirmCRS_btctobusd, state=FormCRSBTCtoBUSD.comfirm)

    # = = = = BTC to POLKADOT : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frbitcoin_topolkadot, text="call_tocrspolkadotBTC")
    dp.register_message_handler(process_numberCRS_btctopolkadot, state=FormCRSBTCtoPOLKADOT.number)
    dp.register_message_handler(process_typeCRS_btctopolkadot, state=FormCRSBTCtoPOLKADOT.type)
    dp.register_message_handler(process_adressCRS_btctopolkadot, state=FormCRSBTCtoPOLKADOT.adress)
    dp.register_message_handler(process_comfirmCRS_btctopolkadot, state=FormCRSBTCtoPOLKADOT.comfirm)

    # = = = = BTC to MATIC : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frbitcoin_tomatic, text="call_tocrsmaticBTC")
    dp.register_message_handler(process_numberCRS_btctomatic, state=FormCRSBTCtoMATIC.number)
    dp.register_message_handler(process_typeCRS_btctomatic, state=FormCRSBTCtoMATIC.type)
    dp.register_message_handler(process_adressCRS_btctomatic, state=FormCRSBTCtoMATIC.adress)
    dp.register_message_handler(process_comfirmCRS_btctomatic, state=FormCRSBTCtoMATIC.comfirm)

    # = = = = ETH to BTC : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frethereum_tobtc, text="call_tocrsbitcoinETH")
    dp.register_message_handler(process_numberCRS_ethtobtc, state=FormCRSETHtoBTC.number)
    dp.register_message_handler(process_typeCRS_ethtobtc, state=FormCRSETHtoBTC.type)
    dp.register_message_handler(process_adressCRS_ethtobtc, state=FormCRSETHtoBTC.adress)
    dp.register_message_handler(process_comfirmCRS_ethtobtc, state=FormCRSETHtoBTC.comfirm)

    # = = = = ETH to SOL : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frethereum_tosol, text="call_tocrssolETH")
    dp.register_message_handler(process_numberCRS_ethtosol, state=FormCRSETHtoSOL.number)
    dp.register_message_handler(process_typeCRS_ethtosol, state=FormCRSETHtoSOL.type)
    dp.register_message_handler(process_adressCRS_ethtosol, state=FormCRSETHtoSOL.adress)
    dp.register_message_handler(process_comfirmCRS_ethtosol, state=FormCRSETHtoSOL.comfirm)

    # = = = = ETH to USDT : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frethereum_tousdt, text="call_tocrsusdtETH")
    dp.register_message_handler(process_numberCRS_ethtousdt, state=FormCRSETHtoUSDT.number)
    dp.register_message_handler(process_typeCRS_ethtousdt, state=FormCRSETHtoUSDT.type)
    dp.register_message_handler(process_adressCRS_ethtousdt, state=FormCRSETHtoUSDT.adress)
    dp.register_message_handler(process_comfirmCRS_ethtousdt, state=FormCRSETHtoUSDT.comfirm)

    # = = = = ETH to BNB : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frethereum_tobnb, text="call_tocrsbnbETH")
    dp.register_message_handler(process_numberCRS_ethtobnb, state=FormCRSETHtoBNB.number)
    dp.register_message_handler(process_typeCRS_ethtobnb, state=FormCRSETHtoBNB.type)
    dp.register_message_handler(process_adressCRS_ethtobnb, state=FormCRSETHtoBNB.adress)
    dp.register_message_handler(process_comfirmCRS_ethtobnb, state=FormCRSETHtoBNB.comfirm)

    # = = = = ETH to CARDANO : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frethereum_tocardano, text="call_tocrscardanoETH")
    dp.register_message_handler(process_numberCRS_ethtocardano, state=FormCRSETHtoCARDANO.number)
    dp.register_message_handler(process_typeCRS_ethtocardano, state=FormCRSETHtoCARDANO.type)
    dp.register_message_handler(process_adressCRS_ethtocardano, state=FormCRSETHtoCARDANO.adress)
    dp.register_message_handler(process_comfirmCRS_ethtocardano, state=FormCRSETHtoCARDANO.comfirm)

    # = = = = ETH to TRON : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frethereum_totron, text="call_tocrstronETH")
    dp.register_message_handler(process_numberCRS_ethtotron, state=FormCRSETHtoTRON.number)
    dp.register_message_handler(process_typeCRS_ethtotron, state=FormCRSETHtoTRON.type)
    dp.register_message_handler(process_adressCRS_ethtotron, state=FormCRSETHtoTRON.adress)
    dp.register_message_handler(process_comfirmCRS_ethtotron, state=FormCRSETHtoTRON.comfirm)

    # = = = = ETH to BUSD : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frethereum_tobusd, text="call_tocrsbusdETH")
    dp.register_message_handler(process_numberCRS_ethtobusd, state=FormCRSETHtoBUSD.number)
    dp.register_message_handler(process_typeCRS_ethtobusd, state=FormCRSETHtoBUSD.type)
    dp.register_message_handler(process_adressCRS_ethtobusd, state=FormCRSETHtoBUSD.adress)
    dp.register_message_handler(process_comfirmCRS_ethtobusd, state=FormCRSETHtoBUSD.comfirm)

    # = = = = ETH to POLKADOT : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frethereum_topolkadot, text="call_tocrspolkadotETH")
    dp.register_message_handler(process_numberCRS_ethtopolkadot, state=FormCRSETHtoPOLKADOT.number)
    dp.register_message_handler(process_typeCRS_ethtopolkadot, state=FormCRSETHtoPOLKADOT.type)
    dp.register_message_handler(process_adressCRS_ethtopolkadot, state=FormCRSETHtoPOLKADOT.adress)
    dp.register_message_handler(process_comfirmCRS_ethtopolkadot, state=FormCRSETHtoPOLKADOT.comfirm)

    # = = = = ETH to MATIC : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frethereum_tomatic, text="call_tocrsmaticETH")
    dp.register_message_handler(process_numberCRS_ethtomatic, state=FormCRSETHtoMATIC.number)
    dp.register_message_handler(process_typeCRS_ethtomatic, state=FormCRSETHtoMATIC.type)
    dp.register_message_handler(process_adressCRS_ethtomatic, state=FormCRSETHtoMATIC.adress)
    dp.register_message_handler(process_comfirmCRS_ethtomatic, state=FormCRSETHtoMATIC.comfirm)

    # = = = = SOL to BTC : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frsolana_tobtc, text="call_tocrsbitcoinSOL")
    dp.register_message_handler(process_numberCRS_soltobtc, state=FormCRSSOLtoBTC.number)
    dp.register_message_handler(process_typeCRS_soltobtc, state=FormCRSSOLtoBTC.type)
    dp.register_message_handler(process_adressCRS_soltobtc, state=FormCRSSOLtoBTC.adress)
    dp.register_message_handler(process_comfirmCRS_soltobtc, state=FormCRSSOLtoBTC.comfirm)

    # = = = = SOL to ETH : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frsolana_toeth, text="call_tocrsethereumSOL")
    dp.register_message_handler(process_numberCRS_soltoeth, state=FormCRSSOLtoETH.number)
    dp.register_message_handler(process_typeCRS_soltobtc, state=FormCRSSOLtoBTC.type)
    dp.register_message_handler(process_adressCRS_soltobtc, state=FormCRSSOLtoBTC.adress)
    dp.register_message_handler(process_comfirmCRS_soltoeth, state=FormCRSSOLtoETH.comfirm)

    # = = = = SOL to USDT : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frsolana_tousdt, text="call_tocrsusdtSOL")
    dp.register_message_handler(process_numberCRS_soltousdt, state=FormCRSSOLtoUSDT.number)
    dp.register_message_handler(process_typeCRS_soltousdt, state=FormCRSSOLtoUSDT.type)
    dp.register_message_handler(process_adressCRS_soltousdt, state=FormCRSSOLtoUSDT.adress)
    dp.register_message_handler(process_comfirmCRS_soltousdt, state=FormCRSSOLtoUSDT.comfirm)

    # = = = = SOL to BNB : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frsolana_tobnb, text="call_tocrsbnbSOL")
    dp.register_message_handler(process_numberCRS_soltobnb, state=FormCRSSOLtoBNB.number)
    dp.register_message_handler(process_typeCRS_soltobnb, state=FormCRSSOLtoBNB.type)
    dp.register_message_handler(process_adressCRS_soltobnb, state=FormCRSSOLtoBNB.adress)
    dp.register_message_handler(process_comfirmCRS_soltobnb, state=FormCRSSOLtoBNB.comfirm)

    # = = = = SOL to CARDANO : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frsolana_tocardano, text="call_tocrscardanoSOL")
    dp.register_message_handler(process_numberCRS_soltocardano, state=FormCRSSOLtoCARDANO.number)
    dp.register_message_handler(process_typeCRS_soltocardano, state=FormCRSSOLtoCARDANO.type)
    dp.register_message_handler(process_adressCRS_soltocardano, state=FormCRSSOLtoCARDANO.adress)
    dp.register_message_handler(process_comfirmCRS_soltocardano, state=FormCRSSOLtoCARDANO.comfirm)

    # = = = = SOL to TRON : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frsolana_totron, text="call_tocrstronSOL")
    dp.register_message_handler(process_numberCRS_soltotron, state=FormCRSSOLtoTRON.number)
    dp.register_message_handler(process_typeCRS_soltotron, state=FormCRSSOLtoTRON.type)
    dp.register_message_handler(process_adressCRS_soltotron, state=FormCRSSOLtoTRON.adress)
    dp.register_message_handler(process_comfirmCRS_soltotron, state=FormCRSSOLtoTRON.comfirm)

    # = = = = SOL to BUSD : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frsolana_tobusd, text="call_tocrsbusdSOL")
    dp.register_message_handler(process_numberCRS_soltobusd, state=FormCRSSOLtoBUSD.number)
    dp.register_message_handler(process_typeCRS_soltobusd, state=FormCRSSOLtoBUSD.type)
    dp.register_message_handler(process_adressCRS_soltobusd, state=FormCRSSOLtoBUSD.adress)
    dp.register_message_handler(process_comfirmCRS_soltobusd, state=FormCRSSOLtoBUSD.comfirm)

    # = = = = SOL to POLKADOT : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frsolana_topolkadot, text="call_tocrspolkadotSOL")
    dp.register_message_handler(process_numberCRS_soltopolkadot, state=FormCRSSOLtoPOLKADOT.number)
    dp.register_message_handler(process_typeCRS_soltopolkadot, state=FormCRSSOLtoPOLKADOT.type)
    dp.register_message_handler(process_adressCRS_soltopolkadot, state=FormCRSSOLtoPOLKADOT.adress)
    dp.register_message_handler(process_comfirmCRS_soltopolkadot, state=FormCRSSOLtoPOLKADOT.comfirm)

    # = = = = SOL to MATIC : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frsolana_tomatic, text="call_tocrsmaticSOL")
    dp.register_message_handler(process_numberCRS_soltomatic, state=FormCRSSOLtoMATIC.number)
    dp.register_message_handler(process_typeCRS_soltomatic, state=FormCRSSOLtoMATIC.type)
    dp.register_message_handler(process_adressCRS_soltomatic, state=FormCRSSOLtoMATIC.adress)
    dp.register_message_handler(process_comfirmCRS_soltomatic, state=FormCRSSOLtoMATIC.comfirm)

    # = = = = USDT to BTC : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frusdt_tobtc, text="call_tocrsbitcoinUSDT")
    dp.register_message_handler(process_numberCRS_usdttobtc, state=FormCRSUSDTtoBTC.number)
    dp.register_message_handler(process_typeCRS_usdttobtc, state=FormCRSUSDTtoBTC.type)
    dp.register_message_handler(process_adressCRS_usdttobtc, state=FormCRSUSDTtoBTC.adress)
    dp.register_message_handler(process_comfirmCRS_usdttobtc, state=FormCRSUSDTtoBTC.comfirm)

    # = = = = USDT to ETH : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frusdt_toeth, text="call_tocrsethereumUSDT")
    dp.register_message_handler(process_numberCRS_usdttoeth, state=FormCRSUSDTtoETH.number)
    dp.register_message_handler(process_typeCRS_usdttoeth, state=FormCRSUSDTtoETH.type)
    dp.register_message_handler(process_adressCRS_usdttoeth, state=FormCRSUSDTtoETH.adress)
    dp.register_message_handler(process_comfirmCRS_usdttoeth, state=FormCRSUSDTtoETH.comfirm)

    # = = = = USDT to SOL : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frusdt_tosol, text="call_tocrssolUSDT")
    dp.register_message_handler(process_numberCRS_usdttosol, state=FormCRSUSDTtoSOL.number)
    dp.register_message_handler(process_typeCRS_usdttosol, state=FormCRSUSDTtoSOL.type)
    dp.register_message_handler(process_adressCRS_usdttosol, state=FormCRSUSDTtoSOL.adress)
    dp.register_message_handler(process_comfirmCRS_usdttosol, state=FormCRSUSDTtoSOL.comfirm)

    # = = = = USDT to BNB : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frusdt_tobnb, text="call_tocrsbnbUSDT")
    dp.register_message_handler(process_numberCRS_usdttobnb, state=FormCRSUSDTtoBNB.number)
    dp.register_message_handler(process_typeCRS_usdttobnb, state=FormCRSUSDTtoBNB.type)
    dp.register_message_handler(process_adressCRS_usdttobnb, state=FormCRSUSDTtoBNB.adress)
    dp.register_message_handler(process_comfirmCRS_usdttobnb, state=FormCRSUSDTtoBNB.comfirm)

    # = = = = USDT to CARDANO : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frusdt_tocardano, text="call_tocrscardanoUSDT")
    dp.register_message_handler(process_numberCRS_usdttocardano, state=FormCRSUSDTtoCARDANO.number)
    dp.register_message_handler(process_typeCRS_usdttocardano, state=FormCRSUSDTtoCARDANO.type)
    dp.register_message_handler(process_adressCRS_usdttocardano, state=FormCRSUSDTtoCARDANO.adress)
    dp.register_message_handler(process_comfirmCRS_usdttocardano, state=FormCRSUSDTtoCARDANO.comfirm)

    # = = = = USDT to TRON : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frusdt_totron, text="call_tocrstronUSDT")
    dp.register_message_handler(process_numberCRS_usdttotron, state=FormCRSUSDTtoTRON.number)
    dp.register_message_handler(process_typeCRS_usdttotron, state=FormCRSUSDTtoTRON.type)
    dp.register_message_handler(process_adressCRS_usdttotron, state=FormCRSUSDTtoTRON.adress)
    dp.register_message_handler(process_comfirmCRS_usdttotron, state=FormCRSUSDTtoTRON.comfirm)

    # = = = = USDT to BUSD : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frusdt_tobusd, text="call_tocrsbusdUSDT")
    dp.register_message_handler(process_numberCRS_usdttobusd, state=FormCRSUSDTtoBUSD.number)
    dp.register_message_handler(process_typeCRS_usdttobusd, state=FormCRSUSDTtoBUSD.type)
    dp.register_message_handler(process_adressCRS_usdttobusd, state=FormCRSUSDTtoBUSD.adress)
    dp.register_message_handler(process_comfirmCRS_usdttobusd, state=FormCRSUSDTtoBUSD.comfirm)

    # = = = = USDT to POLKADOT : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frusdt_topolkadot, text="call_tocrspolkadotUSDT")
    dp.register_message_handler(process_numberCRS_usdttopolkadot, state=FormCRSUSDTtoPOLKADOT.number)
    dp.register_message_handler(process_typeCRS_usdttopolkadot, state=FormCRSUSDTtoPOLKADOT.type)
    dp.register_message_handler(process_adressCRS_usdttopolkadot, state=FormCRSUSDTtoPOLKADOT.adress)
    dp.register_message_handler(process_comfirmCRS_usdttopolkadot, state=FormCRSUSDTtoPOLKADOT.comfirm)

    # = = = = USDT to MATIC : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frusdt_tomatic, text="call_tocrsmaticUSDT")
    dp.register_message_handler(process_numberCRS_usdttomatic, state=FormCRSUSDTtoMATIC.number)
    dp.register_message_handler(process_typeCRS_usdttomatic, state=FormCRSUSDTtoMATIC.type)
    dp.register_message_handler(process_adressCRS_usdttomatic, state=FormCRSUSDTtoMATIC.adress)
    dp.register_message_handler(process_comfirmCRS_usdttomatic, state=FormCRSUSDTtoMATIC.comfirm)

    # = = = = BNB to BTC : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frbnb_tobtc, text="call_tocrsbitcoinBNB")
    dp.register_message_handler(process_numberCRS_bnbtobtc, state=FormCRSBNBtoBTC.number)
    dp.register_message_handler(process_typeCRS_bnbtobtc, state=FormCRSBNBtoBTC.type)
    dp.register_message_handler(process_adressCRS_bnbtobtc, state=FormCRSBNBtoBTC.adress)
    dp.register_message_handler(process_comfirmCRS_bnbtobtc, state=FormCRSBNBtoBTC.comfirm)

    # = = = = BNB to ETH : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frbnb_toeth, text="call_tocrsethereumBNB")
    dp.register_message_handler(process_numberCRS_bnbtoeth, state=FormCRSBNBtoETH.number)
    dp.register_message_handler(process_typeCRS_bnbtoeth, state=FormCRSBNBtoETH.type)
    dp.register_message_handler(process_adressCRS_bnbtoeth, state=FormCRSBNBtoETH.adress)
    dp.register_message_handler(process_comfirmCRS_bnbtoeth, state=FormCRSBNBtoETH.comfirm)

    # = = = = BNB to SOL : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frbnb_tosol, text="call_tocrssolBNB")
    dp.register_message_handler(process_numberCRS_bnbtosol, state=FormCRSBNBtoSOL.number)
    dp.register_message_handler(process_typeCRS_bnbtosol, state=FormCRSBNBtoSOL.type)
    dp.register_message_handler(process_adressCRS_bnbtosol, state=FormCRSBNBtoSOL.adress)
    dp.register_message_handler(process_comfirmCRS_bnbtosol, state=FormCRSBNBtoSOL.comfirm)

    # = = = = BNB to USDT : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frbnb_tousdt, text="call_tocrsusdtBNB")
    dp.register_message_handler(process_numberCRS_bnbtousdt, state=FormCRSBNBtoUSDT.number)
    dp.register_message_handler(process_typeCRS_bnbtousdt, state=FormCRSBNBtoUSDT.type)
    dp.register_message_handler(process_adressCRS_bnbtousdt, state=FormCRSBNBtoUSDT.adress)
    dp.register_message_handler(process_comfirmCRS_bnbtousdt, state=FormCRSBNBtoUSDT.comfirm)

    # = = = = BNB to CARDANO : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frbnb_tocardano, text="call_tocrscardanoBNB")
    dp.register_message_handler(process_numberCRS_bnbtocardano, state=FormCRSBNBtoCARDANO.number)
    dp.register_message_handler(process_typeCRS_bnbtocardano, state=FormCRSBNBtoCARDANO.type)
    dp.register_message_handler(process_adressCRS_bnbtocardano, state=FormCRSBNBtoCARDANO.adress)
    dp.register_message_handler(process_comfirmCRS_bnbtocardano, state=FormCRSBNBtoCARDANO.comfirm)

    # = = = = BNB to TRON : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frbnb_totron, text="call_tocrstronBNB")
    dp.register_message_handler(process_numberCRS_bnbtotron, state=FormCRSBNBtoTRON.number)
    dp.register_message_handler(process_typeCRS_bnbtotron, state=FormCRSBNBtoTRON.type)
    dp.register_message_handler(process_adressCRS_bnbtotron, state=FormCRSBNBtoTRON.adress)
    dp.register_message_handler(process_comfirmCRS_bnbtotron, state=FormCRSBNBtoTRON.comfirm)

    # = = = = BNB to BUSD : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frbnb_tobusd, text="call_tocrsbusdBNB")
    dp.register_message_handler(process_numberCRS_bnbtobusd, state=FormCRSBNBtoBUSD.number)
    dp.register_message_handler(process_typeCRS_bnbtobusd, state=FormCRSBNBtoBUSD.type)
    dp.register_message_handler(process_adressCRS_bnbtobusd, state=FormCRSBNBtoBUSD.adress)
    dp.register_message_handler(process_comfirmCRS_bnbtobusd, state=FormCRSBNBtoBUSD.comfirm)

    # = = = = BNB to POLKADOT : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frbnb_topolkadot, text="call_tocrspolkadotBNB")
    dp.register_message_handler(process_numberCRS_bnbtopolkadot, state=FormCRSBNBtoPOLKADOT.number)
    dp.register_message_handler(process_typeCRS_bnbtopolkadot, state=FormCRSBNBtoPOLKADOT.type)
    dp.register_message_handler(process_adressCRS_bnbtopolkadot, state=FormCRSBNBtoPOLKADOT.adress)
    dp.register_message_handler(process_comfirmCRS_bnbtopolkadot, state=FormCRSBNBtoPOLKADOT.comfirm)

    # = = = = BNB to MATIC : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frbnb_tomatic, text="call_tocrsmaticBNB")
    dp.register_message_handler(process_numberCRS_bnbtomatic, state=FormCRSBNBtoMATIC.number)
    dp.register_message_handler(process_typeCRS_bnbtomatic, state=FormCRSBNBtoMATIC.type)
    dp.register_message_handler(process_adressCRS_bnbtomatic, state=FormCRSBNBtoMATIC.adress)
    dp.register_message_handler(process_comfirmCRS_bnbtomatic, state=FormCRSBNBtoMATIC.comfirm)

    # = = = = CARDANO to BTC : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frcardano_tobtc, text="call_tocrsbitcoinCARDANO")
    dp.register_message_handler(process_numberCRS_cardanotobtc, state=FormCRSCARDANOtoBTC.number)
    dp.register_message_handler(process_typeCRS_cardanotobtc, state=FormCRSCARDANOtoBTC.type)
    dp.register_message_handler(process_adressCRS_cardanotobtc, state=FormCRSCARDANOtoBTC.adress)
    dp.register_message_handler(process_comfirmCRS_cardanotobtc, state=FormCRSCARDANOtoBTC.comfirm)

    # = = = = CARDANO to ETH : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frcardano_toeth, text="call_tocrsethereumCARDANO")
    dp.register_message_handler(process_numberCRS_cardanotoeth, state=FormCRSCARDANOtoETH.number)
    dp.register_message_handler(process_typeCRS_cardanotoeth, state=FormCRSCARDANOtoETH.type)
    dp.register_message_handler(process_adressCRS_cardanotoeth, state=FormCRSCARDANOtoETH.adress)
    dp.register_message_handler(process_comfirmCRS_cardanotoeth, state=FormCRSCARDANOtoETH.comfirm)

    # = = = = CARDANO to SOL : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frcardano_tosol, text="call_tocrssolCARDANO")
    dp.register_message_handler(process_numberCRS_cardanotosol, state=FormCRSCARDANOtoSOL.number)
    dp.register_message_handler(process_typeCRS_cardanotosol, state=FormCRSCARDANOtoSOL.type)
    dp.register_message_handler(process_adressCRS_cardanotosol, state=FormCRSCARDANOtoSOL.adress)
    dp.register_message_handler(process_comfirmCRS_cardanotosol, state=FormCRSCARDANOtoSOL.comfirm)

    # = = = = CARDANO to USDT : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frcardano_tousdt, text="call_tocrsusdtCARDANO")
    dp.register_message_handler(process_numberCRS_cardanotousdt, state=FormCRSCARDANOtoUSDT.number)
    dp.register_message_handler(process_typeCRS_cardanotousdt, state=FormCRSCARDANOtoUSDT.type)
    dp.register_message_handler(process_adressCRS_cardanotousdt, state=FormCRSCARDANOtoUSDT.adress)
    dp.register_message_handler(process_comfirmCRS_cardanotousdt, state=FormCRSCARDANOtoUSDT.comfirm)

    # = = = = CARDANO to BNB : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frcardano_tobnb, text="call_tocrsbnbCARDANO")
    dp.register_message_handler(process_numberCRS_cardanotobnb, state=FormCRSCARDANOtoBNB.number)
    dp.register_message_handler(process_typeCRS_cardanotobnb, state=FormCRSCARDANOtoBNB.type)
    dp.register_message_handler(process_adressCRS_cardanotobnb, state=FormCRSCARDANOtoBNB.adress)
    dp.register_message_handler(process_comfirmCRS_cardanotobnb, state=FormCRSCARDANOtoBNB.comfirm)

    # = = = = CARDANO to TROB : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frcardano_totron, text="call_tocrstronCARDANO")
    dp.register_message_handler(process_numberCRS_cardanototron, state=FormCRSCARDANOtoTRON.number)
    dp.register_message_handler(process_typeCRS_cardanototron, state=FormCRSCARDANOtoTRON.type)
    dp.register_message_handler(process_adressCRS_cardanototron, state=FormCRSCARDANOtoTRON.adress)
    dp.register_message_handler(process_comfirmCRS_cardanototron, state=FormCRSCARDANOtoTRON.comfirm)

    # = = = = CARDANO to BUSD : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frcardano_tobusd, text="call_tocrsbusdCARDANO")
    dp.register_message_handler(process_numberCRS_cardanotobusd, state=FormCRSCARDANOtoBUSD.number)
    dp.register_message_handler(process_typeCRS_cardanotobusd, state=FormCRSCARDANOtoBUSD.type)
    dp.register_message_handler(process_adressCRS_cardanotobusd, state=FormCRSCARDANOtoBUSD.adress)
    dp.register_message_handler(process_comfirmCRS_cardanotobusd, state=FormCRSCARDANOtoBUSD.comfirm)

    # = = = = CARDANO to POLKADOT : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frcardano_topolkadot, text="call_tocrspolkadotCARDANO")
    dp.register_message_handler(process_numberCRS_cardanotopolkadot, state=FormCRSCARDANOtoPOLKADOT.number)
    dp.register_message_handler(process_typeCRS_cardanotopolkadot, state=FormCRSCARDANOtoPOLKADOT.type)
    dp.register_message_handler(process_adressCRS_cardanotopolkadot, state=FormCRSCARDANOtoPOLKADOT.adress)
    dp.register_message_handler(process_comfirmCRS_cardanotopolkadot, state=FormCRSCARDANOtoPOLKADOT.comfirm)

    # = = = = CARDANO to MATIC : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frcardano_tomatic, text="call_tocrsmaticCARDANO")
    dp.register_message_handler(process_numberCRS_cardanotomatic, state=FormCRSPOLKADOTtoMATIC.number)
    dp.register_message_handler(process_typeCRS_cardanotomatic, state=FormCRSPOLKADOTtoMATIC.type)
    dp.register_message_handler(process_adressCRS_cardanotomatic, state=FormCRSPOLKADOTtoMATIC.adress)
    dp.register_message_handler(process_comfirmCRS_cardanotomatic, state=FormCRSPOLKADOTtoMATIC.comfirm)

    # = = = = TRON to BTC : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frtron_tobitcoin, text="call_tocrsbitcoinTRON")
    dp.register_message_handler(process_numberCRS_trontobtc, state=FormCRSTRONtoBTC.number)
    dp.register_message_handler(process_typeCRS_trontobtc, state=FormCRSTRONtoBTC.type)
    dp.register_message_handler(process_adressCRS_trontobtc, state=FormCRSTRONtoBTC.adress)
    dp.register_message_handler(process_comfirmCRS_trontobtc, state=FormCRSTRONtoBTC.comfirm)

    # = = = = TRON to ETH : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frtron_toethereum, text="call_tocrsethereumTRON")
    dp.register_message_handler(process_numberCRS_trontoeth, state=FormCRSTRONtoETH.number)
    dp.register_message_handler(process_typeCRS_trontoeth, state=FormCRSTRONtoETH.type)
    dp.register_message_handler(process_adressCRS_trontoeth, state=FormCRSTRONtoETH.adress)
    dp.register_message_handler(process_comfirmCRS_trontoeth, state=FormCRSTRONtoETH.comfirm)

    # = = = = TRON to SOL : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frtron_tosol, text="call_tocrssolTRON")
    dp.register_message_handler(process_numberCRS_trontosol, state=FormCRSTRONtoSOL.number)
    dp.register_message_handler(process_typeCRS_trontosol, state=FormCRSTRONtoSOL.type)
    dp.register_message_handler(process_adressCRS_trontosol, state=FormCRSTRONtoSOL.adress)
    dp.register_message_handler(process_comfirmCRS_trontosol, state=FormCRSTRONtoSOL.comfirm)

    # = = = = TRON to USDT : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frtron_tousdt, text="call_tocrsusdtTRON")
    dp.register_message_handler(process_numberCRS_trontousdt, state=FormCRSTRONtoUSDT.number)
    dp.register_message_handler(process_typeCRS_trontousdt, state=FormCRSTRONtoUSDT.type)
    dp.register_message_handler(process_adressCRS_trontousdt, state=FormCRSTRONtoUSDT.adress)
    dp.register_message_handler(process_comfirmCRS_trontousdt, state=FormCRSTRONtoUSDT.comfirm)

    # = = = = TRON to BNB : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frtron_tobnb, text="call_tocrsbnbTRON")
    dp.register_message_handler(process_numberCRS_trontobnb, state=FormCRSTRONtoBNB.number)
    dp.register_message_handler(process_typeCRS_trontobnb, state=FormCRSTRONtoBNB.type)
    dp.register_message_handler(process_adressCRS_trontobnb, state=FormCRSTRONtoBNB.adress)
    dp.register_message_handler(process_comfirmCRS_trontobnb, state=FormCRSTRONtoBNB.comfirm)

    # = = = = TRON to CARDANO : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frtron_tocardano, text="call_tocrscardanoTRON")
    dp.register_message_handler(process_numberCRS_trontocardano, state=FormCRSTRONtoCARDANO.number)
    dp.register_message_handler(process_typeCRS_trontocardano, state=FormCRSTRONtoCARDANO.type)
    dp.register_message_handler(process_adressCRS_trontocardano, state=FormCRSTRONtoCARDANO.adress)
    dp.register_message_handler(process_comfirmCRS_trontocardano, state=FormCRSTRONtoCARDANO.comfirm)

    # = = = = TRON to BUSD : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frtron_tobusd, text="call_tocrsbusdTRON")
    dp.register_message_handler(process_numberCRS_trontobusd, state=FormCRSTRONtoBUSD.number)
    dp.register_message_handler(process_typeCRS_trontobusd, state=FormCRSTRONtoBUSD.type)
    dp.register_message_handler(process_adressCRS_trontobusd, state=FormCRSTRONtoBUSD.adress)
    dp.register_message_handler(process_comfirmCRS_trontobusd, state=FormCRSTRONtoBUSD.comfirm)

    # = = = = TRON to POLKADOT : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frtron_topolkadot, text="call_tocrspolkadotTRON")
    dp.register_message_handler(process_numberCRS_trontopolkadot, state=FormCRSTRONtoPOLKADOT.number)
    dp.register_message_handler(process_typeCRS_trontopolkadot, state=FormCRSTRONtoPOLKADOT.type)
    dp.register_message_handler(process_adressCRS_trontopolkadot, state=FormCRSTRONtoPOLKADOT.adress)
    dp.register_message_handler(process_comfirmCRS_trontopolkadot, state=FormCRSTRONtoPOLKADOT.comfirm)

    # = = = = TRON to MATIC : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frtron_tomatic, text="call_tocrsmaticTRON")
    dp.register_message_handler(process_numberCRS_trontomatic, state=FormCRSTRONtoMATIC.number)
    dp.register_message_handler(process_typeCRS_trontomatic, state=FormCRSTRONtoMATIC.type)
    dp.register_message_handler(process_adressCRS_trontomatic, state=FormCRSTRONtoMATIC.adress)
    dp.register_message_handler(process_comfirmCRS_trontomatic, state=FormCRSTRONtoMATIC.comfirm)

    # = = = = BUSD to BTC : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frbusd_tobtc, text="call_tocrsbitcoinBUSD")
    dp.register_message_handler(process_numberCRS_busdtobtc, state=FormCRSBUSDtoBTC.number)
    dp.register_message_handler(process_typeCRS_busdtobtc, state=FormCRSBUSDtoBTC.type)
    dp.register_message_handler(process_adressCRS_busdtobtc, state=FormCRSBUSDtoBTC.adress)
    dp.register_message_handler(process_comfirmCRS_busdtobtc, state=FormCRSBUSDtoBTC.comfirm)

    # = = = = BUSD to ETH : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frbusd_toeth, text="call_tocrsethereumBUSD")
    dp.register_message_handler(process_numberCRS_busdtoeth, state=FormCRSBUSDtoETH.number)
    dp.register_message_handler(process_typeCRS_busdtoeth, state=FormCRSBUSDtoETH.type)
    dp.register_message_handler(process_adressCRS_busdtoeth, state=FormCRSBUSDtoETH.adress)
    dp.register_message_handler(process_comfirmCRS_busdtoeth, state=FormCRSBUSDtoETH.comfirm)

    # = = = = BUSD to SOL : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frbusd_tosol, text="call_tocrssolBUSD")
    dp.register_message_handler(process_numberCRS_busdtosol, state=FormCRSBUSDtoSOL.number)
    dp.register_message_handler(process_typeCRS_busdtosol, state=FormCRSBUSDtoSOL.type)
    dp.register_message_handler(process_adressCRS_busdtosol, state=FormCRSBUSDtoSOL.adress)
    dp.register_message_handler(process_comfirmCRS_busdtosol, state=FormCRSBUSDtoSOL.comfirm)

    # = = = = BUSD to USDT : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frbusd_tousdt, text="call_tocrsusdtBUSD")
    dp.register_message_handler(process_numberCRS_busdtousdt, state=FormCRSBUSDtoUSDT.number)
    dp.register_message_handler(process_typeCRS_busdtousdt, state=FormCRSBUSDtoUSDT.type)
    dp.register_message_handler(process_adressCRS_busdtousdt, state=FormCRSBUSDtoUSDT.adress)
    dp.register_message_handler(process_comfirmCRS_busdtousdt, state=FormCRSBUSDtoUSDT.comfirm)

    # = = = = BUSD to BNB : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frbusd_tobnb, text="call_tocrsbnbBUSD")
    dp.register_message_handler(process_numberCRS_busdtobnb, state=FormCRSBUSDtoBNB.number)
    dp.register_message_handler(process_typeCRS_busdtobnb, state=FormCRSBUSDtoBNB.type)
    dp.register_message_handler(process_adressCRS_busdtobnb, state=FormCRSBUSDtoBNB.adress)
    dp.register_message_handler(process_comfirmCRS_busdtobnb, state=FormCRSBUSDtoBNB.comfirm)

    # = = = = BUSD to CARDANO : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frbusd_tocardano, text="call_tocrscardanoBUSD")
    dp.register_message_handler(process_numberCRS_busdtocardano, state=FormCRSBUSDtoCARDANO.number)
    dp.register_message_handler(process_typeCRS_busdtocardano, state=FormCRSBUSDtoCARDANO.type)
    dp.register_message_handler(process_adressCRS_busdtocardano, state=FormCRSBUSDtoCARDANO.adress)
    dp.register_message_handler(process_comfirmCRS_busdtocardano, state=FormCRSBUSDtoCARDANO.comfirm)

    # = = = = BUSD to TRON : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frbusd_totron, text="call_tocrstronBUSD")
    dp.register_message_handler(process_numberCRS_busdtotron, state=FormCRSBUSDtoTRON.number)
    dp.register_message_handler(process_typeCRS_busdtotron, state=FormCRSBUSDtoTRON.type)
    dp.register_message_handler(process_adressCRS_busdtotron, state=FormCRSBUSDtoTRON.adress)
    dp.register_message_handler(process_comfirmCRS_busdtotron, state=FormCRSBUSDtoTRON.comfirm)

    # = = = = BUSD to POLKADOT : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frbusd_topolkadot, text="call_tocrspolkadotBUSD")
    dp.register_message_handler(process_numberCRS_busdtopolkadot, state=FormCRSBUSDtoPOLKADOT.number)
    dp.register_message_handler(process_typeCRS_busdtopolkadot, state=FormCRSBUSDtoPOLKADOT.type)
    dp.register_message_handler(process_adressCRS_busdtopolkadot, state=FormCRSBUSDtoPOLKADOT.adress)
    dp.register_message_handler(process_comfirmCRS_busdtopolkadot, state=FormCRSBUSDtoPOLKADOT.comfirm)

    # = = = = BUSD to MATIC : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frbusd_tomatic, text="call_tocrsmaticBUSD")
    dp.register_message_handler(process_numberCRS_busdtomatic, state=FormCRSBUSDtoMATIC.number)
    dp.register_message_handler(process_typeCRS_busdtomatic, state=FormCRSBUSDtoMATIC.type)
    dp.register_message_handler(process_adressCRS_busdtomatic, state=FormCRSBUSDtoMATIC.adress)
    dp.register_message_handler(process_comfirmCRS_busdtomatic, state=FormCRSBUSDtoMATIC.comfirm)

    # = = = = POLKADOT to BTC : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frpolkadot_tobtc, text="call_tocrsbitcoinPOLKADOT")
    dp.register_message_handler(process_numberCRS_polkadottobtc, state=FormCRSPOLKADOTtoBTC.number)
    dp.register_message_handler(process_typeCRS_polkadottobtc, state=FormCRSPOLKADOTtoBTC.type)
    dp.register_message_handler(process_adressCRS_polkadottobtc, state=FormCRSPOLKADOTtoBTC.adress)
    dp.register_message_handler(process_comfirmCRS_polkadottobtc, state=FormCRSPOLKADOTtoBTC.comfirm)

    # = = = = POLKADOT to ETH : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frpolkadot_toeth, text="call_tocrsethereumPOLKADOT")
    dp.register_message_handler(process_numberCRS_polkadottoeth, state=FormCRSPOLKADOTtoETH.number)
    dp.register_message_handler(process_typeCRS_polkadottoeth, state=FormCRSPOLKADOTtoETH.type)
    dp.register_message_handler(process_adressCRS_polkadottoeth, state=FormCRSPOLKADOTtoETH.adress)
    dp.register_message_handler(process_comfirmCRS_polkadottoeth, state=FormCRSPOLKADOTtoETH.comfirm)

    # = = = = POLKADOT to SOL : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frpolkadot_tosol, text="call_tocrssolPOLKADOT")
    dp.register_message_handler(process_numberCRS_polkadottosol, state=FormCRSPOLKADOTtoSOL.number)
    dp.register_message_handler(process_typeCRS_polkadottosol, state=FormCRSPOLKADOTtoSOL.type)
    dp.register_message_handler(process_adressCRS_polkadottosol, state=FormCRSPOLKADOTtoSOL.adress)
    dp.register_message_handler(process_comfirmCRS_polkadottosol, state=FormCRSPOLKADOTtoSOL.comfirm)

    # = = = = POLKADOT to USDT : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frpolkadot_tousdt, text="call_tocrsusdtPOLKADOT")
    dp.register_message_handler(process_numberCRS_polkadottousdt, state=FormCRSPOLKADOTtoUSDT.number)
    dp.register_message_handler(process_typeCRS_polkadottousdt, state=FormCRSPOLKADOTtoUSDT.type)
    dp.register_message_handler(process_adressCRS_polkadottousdt, state=FormCRSPOLKADOTtoUSDT.adress)
    dp.register_message_handler(process_comfirmCRS_polkadottousdt, state=FormCRSPOLKADOTtoUSDT.comfirm)

    # = = = = POLKADOT to BNB : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frpolkadot_tobnb, text="call_tocrsbnbPOLKADOT")
    dp.register_message_handler(process_numberCRS_polkadottobnb, state=FormCRSPOLKADOTtoBNB.number)
    dp.register_message_handler(process_typeCRS_polkadottobnb, state=FormCRSPOLKADOTtoBNB.type)
    dp.register_message_handler(process_adressCRS_polkadottobnb, state=FormCRSPOLKADOTtoBNB.adress)
    dp.register_message_handler(process_comfirmCRS_polkadottobnb, state=FormCRSPOLKADOTtoBNB.comfirm)

    # = = = = POLKADOT to CARDANO : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frpolkadot_tocardano, text="call_tocrscardanoPOLKADOT")
    dp.register_message_handler(process_numberCRS_polkadottocardano, state=FormCRSPOLKADOTtoCARDANO.number)
    dp.register_message_handler(process_typeCRS_polkadottocardano, state=FormCRSPOLKADOTtoCARDANO.type)
    dp.register_message_handler(process_adressCRS_polkadottocardano, state=FormCRSPOLKADOTtoCARDANO.adress)
    dp.register_message_handler(process_comfirmCRS_polkadottocardano, state=FormCRSPOLKADOTtoCARDANO.comfirm)

    # = = = = POLKADOT to BUSD : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frpolkadot_tobusd, text="call_tocrsbusdPOLKADOT")
    dp.register_message_handler(process_numberCRS_polkadottobusd, state=FormCRSPOLKADOTtoBUSD.number)
    dp.register_message_handler(process_typeCRS_polkadottobusd, state=FormCRSPOLKADOTtoBUSD.type)
    dp.register_message_handler(process_adressCRS_polkadottobusd, state=FormCRSPOLKADOTtoBUSD.adress)
    dp.register_message_handler(process_comfirmCRS_polkadottobusd, state=FormCRSPOLKADOTtoBUSD.comfirm)

    # = = = = POLKADOT to TRON : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frpolkadot_totron, text="call_tocrstronPOLKADOT")
    dp.register_message_handler(process_numberCRS_polkadottotron, state=FormCRSPOLKADOTtoTRON.number)
    dp.register_message_handler(process_typeCRS_polkadottotron, state=FormCRSPOLKADOTtoTRON.type)
    dp.register_message_handler(process_adressCRS_polkadottotron, state=FormCRSPOLKADOTtoTRON.adress)
    dp.register_message_handler(process_comfirmCRS_polkadottotron, state=FormCRSPOLKADOTtoTRON.comfirm)

    # = = = = POLKADOT to MATIC : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frpolkadot_tomatic, text="call_tocrsmaticPOLKADOT")
    dp.register_message_handler(process_numberCRS_polkadottomatic, state=FormCRSPOLKADOTtoMATIC.number)
    dp.register_message_handler(process_typeCRS_polkadottomatic, state=FormCRSPOLKADOTtoMATIC.type)
    dp.register_message_handler(process_adressCRS_polkadottomatic, state=FormCRSPOLKADOTtoMATIC.adress)
    dp.register_message_handler(process_comfirmCRS_polkadottomatic, state=FormCRSPOLKADOTtoMATIC.comfirm)

    # = = = = MATIC to BTC : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frmatic_tobtc, text="call_tocrsbitcoinMATIC")
    dp.register_message_handler(process_numberCRS_matictobtc, state=FormCRSMATICtoBTC.number)
    dp.register_message_handler(process_typeCRS_matictobtc, state=FormCRSMATICtoBTC.type)
    dp.register_message_handler(process_adressCRS_matictobtc, state=FormCRSMATICtoBTC.adress)
    dp.register_message_handler(process_comfirmCRS_matictobtc, state=FormCRSMATICtoBTC.comfirm)

    # = = = = MATIC to ETH : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frmatic_toeth, text="call_tocrsethereumMATIC")
    dp.register_message_handler(process_numberCRS_matictoeth, state=FormCRSMATICtoETH.number)
    dp.register_message_handler(process_typeCRS_matictoeth, state=FormCRSMATICtoETH.type)
    dp.register_message_handler(process_adressCRS_matictoeth, state=FormCRSMATICtoETH.adress)
    dp.register_message_handler(process_comfirmCRS_matictoeth, state=FormCRSMATICtoETH.comfirm)

    # = = = = MATIC to SOL : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frmatic_tosol, text="call_tocrssolMATIC")
    dp.register_message_handler(process_numberCRS_matictosol, state=FormCRSMATICtoSOL.number)
    dp.register_message_handler(process_typeCRS_matictosol, state=FormCRSMATICtoSOL.type)
    dp.register_message_handler(process_adressCRS_matictosol, state=FormCRSMATICtoSOL.adress)
    dp.register_message_handler(process_comfirmCRS_matictosol, state=FormCRSMATICtoSOL.comfirm)

    # = = = = MATIC to USDT : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frmatic_tousdt, text="call_tocrsusdtMATIC")
    dp.register_message_handler(process_numberCRS_matictousdt, state=FormCRSMATICtoUSDT.number)
    dp.register_message_handler(process_typeCRS_matictousdt, state=FormCRSMATICtoUSDT.type)
    dp.register_message_handler(process_adressCRS_matictousdt, state=FormCRSMATICtoUSDT.adress)
    dp.register_message_handler(process_comfirmCRS_matictousdt, state=FormCRSMATICtoUSDT.comfirm)

    # = = = = MATIC to BNB : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frmatic_tobnb, text="call_tocrsbnbMATIC")
    dp.register_message_handler(process_numberCRS_matictobnb, state=FormCRSMATICtoBNB.number)
    dp.register_message_handler(process_typeCRS_matictobnb, state=FormCRSMATICtoBNB.type)
    dp.register_message_handler(process_adressCRS_matictobnb, state=FormCRSMATICtoBNB.adress)
    dp.register_message_handler(process_comfirmCRS_matictobnb, state=FormCRSMATICtoBNB.comfirm)

    # = = = = MATIC to CARDANO : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frmatic_tocardano, text="call_tocrscardanoMATIC")
    dp.register_message_handler(process_numberCRS_matictocardano, state=FormCRSMATICtoCARDANO.number)
    dp.register_message_handler(process_typeCRS_matictocardano, state=FormCRSMATICtoCARDANO.type)
    dp.register_message_handler(process_adressCRS_matictocardano, state=FormCRSMATICtoCARDANO.adress)
    dp.register_message_handler(process_comfirmCRS_matictocardano, state=FormCRSMATICtoCARDANO.comfirm)

    # = = = = MATIC to BUSD : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frmatic_tobusd, text="call_tocrsbusdMATIC")
    dp.register_message_handler(process_numberCRS_matictobusd, state=FormCRSMATICtoBUSD.number)
    dp.register_message_handler(process_typeCRS_matictobusd, state=FormCRSMATICtoBUSD.type)
    dp.register_message_handler(process_adressCRS_matictobusd, state=FormCRSMATICtoBUSD.adress)
    dp.register_message_handler(process_comfirmCRS_matictobusd, state=FormCRSMATICtoBUSD.comfirm)

    # = = = = MATIC to TRON : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frmatic_totron, text="call_tocrstronMATIC")
    dp.register_message_handler(process_numberCRS_matictotron, state=FormCRSMATICtoTRON.number)
    dp.register_message_handler(process_typeCRS_matictotron, state=FormCRSMATICtoTRON.type)
    dp.register_message_handler(process_adressCRS_matictotron, state=FormCRSMATICtoTRON.adress)
    dp.register_message_handler(process_comfirmCRS_matictotron, state=FormCRSMATICtoTRON.comfirm)

    # = = = = MATIC to POLKADOT : EXCHANGE = = = = = #
    dp.register_callback_query_handler(call_crosschain_frmatic_topolkadot, text="call_tocrspolkadotMATIC")
    dp.register_message_handler(process_numberCRS_matictopolkadot, state=FormCRSMATICtoPOLKADOT.number)
    dp.register_message_handler(process_typeCRS_matictopolkadot, state=FormCRSMATICtoPOLKADOT.type)
    dp.register_message_handler(process_adressCRS_matictopolkadot, state=FormCRSMATICtoPOLKADOT.adress)
    dp.register_message_handler(process_comfirmCRS_matictopolkadot, state=FormCRSMATICtoPOLKADOT.comfirm)
