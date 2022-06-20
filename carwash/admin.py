from django.contrib import admin

from carwash import models as m


@admin.register(m.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


@admin.register(m.Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('service', 'car_class', 'price')
    list_filter = ('service', 'car_class')


@admin.register(m.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'car', 'is_payed', 'status', 'created_at', 'updated_at')
    list_filter = ('price', 'status', 'created_at', 'updated_at')
    search_fields = ('client', 'car')


@admin.register(m.CallApplication)
class CallApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number')
    search_fields = ('name', 'email', 'phone_number')