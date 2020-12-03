import os
from dotenv import load_dotenv
load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
PASTEBIN_TOKEN = os.getenv("PASTEBIN_TOKEN")


WEBHOOK_URL = os.getenv("WEBHOOK_URL")

HOST = os.environ.get("HOST", "0.0.0.0")
PORT = int(os.environ.get("PORT", 8443))


def debug_mode() -> bool: return HOST == "127.0.0.1"
