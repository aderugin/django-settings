# -*- coding: utf-8 -*-
from django import template
from .. import settings_model


register = template.Library()


@register.simple_tag
def get_option(option):
    return settings_model.get_option(option)