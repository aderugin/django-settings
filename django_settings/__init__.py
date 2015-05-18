# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils.functional import SimpleLazyObject
from .utils import get_class


MODEL = getattr(settings, 'DJANGO_SETTINGS_MODEL', None)

if not MODEL:
	raise Exception('You need to define DJANGO_SETTINGS_MODEL variable in your settings file')


settings_model = SimpleLazyObject(lambda: get_class(MODEL))


from .base import *