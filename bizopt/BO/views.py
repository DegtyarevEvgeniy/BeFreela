from django.shortcuts import render
from .utils import *
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import *
from .models import *
from django.http import HttpResponseRedirect, Http404

def gen_menu():
    context = {
        'menu': [
            {'position': 'out', 'link': '/', 'text': 'Главная'},
            {'position': 'out', 'link': '/creators/', 'text': 'Создатели'},
            # {'position': 'out', 'link': '/employers/', 'text': 'Предприниматели'},
            # {'position': 'mid', 'link': '/login/', 'text': 'Войти'},
            {'position': 'out', 'link': '/tasks/', 'text': 'Задачи'},
            {'position': 'out', 'link': '', 'text': 'Профиль'},
            {'position': 'in', 'link': '', 'text': 'Ваши задачи'},
            {'position': 'in', 'link': '', 'text': 'Заказы'},
            {'position': 'in', 'link': 'edit/', 'text': 'Настройки профиля'},
            {'position': 'in', 'link': '', 'text': 'Криейтерам'},
            {'position': 'in', 'link': '', 'text': 'Выйти'},
        ]
    }
    return context

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
    context = gen_menu()
    return render(request, 'creators.html', context)


def becomeCreator_page(request):
    context = gen_menu()
    return render(request, 'becomeCreator.html', context)


def tasks_page(request):
    context = gen_menu()
    return render(request, 'tasks.html', context)


def employers_page(request):
    context = gen_menu()
    return render(request, 'employers.html', context)


def index_page(request):
    context = gen_menu()
    return render(request, 'index.html', context)


def edit_profile(request, name):
    context = gen_menu()
    try:
        person = User.objects.get(login=name)
        if request.method == "POST":
            person.name = request.POST.get("name")
            person.surname = request.POST.get("surname")
            person.city = request.POST.get("city")
            person.save()
            print(person.name)
            return HttpResponseRedirect("/profile/")
        else:
            context['user']=person
            return render(request, "editProfile.html", context)

    except User.DoesNotExist:
        raise Http404


def register(request):
    context = gen_menu()

    if request.method == "POST":
        user = UserForm(request.POST)
        u_data = user.data
        item = User(login=u_data["login"],
                    password=u_data["password"],
                    name=u_data["name"],
                    surname=u_data["surname"],
                    phone=u_data["phone"],
                    email=u_data["email"],
                    city=u_data["city"])
        item.save()

        print('ky')
    form = UserForm()
    context['form'] = form
    return render(request, "signin.html", context)


def login(request):
    context = gen_menu()
    form = UserLoginForm()
    context['form'] = form
    formm = UserLoginForm(request.POST)
    if formm.is_valid():
        form_data = formm.data
        if (form_data['login'],) in User.objects.values_list('login'):
            user_data = User.objects.get(login=form_data['login'])
            if user_data['password'] == form_data['password']:
                return render(request, 'login.html', context)
            else:
                return render(request, 'login.html', context)


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
