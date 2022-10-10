# -*- coding: utf-8 -*-
# = = = = = = = IMPORTS = = = = = = = #
from aiogram import Dispatcher, Bot, executor
from aiogram.utils.exceptions import NetworkError
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
import config as cfg
from handlers import db
from handlers import p2p_exchanger, wallet, aboutus, staking, start_place, crosschain_exchanger

# = = = = = = = BOT START = = = = = = = #
logging.basicConfig(filename="logs.log", level=logging.INFO, format='%(asctime)s - %(levelname)s -%(message)s')
db.CreateDB()
storage = MemoryStorage()
bot = Bot(token=cfg.token, parse_mode=cfg.parse_mode)
dp = Dispatcher(bot, storage=storage)

p2p_exchanger.register_handlers_p2pexchanger(dp)
wallet.register_handlers_wallet(dp)
aboutus.register_handlers_aboutus(dp)
staking.register_handlers_staking(dp)
start_place.register_handlers_startplace(dp)
crosschain_exchanger.register_handlers_crosschain_exchanger(dp)

# = = = = = = = STABLE LOOP CONNECT = = = = = = = #
if __name__ == "__main__":
    try:
        executor.start_polling(dp, skip_updates=True)
        print("If you're reading this, you're lucky dude :D")
        print("Crypto Exchanger Bot successfully started!")
    except NetworkError:
        print("Not allowed connect to localhost ;(")
        print("Error: Low or Invalid Internet Connection")
        print("TECH: @alexndrev")
