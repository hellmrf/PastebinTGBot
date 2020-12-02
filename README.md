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
-   [Getting Started](#getting-started)
    -   [Prerequisites](#prerequisites)
    -   [Installation](#installation)
-   [Usage](#usage)
-   [Roadmap](#roadmap)
-   [Contributing](#contributing)
-   [License](#license)
-   [Contact](#contact)

<!-- ABOUT THE PROJECT -->

## About The Project

[Pastebin.com](https://pastebin.com) is online since 2002. Many people use it to share code and get help, also in Telegram groups. PastebinTGBot allow you to create pastebins directly in your groups or at least within Telegram.

### Built With

This project uses [Python](https://www.python.org/) as programming language and are free hosted on [Heroku](https://www.heroku.com/).
It also uses the following resources.

-   [Telegram Bot API](https://core.telegram.org/bots/api)
-   [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
-   [Pastebin API](https://pastebin.com/doc_api)

---

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

-   Make sure you have Python &geq; 3.7 and pip.

-   You can create a new [virtual environment](https://docs.python.org/3/tutorial/venv.html), but it's optional

```sh
$ python3 -m venv pastebintgbot

$ source tutorial-env/bin/activate # Unix

$ tutorial-env\Scripts\activate.bat # Windows
```

<small>**Beginners tip**: you'll see shell commands like this: `(pastebintgbot) $ something`. In this case, type just `something` in your Terminal. `(pastebintgbot)` indicates the active virtual environment and `$` indicates "input".</small>

-   Install dependencies

```sh
(pastebintgbot) $ pip install -r requirements.txt
```

-   Create your Telegram Bot with [@BotFather](https://telegram.me/BotFather) and get your token.

-   Create an account on Pastebin.com to get you `api_dev_key`.

-   Create a `.env` file in the root of the project containing:

```env
TELEGRAM_TOKEN=
PASTEBIN_TOKEN=
HOST=0.0.0.0
WEBHOOK_URL=
```

The last two are optional.

### Installation

Clone the PastebinTGBot and enter the directory

```sh
(pastebintgbot) $ git clone https://github.com/hellmrf/PastebinTGBot.git

(pastebintgbot) $ cd PastebinTGBot
```

---

<!-- USAGE EXAMPLES -->

## Usage

Just run:

```sh
(pastebintgbot) $ python pastebintgbot/main.py
```

<!-- ROADMAP -->

## Roadmap

See the [open issues](https://github.com/hellmrf/PastebinTGBot/issues) for a list of proposed features (and known bugs).

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->

## Contact

Heliton Martins - [@hellmrf](https://twitter.com/hellmrf) - helitonmrf@gmail.com

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
