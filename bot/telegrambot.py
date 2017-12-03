from telegram.ext import CommandHandler, MessageHandler, Filters
from django_telegrambot.apps import DjangoTelegramBot

import logging
logger = logging.getLogger(__name__)


def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hi!')


def startgroup(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hi!')


def me(bot, update):
    bot.sendMessage(update.message.chat_id, text='Your information:\n{}'.format(update.effective_user))


def chat(bot, update):
    bot.sendMessage(update.message.chat_id, text='This chat information:\n {}'.format(update.effective_chat))


def forwarded(bot, update):
    bot.sendMessage(update.message.chat_id, text='This msg forwaded information:\n {}'.format(update.effective_message))


def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='Help!')


def echo(bot, update):
    update.message.reply_text(update.message.text)


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    logger.info("Loading handlers for telegram bot")

    dp = DjangoTelegramBot.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(CommandHandler("startgroup", startgroup))
    dp.add_handler(CommandHandler("me", me))
    dp.add_handler(CommandHandler("chat", chat))
    dp.add_handler(MessageHandler(Filters.forwarded , forwarded))

    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)
