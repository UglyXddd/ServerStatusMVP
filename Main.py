import pandas as pd
from aiogram.types import user
import userInterface
import excel
import ping_file
import schedule
import time
import threading
import tg_bot


def start_updataes():
    while 1:
        schedule.run_pending()
        time.sleep(1)


def rest_bot():
    pass


class Main:
    def __init__(self):
        pass

    def start_ui(self):
        return userInterface.main()

    def start_bot(self):
        return tg_bot.main()


if __name__ == "__main__":
    Main_class = Main()
    t1 = threading.Thread(target=Main_class.start_ui, daemon=True)
    t2 = threading.Thread(target=Main_class.start_bot, daemon=True)
    t1.start()
    t2.run()
    t1.join()


