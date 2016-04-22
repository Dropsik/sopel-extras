# coding=utf-8
# Copyright 2010, Michael Yanovich (yanovich.net), and Morgan Goose
# Copyright 2012, Lior Ramati
# Copyright 2013, Elsie Powell (embolalia.com)
# Licensed under the Eiffel Forum License 2.
from __future__ import unicode_literals, absolute_import, print_function, division

import json
import random
import re
import requests
from sopel import web
from sopel.module import commands, rule



@rule('(?i)$nickname\:\s+(poka|zapodaj).*(cyc|piersi).*')
def cycory(bot, trigger):
    url = 'http://api.oboobs.ru/noise/1'
    data = requests.get(url).json()
    cyce = ('http://media.oboobs.ru/noise/' + str(data[0]['id']) + '.jpg')
    bot.say(cyce)
