import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from BotMessages import TELEGRAM_MESSAGES, TELEGRAM_MESSAGES_PT
from settings import TELEGRAM_TOKEN, HOST, PORT, WEBHOOK_URL
from PastebinUploader import PastebinUploader


class TelegramBot:
    def __init__(self):
        self.main()

    def _get_message(self, key: str, lang: str = "en"):
        if lang.startswith("pt"):
            return TELEGRAM_MESSAGES_PT[key]
        else:
            return TELEGRAM_MESSAGES[key]

    def start(self, update: Update, context: CallbackContext) -> None:
        """Send a message when the command /start is issued."""
        update.message.reply_text(
            self._get_message("start", update.message.from_user.language_code), parse_mode="HTML", disable_web_page_preview=True)

    def help_command(self, update: Update, context: CallbackContext) -> None:
        """Send a message when the command /help is issued."""
        update.message.reply_text(
            self._get_message('help', update.message.from_user.language_code), parse_mode="HTML", disable_web_page_preview=True)

    def receive_paste(self, update: Update, context: CallbackContext) -> None:
        """Receive the code, check if is it valid and start StickerSet creation"""
        # TODO: open a new thread to process requirements for many users at the same time.
        message = update.message.text
        usern = "@" + update.message.from_user.username
        lang = update.message.from_user.language_code
        message_id = update.message.message_id
        chat_id = update.message.chat.id
        logging.info(f"Received msg_id {message_id} from {usern} in {chat_id}")
        pastebinUp = PastebinUploader()
        url = pastebinUp.paste(message)
        if url == "":
            update.message.reply_text(
                self._get_message('paste_empty', lang), parse_mode="HTML", disable_web_page_preview=True)
            return
        message_to_send = self._get_message('sent', lang).format(usern, url)
        if self.check_delete_permission(chat_id):
            self.updater.bot.send_message(
                chat_id, message_to_send, parse_mode="HTML", disable_web_page_preview=True)
            self.updater.bot.delete_message(chat_id, message_id)
        else:
            update.message.reply_text(
                message_to_send, parse_mode="HTML", disable_web_page_preview=True)

    def main(self) -> None:
        """Start the bot."""
        self.updater = Updater(TELEGRAM_TOKEN, use_context=True)

        # Get the dispatcher to register handlers
        dp = self.updater.dispatcher

        # Register handlers
        dp.add_handler(CommandHandler("paste", self.receive_paste))
        dp.add_handler(CommandHandler(
            "start", self.start, filters=Filters.chat_type.private))
        dp.add_handler(CommandHandler(
            "help", self.help_command, filters=Filters.chat_type.private))
        # TODO: add handler only to private messages
        dp.add_handler(MessageHandler(
            Filters.text & Filters.chat_type.private, self.receive_paste))

        # Starting the webhook.
        self.updater.start_webhook(listen=HOST, port=PORT,
                                   url_path=TELEGRAM_TOKEN)
        self.updater.bot.set_webhook(f"{WEBHOOK_URL}/{TELEGRAM_TOKEN}")
        logging.info(
            f"Server started on {HOST}:{PORT}. Listening publicily on {WEBHOOK_URL}/<token>")

        # Wait for a signal
        self.updater.idle()

    def check_delete_permission(self, chat_id) -> bool:
        return self.updater.bot.get_chat_member(chat_id, self.updater.bot.id).can_delete_messages

    @staticmethod
    def get_bot_username() -> str:
        """Return the bot username without '@'."""
        return "PastebinTGBot"
