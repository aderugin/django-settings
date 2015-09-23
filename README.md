## Установка

* `pip install git+git://github.com/aderugin/django-settings.git`


* Добавить контекстный процессор
`django_settings.context_processor`

* Создать модель для хранения настроек сайта

```
from django_settings import BaseSettingsModel

class SettingsModel(BaseSettingsModel):
    pass
```

* Зарегистрировать модель в админке
```
from django_settings import BaseSettingsAdmin

admin.site.register(<SettingsModel>, BaseSettingsAdmin)
```

* В настройках нужно определить класс модели
`DJANGO_SETTINGS_MODEL = 'settings.model.class.name'`