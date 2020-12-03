from PastebinAPI import PasteBin
from PastebinAPI.pastebin_values import FIELD_VALUES
from settings import PASTEBIN_TOKEN, debug_mode
import re
import logging
from datetime import datetime


class PastebinUploader:

    def __init__(self) -> None:
        self.option = {"format": None, "private": None, "expire": None}
        self.pastebin = PasteBin(PASTEBIN_TOKEN)

    def paste(self, message: str) -> str:
        """Sanitize, upload and return the URL for a new pastebin.

        Args:
            message (str): The code to be pasted.

        Raises:
            ValueError: When the message (without command and configs) is too short.

        Returns:
            str: The URL of the new pastebin.
        """
        msg = self.remove_bot_call(message)
        msg = self.check_for_config(msg)
        if len(msg) < 16:
            raise ValueError("Actual message must have at least 16 characters")
        if debug_mode():
            self._DEBUG_log_incoming_message(message)
            # return "Test mode." # For DEBUG.
        url = self.pastebin.paste(msg, **self.option)
        return url

    def check_for_config(self, message: str) -> str:
        """Verify if the message sent start with configuration flags.
        These flags are any valid key in `FIELD_VALUES["format_values"]`
        and FIELD_VALUES["expire_values"], as well as "public" and "private".
        When these flags are found in the beginning of the message, they are
        considered and removed. If there are two flags of the same category,
        only the first is considered and the parsing stops.
        For example, the following string

        ```
        javascript 10M Hello World
        ```

        will be parsed as "Hello World", formated as Javascript and persisted
        for 10 Minutes. On the other hand, the following string

        ```
        javascript haskell Hello World
        ```

        will be parsed as "haskell Hello World" and formatted as Javascript.

        Args:
            message (str): The message without bot command. (See `PastebinUploader.remove_bot_call`)

        Returns:
            str: The message without config flags.
        """
        msg = message.split("\n")[0]
        initial_chunk = list(filter(None, msg.split(" ")))[:3]
        last_config_found = None
        for part in initial_chunk:
            part_lc = part.lower()
            if part_lc in FIELD_VALUES["format_values"].keys() and self.option["format"] is None:
                self.option["format"] = part
                last_config_found = part
                continue
            elif part in FIELD_VALUES["expire_values"].keys() and self.option["expire"] is None:
                self.option["expire"] = part
                last_config_found = part
                continue
            elif part_lc in ["public", "unlisted"]:
                self.option["private"] = 1 if part_lc == "unlisted" else None
                last_config_found = part
                continue
            else:
                break
        if not last_config_found:
            return message
        return message[msg.index(last_config_found, 0, 100)+len(last_config_found):].strip()

    def remove_bot_call(self, message: str) -> str:
        """Remove the bot call from the beggining of the string.
        For instance, if the string starts with /<command>@botname,
        that part will be removed.

        Args:
            message (str): The string.

        Returns:
            str: The string without bot call.
        """
        return re.sub(r'^[/][A-Za-z0-9@_-]+\s*', '', message)

    def _DEBUG_log_incoming_message(self, msg: str) -> None:
        """Log msg to a file in the filesystem. ONLY FOR DEBUG.

        Args:
            msg (str): The message to be logged.
        """
        with open("incoming_message.log", 'a') as fl:
            fl.writelines(
                f"\n\n================"+datetime.now().isoformat()
                + "================\n\n")
            fl.write(msg)
