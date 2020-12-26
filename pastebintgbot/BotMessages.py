import os


def get_message(key: str, lang: str = "en_US"):
    if lang is not None and lang.startswith("pt"):
        return TELEGRAM_MESSAGES_PT[key]
    else:
        return TELEGRAM_MESSAGES[key]


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
    "paste_empty": "Please, send in a single message the command /paste followed by the configuration (if any) and your text. (Or send /help to see the complete usage.)",
    "author": "Open-source and developed by <a href='https://github.com/hellmrf'>Heliton Martins</a> (@helitonmrf).\n\n<a href='https://github.com/hellmrf/PastebinTGBot'>Source code</a>"
}
TELEGRAM_MESSAGES_PT = {
    "start": "Olá! O que você quer colar? Basta me enviar seu texto/código ou enviar /help para ver a utilização completa.",
    "help": _help_pt(),
    "sent": "{} enviou um Pastebin:\n\n📝 {}",
    "paste_empty": "Por favor, envie em uma única mensagem o comando /paste seguido das configurações (se houver) e do seu texto. (Ou envie /help para ver as opções disponíveis).",
    "author": "Código aberto e desenvolvido por <a href='https://github.com/hellmrf'>Heliton Martins</a> (@helitonmrf).\n\n<a href='https://github.com/hellmrf/PastebinTGBot'>Código Fonte</a>"
}
