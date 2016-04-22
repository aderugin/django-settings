# -*- coding: utf-8 -*-
from django.contrib import admin
from django.db import models
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible
from django_settings.config import SETTINGS_TITLE


def context_processor(request):
    from django_settings import settings_model
    return {'settings': settings_model.get_instance()}


@python_2_unicode_compatible
class BaseSettingsModel(models.Model):
    class Meta:
        verbose_name = SETTINGS_TITLE
        verbose_name_plural = SETTINGS_TITLE
        abstract = True

    @classmethod
    def get_option(cls, name):
        return getattr(cls.get_instance(), name, '')

    @classmethod
    def get_instance(cls):
        instance, _ = cls.objects.get_or_create()
        return instance

    def __str__(self):
        return SETTINGS_TITLE


class BaseSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects > 0:
            return False
        else:
            return True

    def changelist_view(self, request, extra_context=None):
        info = '{0}_{1}'.format(self.model._meta.app_label, self.model._meta.model_name)
        try:
            instance = self.model.objects.get()
        except self.model.DoesNotExist:
            return redirect(reverse('admin:{0}_add'.format(info)))
        else:
            return redirect(reverse('admin:{0}_change'.format(info), args=[instance.pk]))
