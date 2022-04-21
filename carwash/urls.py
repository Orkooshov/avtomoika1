from django.http import HttpResponse
from django.urls import path

from . import views as v

urlpatterns = [
    path('', lambda request: HttpResponse('hello')),
    path('test', v.test)
]
