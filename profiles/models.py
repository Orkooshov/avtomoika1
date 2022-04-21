from tabnanny import verbose
from django.db import models

from core.models import AbstractTimestampedModel


class AbstractProfile(AbstractTimestampedModel):
    user = models.OneToOneField(
        'authentication.User', on_delete=models.CASCADE
    )
    photo = models.ImageField(
        'Фото', blank=True, upload_to='avatars/')

    class Meta:
        abstract = True


class Client(AbstractProfile):
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Staff(AbstractProfile):
    class Meta:
        verbose_name = 'Рабочий'
        verbose_name_plural = 'Рабочие'
