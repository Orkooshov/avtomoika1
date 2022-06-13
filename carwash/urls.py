from django.http import HttpResponse
from django.urls import path

from . import views as v

urlpatterns = [
    path('', v.HomeView.as_view(), name='home'),
    path('contacts/', v.ContactsView.as_view(), name='contacts'),
    path('about/', v.AboutView.as_view(), name='about'),
    path('prices/', v.PricesView.as_view(), name='prices'),
    # path('personal-account/', lambda x: HttpResponse('личный кабинет'), name='personal_account'),
    path('orders/', v.OrderListView.as_view(), name='order_list'),
    path('orders/create/', v.OrderCreateView.as_view(), name='order_create'),
    path('orders/<int:pk>/', v.OrderDetailView.as_view(), name='order_detail'),
    path('test', v.test)
]
