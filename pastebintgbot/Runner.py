"""To be called when an user send a paste.
This has the responsability of send to PastebinUploader
and answer the user with the url.
Maybe Runner isn't the best name, but I can't create a better now.
"""
import logging
from telegram import Update
from telegram.bot import Bot
from BotMessages import get_message
from PastebinUploader import PastebinUploader


class Runner:

    msg_options = {"parse_mode": "HTML", "disable_web_page_preview": True}

    def __init__(self, bot: Bot):
        """Receive the paste code and answer the user with URL.

        Args:
            bot (Bot): The Bot object running.
        """
        self.bot = bot

    def just_answer(self, update: Update, key: str) -> None:
        """Just answer the `update.message` with the message `BotMessages.get_message(key)`.

        Args:
            update (Update): The update object.
            key (str): The key of the message. Just passed to `BotMessages.get_message(key)`.
        """
        update.message.reply_text(
            get_message(key, update.message.from_user.language_code), **self.msg_options)

    def process_paste(self, update: Update) -> None:
        """Actually process a paste sent, including the Upload (delegated to PastebinUploader) and the answer to user.

        Args:
            update (Update): The update that generated this request.
        """
        message = update.message.text
        username = "@" + update.message.from_user.username
        language = update.message.from_user.language_code
        message_id = update.message.message_id
        chat_id = update.message.chat.id

        logging.info(
            f"Received msg_id {message_id} from {username} in {chat_id}")

        try:
            url = PastebinUploader().paste(message)
            msg = get_message('sent', language).format(username, url)
            if self.have_delete_permission(chat_id):
                self.bot.send_message(chat_id, msg, **self.msg_options)
                self.bot.delete_message(chat_id, message_id)
            else:
                update.message.reply_text(msg, **self.msg_options)
        except ValueError:
            msg = get_message('paste_empty', language)
            update.message.reply_text(msg, **self.msg_options)
            return

    def have_delete_permission(self, chat_id) -> bool:
        """Check if I have the privilege to delete messages from users (in groups).

        Args:
            chat_id (str|int): The chat_id

        Returns:
            bool: If the bot has delete permission.
        """
        return self.bot.get_chat_member(chat_id, self.bot.id).can_delete_messages
