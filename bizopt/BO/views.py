from django.shortcuts import render
from .utils import *
from .forms import *
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, Http404
from .forms import UserRegistrationForm
from django.contrib.auth.models import User

def gen_menu():
    context = {
        'menu': [
            {'position': 'out', 'link': 'http://127.0.0.1:8000/', 'text': 'Главная'},
            {'position': 'out', 'link': 'http://127.0.0.1:8000/creators/', 'text': 'Создатели'},
            # {'position': 'out', 'link': '/employers/', 'text': 'Предприниматели'},
            # {'position': 'mid', 'link': 'accounts/login/', 'text': 'Войти'},
            {'position': 'out', 'link': 'http://127.0.0.1:8000/tasks/', 'text': 'Задачи'},
            {'position': 'out', 'link': '', 'text': 'Профиль'},
            {'position': 'in', 'link': '', 'text': 'Ваши задачи'},
            {'position': 'in', 'link': '', 'text': 'Заказы'},
            {'position': 'in', 'link': 'http://127.0.0.1:8000/edit/', 'text': 'Настройки профиля'},
            {'position': 'in', 'link': 'http://127.0.0.1:8000/becomeCreator/', 'text': 'Криейтерам'},

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


def baseResumeCard_page(request):
    context = gen_menu()
    return render(request, 'baseResumeCard.html', context)


def baseProductCard_page(request):
    context = gen_menu()
    return render(request, 'baseProductCard.html', context)



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
    if request.method == 'POST':

        user = User.objects.create_user(request.POST.get("username"), request.POST.get("email"), request.POST.get("password"))

        user.first_name = request.POST.get("name")
        user.last_name = request.POST.get("surname")
        user.phone = request.POST.get("phone")
        user.city = request.POST.get("city")
        user.save()
        return HttpResponseRedirect("/")
    else:
        print('ky')
        user_form = UserRegistrationForm()
        context['user_form'] = user_form
    return render(request, 'signin.html', context)



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
