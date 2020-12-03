import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from settings import TELEGRAM_TOKEN, HOST, PORT, WEBHOOK_URL
from Runner import Runner


class TelegramBot:

    def __init__(self):
        self.main()

    def author_command(self, update: Update, context: CallbackContext) -> None:
        """Send a message when the command /author is issued."""
        self.Runner.just_answer(update, "author")

    def start_command(self, update: Update, context: CallbackContext) -> None:
        """Send a message when the command /start is issued."""
        self.Runner.just_answer(update, "start")

    def help_command(self, update: Update, context: CallbackContext) -> None:
        """Send a message when the command /help is issued."""
        self.Runner.just_answer(update, "help")

    def receive_paste(self, update: Update, context: CallbackContext) -> None:
        """Receive the code to send to pastebin."""
        # TODO: open a new thread to process requirements for many users at the same time.
        self.Runner.process_paste(update)

    def main(self) -> None:
        """Start the bot."""
        self.updater = Updater(TELEGRAM_TOKEN, use_context=True)
        self.bot = self.updater.bot
        self.Runner = Runner(self.bot)

        # Get the dispatcher to register handlers
        dp = self.updater.dispatcher

        # Register handlers
        dp.add_handler(CommandHandler("paste", self.receive_paste))
        dp.add_handler(CommandHandler("author", self.author_command))
        dp.add_handler(CommandHandler(
            "start", self.start_command, filters=Filters.chat_type.private))
        dp.add_handler(CommandHandler(
            "help", self.help_command, filters=Filters.chat_type.private))
        dp.add_handler(MessageHandler(
            Filters.text & (~Filters.command) & Filters.chat_type.private, self.receive_paste))

        # Starting the webhook.
        self.updater.start_webhook(listen=HOST, port=PORT,
                                   url_path=TELEGRAM_TOKEN)
        self.updater.bot.set_webhook(f"{WEBHOOK_URL}/{TELEGRAM_TOKEN}")
        logging.info(
            f"Server started on {HOST}:{PORT}. Listening publicily on {WEBHOOK_URL}/<token>")

        # Wait for a signal
        self.updater.idle()

    @staticmethod
    def get_bot_username() -> str:
        """Return the bot username without '@'."""
        return "PastebinTGBot"
