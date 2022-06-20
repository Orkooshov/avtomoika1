from django import forms
from carwash import models as m
from django.contrib.auth import get_user_model


class OrderCreateForm(forms.ModelForm):
    client = forms.ModelChoiceField(queryset=get_user_model().objects.all(), widget=forms.HiddenInput())
    is_payed = forms.BooleanField(required=False, widget=forms.HiddenInput())
    status = forms.IntegerField(widget=forms.HiddenInput())
    # car = forms.ModelChoiceField(queryset=m.Car.objects.all())
    

    class Meta:
        model = m.Order
        fields = '__all__'