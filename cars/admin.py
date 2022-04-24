from django.contrib import admin
from cars import models as m


@admin.register(m.CarBodywork, m.CarBrand, m.CarCoverage,
                m.CarModel, m.CarSalon, m.CarClass)
class DefaultAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


@admin.register(m.Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'car_class', 'bodywork', 'salon', 'coverage', 'owner', 'state_number')
    list_filter = ('brand', 'model', 'car_class', 'bodywork', 'salon', 'coverage', 'owner')
    search_fields = ('state_number', )