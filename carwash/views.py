import imp
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from carwash.models import Service
from core.mixins import ExtraContextMixin


def test(request):
    return HttpResponse(str(request.user))

class AboutView(generic.TemplateView):
    template_name = 'carwash/about.html'
    extra_context = {
        'header_selected_index': 2
    }

class PricesView(generic.TemplateView):
    template_name = 'carwash/prices.html'
    extra_context = {
        'services': Service.objects.all(), 
        'header_selected_index': 1
    }

class HomeView(generic.TemplateView, ExtraContextMixin):
    template_name = 'carwash/home.html'
    extra_context = {
        'header_selected_index': 0
    }

class ContactsView(generic.TemplateView):
    template_name = 'carwash/contacts.html'
    extra_context = {
        'header_selected_index': 3
    }


class OrderListView(generic.ListView):
    template_name = 'carwash/order_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return self.request.user.order_set.all()


class OrderDetailView(generic.DetailView):
    template_name = 'carwash/order_detail.html'
    context_object_name = 'order'

    def get_queryset(self):
        return self.request.user.order_set.all()


class OrderCreateView(generic.CreateView):
    template_name = 'carwash/order_create.html'
    success_url = reverse_lazy('order_list')
    from carwash.models import Order
    # form_class = 
    queryset = Order.objects.all()
    fields = '__all__'