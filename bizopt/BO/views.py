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
            {'position': 'out', 'link': '/', 'text': 'Главная'},
            {'position': 'out', 'link': '/creators/', 'text': 'Создатели'},
            # {'position': 'out', 'link': '/employers/', 'text': 'Предприниматели'},
            {'position': 'mid', 'link': 'accounts/login/', 'text': 'Войти'},
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
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        # Create a new user object but avoid saving it yet
        new_user = user_form.save(commit=False)
        # Set the chosen password
        new_user.set_password(user_form.cleaned_data['password'])
        # Save the User object

        user = User.objects.create_user(request.POST.get("username"), request.POST.get("email"),
                                        request.POST.get("password"))
        user.save()
        # user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')

        # # Обновите поля и сохраните их снова
        # user.first_name = 'John'
        # user.last_name = 'Citizen'
        # user.save()
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
