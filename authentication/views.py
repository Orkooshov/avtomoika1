from django.views.generic import FormView, UpdateView, DetailView
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse_lazy

from authentication.forms import (LoginForm, RegisterForm, UserEditForm, 
    CustomPasswordChangeForm, ClientProfileEditForm)


User = get_user_model()


class LoginView(FormView):
    template_name = 'authentication/login.html'
    form_class = LoginForm
    success_url = settings.LOGIN_REDIRECT_URL

    def form_valid(self, form):
        user = authenticate(self.request, **form.cleaned_data)
        login(self.request, user)
        return super().form_valid(form)


class RegisterView(FormView):
    template_name = 'authentication/register.html'
    form_class = RegisterForm
    success_url = settings.LOGIN_REDIRECT_URL

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


def logout_view(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)


class UserEditView(UpdateView):
    template_name = 'authentication/user_edit.html'
    form_class = UserEditForm
    success_url = reverse_lazy('user_edit')
    
    def get_object(self):
        return self.request.user
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class UserDetailView(DetailView):
    template_name = 'authentication/user_detail.html'
    model = User

    def get_object(self):
        return self.request.user


class PasswordChangeView(UpdateView):
    form_class = CustomPasswordChangeForm
    template_name = 'authentication/password.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
