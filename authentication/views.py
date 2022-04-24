from django.views.generic import TemplateView
from django.contrib.auth import login, logout, authenticate
from django.conf import settings
from django.shortcuts import redirect

from core.mixins import ExtraContextMixin
from authentication.forms import LoginForm


class LoginView(TemplateView, ExtraContextMixin):
    template_name = 'authentication/login.html'
    form = LoginForm()
    extra_context = {
        'form': form
    }

    def post(self, request, *args, **kwargs):
        self.form = LoginForm(request, data=request.POST)
        if self.form.is_valid():
            user = authenticate(request, **self.form.cleaned_data)
            login(request, user)
        if request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
        return self.get(request, *args, **kwargs)


class RegisterView(TemplateView):
    template_name = 'authentication/register.html'


def logout_view(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)
