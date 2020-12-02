from PastebinAPI import PasteBin
from PastebinAPI.pastebin_values import FIELD_VALUES
from settings import PASTEBIN_TOKEN
import re
import logging


class PastebinUploader:

    def __init__(self) -> None:
        self.option = {"format": None, "private": None, "expire": None}
        self.pastebin = PasteBin(PASTEBIN_TOKEN)

    def paste(self, message: str) -> str:
        msg = self.remove_bot_call(message)
        msg = self.check_for_config(msg)
        if len(msg) < 5:
            return ""
        url = self.pastebin.paste(msg, **self.option)
        return url

    def check_for_config(self, message: str) -> str:
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
        return message[msg.index(last_config_found, 0, 100)+len(last_config_found):]

    def remove_bot_call(self, message: str) -> str:
        """Remove the bot call from the beggining of the string.
        For example, if the string starts with /<command>@botname,
        it will be removed.

        Args:
            message (str): The string.

        Returns:
            str: The string without bot call.
        """
        return re.sub(r'^[/][A-Za-z0-9@_-]+\s*', '', message)
