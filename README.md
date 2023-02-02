# Cyrillic to Latin Converter Telegram Bot

This is a Telegram bot that can convert Cyrillic text to Latin text.

## Prerequisites

Before you begin, make sure you have the following tools installed on your system:

    * Python 3.7 or later
    * pip (Python package manager)


## Installation

1.Clone the repository to your local machine using the following command:


shell:
`$ git clone https://github.com/<user>/KazakhLatinConverterTelegramBot.git` 

2.Change into the project directory:

shell:
`$ cd KazakhLatinConverterTelegramBot`

3.Create a virtual environment and activate it:

shell:
`$ python3 -m venv venv`
`$ source venv/bin/activate`

4.Install the required packages:

`$ pip install -r requirements.txt`

5.Create a Telegram bot and obtain the API key.

6. Store the API key in an environment variable named TELEGRAM_BOT_API_KEY.

7. Run the bot:

ruby

`$ python bot.py`

## Usage

8.Start a conversation with your bot in Telegram.
9.Send it a message in Cyrillic.
10.The bot will reply with the converted Latin text.

## Conclusion

That's it! Your Kazakh Latin Converter Telegram Bot is now ready to use. Enjoy!





> This code uses the pyTelegramBotApi library to handle the communication with Telegram's API.

The `@bot.message_handler(commands=['start'])` decorator is used to handle the `/start` command which is used to start the bot and the `@bot.message_handler(content_types=['text'])` decorator is used to handle the text messages received by the bot and convert

