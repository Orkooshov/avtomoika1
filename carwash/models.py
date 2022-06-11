from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

from cars.models import Car, CarClass
from core.models import AbstractTimestampedModel


User = get_user_model()


class Service(models.Model):
    name = models.CharField(verbose_name='Название', max_length=64)
    description = models.TextField(
        verbose_name='Описание', default='', blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Price(models.Model):
    service = models.ForeignKey(
        verbose_name='Услуга', to=Service, on_delete=models.CASCADE)
    car_class = models.ForeignKey(
        verbose_name='Класс', to=CarClass, on_delete=models.CASCADE)
    price = models.DecimalField(
        verbose_name='Цена', max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.service} {self.car_class} {self.price}'

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'


class OrderStatus(models.IntegerChoices):
    NOT_DONE = 0, 'Не выполнено'
    DONE = 1, 'Выполнено'
    CANCELED = 2, 'Отменено'


class Order(AbstractTimestampedModel):
    client = models.ForeignKey(
        verbose_name='Клиент', to=User, on_delete=models.CASCADE)
    price = models.ForeignKey(
        verbose_name='Цена', to=Price, on_delete=models.CASCADE)
    car = models.ForeignKey(verbose_name='Авто', to=Car,
                            on_delete=models.CASCADE)
    is_payed = models.BooleanField(verbose_name='Оплачен', default=False)
    status = models.IntegerField(verbose_name='Состояние', choices=OrderStatus.choices, default=0)

    def get_absolute_url(self):
        return reverse('order_detail', kwargs={'pk': self.pk})

    def get_sum(self):
        return '1234'

    def __str__(self) -> str:
        return f'{self.client} {self.car}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
