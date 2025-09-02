from pyrogram import Client, filters
from pyrogram.errors import UsernameInvalid, UsernameOccupied, FloodWait, UsernameNotOccupied
from pyrogram.errors.exceptions.bad_request_400 import UsernameNotOccupied
from pyrogram.errors import RPCError
from pyrogram.enums import GiftForResaleOrder
from pyrogram.enums import ParseMode
import time,logging
import asyncio, requests
logging.basicConfig(
        level=logging.INFO,       
        format='%(asctime)s | %(levelname)s | %(message)s'
    )


async def main():
    api_id = '' # id
    api_hash = '' # hash
    app = Client(name='userbot', api_id=api_id,api_hash=api_hash)
    await app.start()
    starbalance = await app.get_stars_balance()
    print(f"Баланс звёзд: {starbalance}")
    while True:
        try:
            stars = []
            ids = []
            test = []
            gifts = await app.get_available_gifts()
            for gift in gifts:
                if gift.limited and gift.availability_remains > 0:
                   test.append([gift.id,gift.stars])
            if test:
                sortedgifts = sorted(test, key=lambda x: x[1], reverse=True)
                logging.info("нашел")
                for gift in sortedgifts:
                    starbalance = await app.get_stars_balance()
                    trs = 0
                    while starbalance >= gift[1] and trs < 5:
                        try:
                            await app.send_gift(chat_id="me",gift_id=gift[0],is_private=True)
                            logging.info(f"купил {gift[0]} за {gift[1]}")
                        except Exception as e:
                            starbalance = await app.get_stars_balance()
                            logging.info(f"Недачная попытка купить {gift[0]} за {gift[1]} | Баланс: {starbalance} | Причина: {e}")
                            trs += 1
                            await asyncio.sleep(2)
            else:
                logging.info(f"Ничего нового | Получил {len(gifts)} подарков |")

            await asyncio.sleep(2)
        except Exception as e:
            logging.error(e)
            await asyncio.sleep(2)
def a():
    if __name__ == "__main__":
        asyncio.run(main())

while True:
    try:
        a()
    except:
        a()
