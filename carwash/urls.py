from django.http import HttpResponse
from django.urls import path

from . import views as v

urlpatterns = [
    path('', v.HomeView.as_view(), name='home'),
    path('contacts/', v.ContactsView.as_view(), name='contacts'),
    path('about/', v.AboutView.as_view(), name='about'),
    path('prices/', v.PricesView.as_view(), name='prices'),
    path('personal-account/', lambda x: HttpResponse('личный кабинет'), name='personal_account'),
    path('orders/', lambda x: HttpResponse('orders'), name='orders'),
    path('test', v.test)
]
