from django.shortcuts import render
from .utils import *
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


def gen_menu():
    return [
        {'link': '/', 'text': 'Главная'},
        {'link': '/creators/', 'text': 'Создатели'},
        {'link': '/employers/', 'text': 'Предприниматели'},
        {'link': '/tasks/', 'text': 'Задачи'},
    ]

#
# def get_base_context():
#     context = {
#         'menu': [
#             {'link': '/', 'text': 'Главная'},
#             {'link': '/creators/', 'text': 'Создатели'},
#             {'link': '/employers/', 'text': 'Предприниматели'},
#             {'link': '/tasks/', 'text': 'Задачи'},
#         ],
#         'main_header': 'BizOpt',
#     }
#     return context


def creators_page(request):
    content = {
        'menu':gen_menu()
    }
    return render(request, 'creators.html', content)


def tasks_page(request):
    content = {
        'menu': gen_menu()
    }
    return render(request, 'tasks.html', content)


def employers_page(request):
    content = {
        'menu': gen_menu()
    }
    return render(request, 'employers.html', content)


def index_page(request):
    content = {
        'menu': gen_menu()
    }
    return render(request, 'index.html', content)


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


def profile(request, name):
    context = gen_menu()
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
            username='',
            surname='',
            name='',
            city='',
        )
        item.save()
    context['user'] = pers_data
    return render(request, 'profile.html', context)


def login_page(request):
    content = {
        'menu': gen_menu()
    }
    return render(request, 'login.html', content)
# Create your views here.
