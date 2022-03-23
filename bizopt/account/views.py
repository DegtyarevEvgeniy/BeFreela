from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from django.views.generic import CreateView

from account.forms import CustomUserCreationForm


def gen_menu():
    context = {
        'menu': [
            {'position': 'out', 'link': '/', 'text': 'Главная'},
            {'position': 'out', 'link': '/creators/', 'text': 'Создатели'},
            # {'position': 'out', 'link': '/employers/', 'text': 'Предприниматели'},
            # {'position': 'mid', 'link': 'accounts/login/', 'text': 'Войти'},
            {'position': 'out', 'link': '/tasks/', 'text': 'Задачи'},
            {'position': 'out', 'link': '', 'text': 'Профиль'},
            {'position': 'in', 'link': '/yourTasks/', 'text': 'Ваши задачи'},
            {'position': 'in', 'link': '', 'text': 'Заказы'},
            {'position': 'in', 'link': '/edit/', 'text': 'Настройки профиля'},
            {'position': 'in', 'link': '/becomeCreator/', 'text': 'Криейтерам'},
            {'position': 'in', 'link': '/logout/', 'text': 'Выйти'},

        ]
    }
    return context


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('/')
    template_name = 'signin.html'

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=True)
            user.save()
            print('kerr')
            return HttpResponseRedirect("/accounts/login/")
        else:
            print(form.errors)
            return render(request, self.template_name, {'form':form})
