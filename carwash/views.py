from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from carwash.models import Service
from core.mixins import ExtraContextMixin


def test(request):
    return HttpResponse(str(request.user))

class AboutView(TemplateView):
    template_name = 'carwash/about.html'
    extra_context = {
        'header_selected_index': 2
    }

class PricesView(TemplateView):
    template_name = 'carwash/prices.html'
    extra_context = {
        'services': Service.objects.all(), 
        'header_selected_index': 1
    }

class HomeView(TemplateView, ExtraContextMixin):
    template_name = 'carwash/home.html'
    extra_context = {
        'header_selected_index': 0
    }

class ContactsView(TemplateView):
    template_name = 'carwash/contacts.html'
    extra_context = {
        'header_selected_index': 3
    }