<!-- PROJECT LOGO -->
<br />
<p align="center">
  <!--<a href="https://github.com/hellmrf/PastebinTGBot">
    <img src="logo.png" alt="Logo" width="80" height="80">
  </a>
  -->
  <h1 align="center">PastebinTGBot Bot</h1>

  <p align="center">
    Telegram interface to <a href="https://pastebin.com">Pastebin.com</a>: paste your code directly to a group and get a Pastebin link.
    <br />
    <a href="https://t.me/PastebinTGBot"><strong>Try it »</strong></a>
    <br />
    <br />
    <a href="https://github.com/hellmrf/PastebinTGBot/issues">Report Bug</a>
    ·
    <a href="https://github.com/hellmrf/PastebinTGBot/blob/master/README.pt-BR.md">Leia em Português</a>
  </p>
</p>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- TABLE OF CONTENTS -->

## Table of Contents

-   [About the Project](#about-the-project)
    -   [Built With](#built-with)
    -   [Author](#author)
-   [Basic Usage](#basic-usage)
    -   [Using in groups](#using-in-groups)
    -   [Special options](#special-options)
-   [Getting Started (for developers and curious)](#getting-started-for-developers-and-curious)
-   [Contributing](#contributing)
-   [Roadmap](#roadmap)
-   [License](#license)
-   [Contact](#contact)

<!-- ABOUT THE PROJECT -->

## About The Project

[Pastebin.com](https://pastebin.com) is online since 2002. Many people use it to share code and get help, also in Telegram groups. PastebinTGBot allows you to create pastebins directly in your groups or at least within Telegram.

### Built With

This project uses [Python](https://www.python.org/) as programming language and is free hosted on [Heroku](https://www.heroku.com/).
It also uses the following resources.

-   [Telegram Bot API](https://core.telegram.org/bots/api)
-   [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
-   [Pastebin API](https://pastebin.com/doc_api)

### Author

This project is developed and maintained by Heliton Martins. You can [contact me on Telegram](https://t.me/helitonmrf).

## Basic Usage

To use the bot, you can access it on Telegram ([@PastebinTGBot](https://t.me/PastebinTGBot)) and click `Start`. Then you can use the command `/help` to see the complete Usage or just send your text/code. To create a Pastebin containing "Hello World", send this to the bot:

```
Hello World
```

which is completely equivalent to

```
/paste Hello World
```

### Using in groups

To use the bot in a group, just add it to the group. Admin privilege is not required, but add functionality. When the bot is a normal member, it will reply to any message starting with `/paste` or `/paste@PastebinTGBot` and parse the content according to the rules (discussed below). However, if the bot has permission to delete messages, it'll send the link and delete the original message. It will avoid visual pollution in your group.

To create a Pastebin containing "Hello World" in a group, send this to the group:

```
/paste Hello World
```

which is completely equivalent to:

```
/paste@PastebinTGBot Hello World
```

### Special options

When creating a paste, you can adjust three options (so far): the syntax highlighting, the expiring time, and the visibility of the paste. These options are expected:

<div style="white-space: pre-wrap;">
╔═ <strong>Privacy</strong>:
╠┄ <code>public</code> (default)
╠┄ <code>unlisted</code>
║
╠═ <strong>Expiring time</strong>:
╠┄ <code>N</code>: Never (default)
╠┄ <code>10M</code>: 10 Minutes
╠┄ <code>1H</code>: 1 Hour
╠┄ <code>1D</code>: 1 Day
╠┄ <code>1W</code>: 1 Week
╠┄ <code>2W</code>: 2 Weeks
╠┄ <code>1M</code>: 1 Month
║
╠═ <strong>Syntax Highlighting</strong>:
╠┄ 253 languages are currently supported. <a href="https://pastebin.com/WT7YzUUV" target="_blank" rel="noopener noreferrer">Click here</a> to see the full list.
╚═
</div>

When these flags are found at the beginning of the message, they are
considered and removed. If there are two flags of the same category,
only the first is considered and the parsing stops.
For example, the string

```
javascript 10M Hello World
```

will be parsed as "Hello World", formatted as Javascript, and persisted
for 10 Minutes. On the other hand, the following string

```
javascript haskell Hello World
```

will be parsed as "haskell Hello World" and formatted as Javascript.

These flags _must_ be at the first line. If you need to begin your pastebin with the word _Julia_ (and don't want syntax highlighting), you should send this:

```
/paste

Julia is a relatively new, but very good language.
```

<!-- GETTING STARTED -->

## Getting Started (for developers and curious)

To get a local copy up and running follow these simple steps.

-   Clone the PastebinTGBot and enter the directory

```sh
$ git clone https://github.com/hellmrf/PastebinTGBot.git

$ cd PastebinTGBot
```

<small>**Beginners tip**: you'll see shell commands like this: `$ something`. In this case, type just `something` in your Terminal. `$` indicates "shell input".</small>

-   Make sure you have Python &geq; 3.7 and pip.

-   You can create a new [virtual environment](https://docs.python.org/3/tutorial/venv.html), but it's optional
<!--

```sh
$ python3 -m venv pastebintgbot

$ source pastebintgbot/bin/activate # Unix

$ pastebintgbot\Scripts\activate.bat # Windows
```

-->

-   Install dependencies

```sh
$ pip install -r requirements.txt
```

-   Create your Telegram Bot with [@BotFather](https://telegram.me/BotFather) and get your token.

-   Create an account on Pastebin.com to get you `api_dev_key` ([here](https://pastebin.com/doc_api#1)).

-   To test the bot, you'll need a public (and https protected) IP. This usually means a server, but for development, you can use [ngrok](https://ngrok.com/).

Download and install ngrok for your system and run the following command in a terminal:

```sh
$ ngrok http 127.0.0.1:8443
```

You'll see something like that:

```
Forwarding  https://d1bf0d3b0d39.ngrok.io -> http://127.0.0.1:8443
```

In this case, `https://d1bf0d3b0d39.ngrok.io` is your public URL (`WEBHOOK_URL` below). Let the terminal running.

-   Create a `.env` file in the folder `pastebintgbot` (the same folder as `main.py`) containing:

```ini
TELEGRAM_TOKEN=
PASTEBIN_TOKEN=
HOST=127.0.0.1
PORT=8443
WEBHOOK_URL=
```

You can change the IP and the port, but it must match the ngrok command.

_Windows users_: make sure the file has the _exact_ filename `.env`. You may need to configure Explorer to show extensions.

-   If everything is ok, run the bot.

```sh
$ python pastebintgbot/main.py
```

You should see something similar to this output (maybe more colorful) and you're good to go.

```
2021-01-01 00:00:00 you root[20513] INFO Server started on 127.0.0.1:8443. Listening publicily on https://d1bf0d3b0d39.ngrok.io/<token>
```

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin AmazingFeature`)
5. Open a Pull Request

I will analyze your PR as soon as possible.

---

<!-- ROADMAP -->

## Roadmap

See the [open issues](https://github.com/hellmrf/PastebinTGBot/issues) for a list of proposed features (and known bugs).

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->

## Contact

Heliton Martins - [@hellmrf](https://t.me/helitonmrf) - helitonmrf@gmail.com

Project Link: [https://github.com/hellmrf/PastebinTGBot](https://github.com/hellmrf/PastebinTGBot)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/hellmrf/PastebinTGBot.svg?style=flat-square
[contributors-url]: https://github.com/hellmrf/PastebinTGBot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/hellmrf/PastebinTGBot.svg?style=flat-square
[forks-url]: https://github.com/hellmrf/PastebinTGBot/network/members
[stars-shield]: https://img.shields.io/github/stars/hellmrf/PastebinTGBot.svg?style=flat-square
[stars-url]: https://github.com/hellmrf/PastebinTGBot/stargazers
[issues-shield]: https://img.shields.io/github/issues/hellmrf/PastebinTGBot.svg?style=flat-square
[issues-url]: https://github.com/hellmrf/PastebinTGBot/issues
[license-shield]: https://img.shields.io/github/license/hellmrf/PastebinTGBot.svg?style=flat-square
[license-url]: https://github.com/hellmrf/PastebinTGBot/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/hellmrf
