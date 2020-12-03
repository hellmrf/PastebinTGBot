<!-- PROJECT LOGO -->
<br />
<p align="center">
  <!--<a href="https://github.com/hellmrf/PastebinTGBot">
    <img src="logo.png" alt="Logo" width="80" height="80">
  </a>
  -->
  <h1 align="center">PastebinTGBot Bot</h1>

  <p align="center">
    Interface no Telegram para o <a href="https://pastebin.com">Pastebin.com</a>: crie pastebins diretamente de um grupo de receba um link do Pastebin.
    <br />
    <a href="https://t.me/PastebinTGBot"><strong>Testar »</strong></a>
    <br />
    <br />
    <a href="https://github.com/hellmrf/PastebinTGBot/issues">Informar bug</a>
    ·
    <a href="https://github.com/hellmrf/PastebinTGBot/blob/master/README.md">Read in English</a>
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

-   [Sobre o Projeto](#sobre-o-projeto)
    -   [Feito com](#feito-com)
    -   [Autor](#autor)
-   [Uso comum](#uso-comum)
    -   [Uso em grupos](#uso-em-grupos)
    -   [Opções especiais](#opções-especiais)
-   [Rodando localmente (para desenvolvedores e curiosos)](#rodando-localmente-para-desenvolvedores-e-curiosos)
-   [Contribuindo](#contribuindo)
-   [Próximos Passos](#próximos-Passos)
-   [Licença](#licença)
-   [Contato](#contato)

<!-- Sobre o Projeto -->

## Sobre o Projeto

O [Pastebin.com](https://pastebin.com) está online desde 2002. Muitas pessoas o utilizam para compartilhar código e obter ajuda, inclusive em grupos do Telegram. O PastebinTGBot te permite criar pastebins diretamente nos seus grupos ou de um chat privado.

### Feito com

Este projeto usa [Python](https://www.python.org/) como linguagem de programação e está hospedado gratuitamente no [Heroku](https://www.heroku.com/).
Os recursos a seguir também foram utilizados:

-   [Telegram Bot API](https://core.telegram.org/bots/api)
-   [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
-   [Pastebin API](https://pastebin.com/doc_api)

### Autor

Este projeto é desenvolvido e mantido por Heliton Martins. Você pode [me contatar no Telegram](https://t.me/helitonmrf).

## Uso Comum

Para usar o bot, você pode acessá-lo no Telegram ([@PastebinTGBot](https://t.me/PastebinTGBot)) e clicar em `Começar`. Então você pode enviar o comando `/help` para ver a utilização completa ou simplismente enviar seu texto/código. Para criar um Pastebin contendo "Olá Mundo", envie para o bot:

```
Olá Mundo
```

que é completamente equivalente a

```
/paste Olá Mundo
```

### Uso em grupos

Para usar o bot num grupo simplesmente adicione-o ao grupo. Privilégios administrativos não são requeridos, mas adicionam funcionalidades. Se o bot for um membro normal, responderá qualquer mensagem começando com `/paste` ou `/paste@PastebinTGBot` e analisar o conteúdo de acordo com as regras (discutidas abaixo). Entretanto, se o bot tiver permissões para deletar mensagens, o link será enviado e a mensagem original apagada. Isso evitará poluição visual nos seus grupos.

Para criar um Pastebin contendo "Olá Mundo" em um grupo, envie:

```
/paste Olá Mundo
```

que é completamente equivalente a

```
/paste@PastebinTGBot Olá Mundo
```

### Opções especiais

Ao criar um pastebin, você pode ajustar três opções (até agora): a _syntax highlighting_, o tempo de expiração e a visibilidade. Essas opções podem ser:

<div style="white-space: pre-wrap;">
╔═ <strong>Privacidade</strong>:
╠┄ <code>public</code> (padrão)
╠┄ <code>unlisted</code>
║
╠═ <strong>Tempo de expiração</strong>:
╠┄ <code>N</code>: Never (padrão)
╠┄ <code>10M</code>: 10 Minutos
╠┄ <code>1H</code>: 1 Horas
╠┄ <code>1D</code>: 1 Dia
╠┄ <code>1W</code>: 1 Semana (Week)
╠┄ <code>2W</code>: 2 Semanas
╠┄ <code>1M</code>: 1 Mês
║
╠═ <strong>Syntax Highlighting</strong>:
╠┄ 253 são suportadas no momento. <a href="https://pastebin.com/WT7YzUUV" target="_blank" rel="noopener noreferrer">Clique aqui</a> para ver a lista completa.
╚═
</div>

Quando essas flags forem encontradas no começo da mensagem, elas serão consideradas e removidas. Se existem duas flags da mesma categoria, apenas a primeira será considerada e o restante ignorado (mesmo que outras flags válidas apareçam na sequência).

Por exemplo, a mensagem

```
javascript 10M Olá Mundo
```

será interpretada como "Olá Mundo", formatada como Javascript, e mantida por 10 minutos. Por outro lado, a mensagem

```
javascript haskell Olá Mundo
```

será interpretada como "haskell Olá Mundo" e formatada como Javascript.

As flags _precisam_ estar na primeira linha. Se você precisa começar seu pastebin com a palavra _Julia_, por exemplo, deve enviar:

```
/paste

Julia é uma linguagem nova, mas muito promissora.
```

Já que `/paste Julia é uma` seria interpretado como `é uma` e formatado como Julia.

<!-- GETTING STARTED -->

## Rodando localmente (para desenvolvedores e curiosos)

<sup><sub>Você pode me ajudar a traduzir esta seção??</sub></sup>

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

## Contribuindo

Contribuições são o que tornam a comunidade open source um lugar tão maravilhoso para aprender, inspirar e criar. Qualquer contribuição que você fizer será muitíssimo apreciada.

1. _Fork_ o projeto
2. Crie sua _branch_ (`git checkout -b AmazingFeature`)
3. _Commit_ as alterações (`git commit -m 'Add some AmazingFeature'`)
4. "Empurre" (_push_) para a _branch_ (`git push origin AmazingFeature`)
5. Abra um _Pull Request_

Eu vou analisar seu PR o mais rápido possível.

---

<!-- ROADMAP -->

## Próximos Passos

Veja as [issues](https://github.com/hellmrf/PastebinTGBot/issues) para uma lista se recursos propostos e bugs conhecidos.

<!-- LICENSE -->

## Licença

Distribuido sob licença MIT. Veja [`LICENSE`](https://github.com/hellmrf/PastebinTGBot/blob/main/LICENSE) para maiores informações.

<!-- CONTACT -->

## Contato

Heliton Martins - [@hellmrf](https://t.me/helitonmrf) - helitonmrf@gmail.com

Link do Projeto: [https://github.com/hellmrf/PastebinTGBot](https://github.com/hellmrf/PastebinTGBot)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/hellmrf/PastebinTGBot.svg?style=for-the-badge
[contributors-url]: https://github.com/hellmrf/PastebinTGBot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/hellmrf/PastebinTGBot.svg?style=for-the-badge
[forks-url]: https://github.com/hellmrf/PastebinTGBot/network/members
[stars-shield]: https://img.shields.io/github/stars/hellmrf/PastebinTGBot.svg?style=for-the-badge
[stars-url]: https://github.com/hellmrf/PastebinTGBot/stargazers
[issues-shield]: https://img.shields.io/github/issues/hellmrf/PastebinTGBot.svg?style=for-the-badge
[issues-url]: https://github.com/hellmrf/PastebinTGBot/issues
[license-shield]: https://img.shields.io/github/license/hellmrf/PastebinTGBot?style=for-the-badge
[license-url]: https://github.com/hellmrf/PastebinTGBot/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/hellmrf
