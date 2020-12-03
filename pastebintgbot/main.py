from TelegramBot import TelegramBot
import coloredlogs
import logging
coloredlogs.install()
logging.basicConfig(level=logging.INFO)


class PasetbinTGBot:
    def __init__(self):
        self._telegram = TelegramBot()


if __name__ == '__main__':
    bot = PasetbinTGBot()
