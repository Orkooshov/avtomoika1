from django.urls import path

from . import views as v

urlpatterns = [
    path('', v.CarwashView.as_view(), name='home'),
    path('contacts/', v.ContactsView.as_view(), name='contacts'),
    path('about/', v.AboutView.as_view(), name='about'),
    path('prices/', v.PricesView.as_view(), name='prices'),
    path('test', v.test)
]
