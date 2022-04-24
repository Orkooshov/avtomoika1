from django.shortcuts import render
from django.views.generic import TemplateView


def test(request):
    return render(request, 'carwash/about.html')

class AboutView(TemplateView):
    template_name = 'carwash/about.html'

class PricesView(TemplateView):
    template_name = 'carwash/prices.html'

class CarwashView(TemplateView):
    template_name = 'carwash/home.html'

class ContactsView(TemplateView):
    template_name = 'carwash/contacts.html'