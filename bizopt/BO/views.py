from django.shortcuts import render
from .utils import *
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

def index_page(request):
    content = {}
    return render(request, 'index.html', content)


def signin_page(request):
    content = {}
    return render(request, 'signin.html', content)


class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'signin.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))


def login_page(request):
    content = {}
    return render(request, 'login.html', content)
# Create your views here.
