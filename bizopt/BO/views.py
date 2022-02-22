from django.shortcuts import render
from .utils import *
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


def get_base_context():
    context = {
        'menu': [
            {'link': '/', 'text': 'Главная'},
            {'link': '/profile_in/', 'text': 'Профиль'},
        ],
        'main_header': 'BizOpt',
    }
    return context


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


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')

def profile (request, name):
    context = get_base_context()
    try:
        pers_data = User.objects.get(username=name)
        pers_data.save()
    except User.DoesNotExist:
        pers_data = {
            'username': name,
            'name': '',
            'surname': '',
            'city': '',
        }
        item = User(
            username = '',
            surname = '',
            name = '',
            city = '',
        )
        item.save()
    context['user'] = pers_data
    return render(request, 'profile.html', context)


def login_page(request):
    content = {}
    return render(request, 'login.html', content)
# Create your views here.
