# -*- coding: utf-8 -*-

# Use this token to access the HTTP API:
# 429189469:AAFopYIIb5jSSKy3hHVhsbxTN_tv5KhPZXA
#
# stalker_creep_bot
from __builtin__ import str

from olx import *
from telegram.ext import Updater
from telegram.ext import CommandHandler

from olx import OlxAdd

updater = Updater(token='429189469:AAFopYIIb5jSSKy3hHVhsbxTN_tv5KhPZXA')
dispatcher = updater.dispatcher


def stalk(bot, update):
    scrapper = OlxScrapper()
    scrapper.set_query('москвич')
    adds = scrapper.scrap

    for add in adds:
        message = add.date + '\r\n'\
                  + add.text + '\r\n'\
                  + add.location + '\r\n'
        bot.send_message(chat_id=update.message.chat_id, text=message)
        bot.send_photo(chat_id=update.message.chat_id, photo=add.image_url)


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


start_handler = CommandHandler('start', start)
stalk_handler = CommandHandler('stalk', stalk)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(stalk_handler)

updater.start_polling()