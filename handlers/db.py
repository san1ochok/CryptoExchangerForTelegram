# = = = = = = = DATABASE : ALL DATA (WALLET BALANCES) = = = = = = = #
import sqlite3

con = sqlite3.connect('database.db')
cursor = con.cursor()


def CreateDB():
    cursor = con.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users(name TEXT, id INT, timeUSDT INT, bitcoin FLOAT, ethereum FLOAT, "
        "solana FLOAT, usdt FLOAT, bnb FLOAT, cardano FLOAT, tron FLOAT, busd FLOAT, polkadot FLOAT, matic FLOAT, "
        "cwd FLOAT, watt FLOAT, STusdt FLOAT, STtron FLOAT, STsolana FLOAT, STpolkadot FLOAT, STbnb FLOAT, timeTRON, "
        "timeSOLANA, timePOLKADOT, timeBNB)")
    con.commit()


def UpdateValue(val_name, new_val, id):
    for row in cursor.execute(f"SELECT {val_name} FROM users where id={id}"):
        new = row[0] + new_val
        cursor.execute(f"UPDATE users SET {val_name}={new} where id={id}")
        con.commit()


def InsertValue(name, id):
    cursor.execute(
        f'INSERT INTO users VALUES ("{name}", {id}, 0, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, '
        f'0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0, 0, 0, 0)')
    con.commit()  # 20
