from django.shortcuts import render
from django.conf import settings
from django_telegrambot.apps import DjangoTelegramBot


def index(request):

    bot_list = DjangoTelegramBot.bots

    context = {'bot_list': bot_list,
               'update_mode': settings.DJANGO_TELEGRAMBOT['MODE'],
               'token': settings.TOKEN,
               'chat_id': settings.CHAT_ID,
               'method': 'sendMessage',

               }

    return render(request, 'bot/index.html', context)







