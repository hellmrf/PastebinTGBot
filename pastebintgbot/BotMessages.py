import os
from PastebinAPI.pastebin_values import FIELD_VALUES


def _get_template_path(filename: str) -> str:
    return os.path.join(os.path.dirname(__file__), "bot_messages", filename)


def _help() -> str:
    with open(_get_template_path("help.txt"), 'r') as fl:
        return fl.read()


def _help_pt() -> str:
    with open(_get_template_path("help_pt.txt"), 'r') as fl:
        return fl.read()


TELEGRAM_MESSAGES = {
    "start": "Hey! What do you want to Paste? Just send your text or send /help to see the complete usage.",
    "help": _help(),
    "sent": "{} sent a Pastebin:\n\n📝 {}",
    "paste_empty": "Please, send in a single message the command /paste followed by the configuration (if any) and your text."
}
TELEGRAM_MESSAGES_PT = {
    "start": "Olá! O que você quer colar? Basta me enviar seu texto/código ou enviar /help para ver a utilização completa.",
    "help": _help_pt(),
    "sent": "{} enviou um Pastebin:\n\n📝 {}",
    "paste_empty": "Por favor, envie em uma única mensagem o comando /paste seguido das configurações (se houver) e do seu texto."
}
