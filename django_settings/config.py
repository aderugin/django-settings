# -*- coding: utf-8 -*-
from django.conf import settings


SETTINGS_TITLE = getattr(settings, 'DJANGO_SETTINGS_TITLE', u'Настройки сайта')

MODEL = getattr(settings, 'DJANGO_SETTINGS_MODEL', None)
if not MODEL:
    raise Exception("You need to define DJANGO_SETTINGS_MODEL variable in your settings file")
