from django.db import models
from django.contrib.auth import get_user_model

from cars.models import Car, CarClass
from core.models import AbstractTimestampedModel


User = get_user_model()


class Service(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Price(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    car_class = models.ForeignKey(CarClass, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.service} {self.car_class} {self.price}'

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'


class Order(AbstractTimestampedModel):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ManyToManyField(Service)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.client} {self.car}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
