from tabnanny import verbose
from django.db import models

from core.models import AbstractTimestampedModel


class CarBrand(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'


class CarModel(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'


class CarBodywork(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Кузов'
        verbose_name_plural = 'Кузовы'


class CarSalon(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Салон'
        verbose_name_plural = 'Салоны'


class CarCoverage(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Покрытие'
        verbose_name_plural = 'Покрытия'


class Car(AbstractTimestampedModel):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    bodywork = models.ForeignKey(CarBodywork, on_delete=models.CASCADE)
    salon = models.ForeignKey(CarSalon, on_delete=models.CASCADE)
    coverage = models.ForeignKey(CarCoverage, on_delete=models.CASCADE)
    owner = models.ForeignKey('profiles.Client', on_delete=models.CASCADE)
    state_number = models.CharField(max_length=20, verbose_name='Госномер')

    def __str__(self) -> str:
        return self.state_number

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
