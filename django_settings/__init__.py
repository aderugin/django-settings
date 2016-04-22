# -*- coding: utf-8 -*-
from django.utils.functional import SimpleLazyObject
from django_settings.utils import get_class
from django_settings.config import MODEL
from .base import context_processor, BaseSettingsModel, BaseSettingsAdmin

settings_model = SimpleLazyObject(lambda: get_class(MODEL))
