import os

from django.shortcuts import render
from .utils import *
from .forms import *
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, Http404
from .forms import UserRegistrationForm, addTasks
from django.contrib.auth import logout
from django.core.files.storage import FileSystemStorage

from account.models import Account


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
    creators = Creator.objects.all()
    products = Product.objects.all()
    context['creators'] = [{'first_name': creator.first_name,
                             'activity_type': creator.activity_type
                            }
                            for creator in creators]
    context['products'] = [{'product_name': product.product_name,
                            'cost': product.cost
                            }
                           for product in products]
    return render(request, 'creators.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")

def baseResumeCard_page(request):
    context = gen_menu()
    return render(request, 'baseResumeCard.html', context)

def yourTasks_page(request):
    context = gen_menu()
    return render(request, 'yourTasks.html', context)

def addTask_page(request):
    context = gen_menu()
    return render(request, 'addTask.html', context)

def baseProductCard_page(request):
    context = gen_menu()
    return render(request, 'baseProductCard.html', context)


def addTask_page(request):
    context = gen_menu()
    if request.method == 'POST':
        form = addTasks(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/yourTasks/')
    else:
        form = addTasks()
    return render(request, 'addTask.html', context)


def becomeCreator_page(request):
    context = gen_menu()
    print(request.user)
    user = Account.objects.get(email=request.user)
    if request.method == 'POST' and "profile_saver" in request.POST:   # для редактирования профиля
        context['first_name'] = user.first_name
        # TODO: на фронте не отрисовывается email
        context['email'] = user.email
        if request.FILES:
            file = request.FILES['profile_images']
            fs = FileSystemStorage()
            fs.save(os.path.join("images/creator", file.name), file)
        creator = Creator()
        creator.first_name = user.first_name
        # TODO: creator.cover и creator.achievements - фантастические поля
        creator.description = request.POST['profile_description']
        creator.activity_type = request.POST['profile_activity_type'].split("_")[1]
        if 'iscompany' in request.POST:
            creator.is_company = True
            creator.company_name = request.POST['profile_company_name']
        else:
            creator.company = False
        creator.save()
    if request.method == 'POST' and "product_creator" in request.POST:    # для создания собственного продукта
        print("PRODUCT_CREATOR")
        if request.FILES:
            file = request.FILES['product_photos']
            fs = FileSystemStorage()
            fs.save(os.path.join("images/products", file.name), file)
        product = Product()
        product.product_name = request.POST['product_name']
        product.cost = request.POST['product_cost']
        product.description = request.POST['product_description']
        # TODO: как будет готов фронт для "availability", сохранить ее в БД
        # product.availability = request.POST['??????']
        product.save()
    print(context)
    return render(request, 'becomeCreator.html', context)


def edit_profile_page(request):
    content = {
        'menu': gen_menu()
    }
    if request.method == 'POST':
        if request.FILES:
            # получаем загруженный файл
            file = request.FILES['myfile']
            fs = FileSystemStorage()
            # сохраняем на файловой системе
            filename = fs.save(os.path.join("images", file.name), file)
            # TODO: Будем сохранять картинку в базу,
            #       когда напишется логика сохранения всего контента формы в базу
            #       Текущие недостатки:
            #           1. /edit должен быть доступен только залогиненым пользователям,
            #               а значит на странице сразу будут заполнены все поля(имя, ...).
            #               Сейчас - нет. Поэтому в базу не update, а insert
            #           2. Нет web-формы на /edit, значит по нажатию на кнопку ничего не случится.
            #              Добавил кнопку, понимающую только картинку, текстовый контент не отправляется на backend
            #           3. Что делать, если картинка с именем уже существует.
            #               а) переименовать на рандом и сохранить.
            #               б) игнорировать
            item = Account(login='default',
                        password=123,
                        email='example@example.com',
                        name='Name',
                        surname='Surname',
                        phone=123456789,
                        city='Orlando',
                        userImage=filename
                        )
            item.save()
            content['imgPath'] = filename
            return render(request, 'edit.html', content)
    # content['imgPath'] = '/images/default.png'
    return render(request, 'edit.html', content)


def becomeCreatorTemplate_page(request, name):
    content = gen_menu()
    user = Account.objects.get(email=request.user)
    content['first_name'] = user.first_name
    path = f"becomeCreatorTemplates/template{name}.html"
    return render(request, path, content)


def tasks_page(request):
    context = gen_menu()
    return render(request, 'tasks.html', context)


def employers_page(request):
    context = gen_menu()
    return render(request, 'employers.html', context)


def index_page(request):
    context = gen_menu()
    return render(request, 'index.html', context)


def cardProduct_page(request):
    context = gen_menu()
    return render(request, 'cardProduct.html', context)


def cardResume_page(request):
    context = gen_menu()
    return render(request, 'cardResume.html', context)


def cardTask_page(request):
    context = gen_menu()
    return render(request, 'cardTask.html', context)


def edit_profile(request):
    context = gen_menu()
    try:
        name = request.user
        person = Account.objects.get(username=name)
        if request.method == "POST":
            if request.FILES:
                # TODO: 'tag->name' неизвестен без фронта - "editProfile.html"
                file = request.FILES['tag->name']
                fs = FileSystemStorage()
                fs.save(os.path.join("images/products", file.name), file)
            person.name = request.POST.get("name")
            person.surname = request.POST.get("surname")
            person.city = request.POST.get("city")
            person.save()
            return HttpResponseRedirect("/profile/")
        else:
            context['user'] = person
            return render(request, "editProfile.html", context)

    except Account.DoesNotExist:
        raise Http404

#
# def register(request):
#     context = gen_menu()
#     if request.method == 'POST':
#
#         user = Account.objects.create_user(request.POST.get("username"),
#                                         request.POST.get("email"),
#                                         request.POST.get("password"))
#
#         user.first_name = request.POST.get("name")
#         user.last_name = request.POST.get("surname")
#         user.phone = request.POST.get("phone")
#         user.city = request.POST.get("city")
#         user.save()
#         return HttpResponseRedirect("/accounts/login/")
#     else:
#         print('ky')
#         user_form = UserRegistrationForm()
#         context['user_form'] = user_form
#     return render(request, 'signin.html', context)
#


def profile(request, name):
    context = gen_menu()
    try:
        pers_data = Account.objects.get(username=name)
        pers_data.save()
    except Account.DoesNotExist:
        pers_data = {
            'username': name,
            'name': '',
            'surname': '',
            'city': '',
        }
        item = Account(
            username='',
            surname='',
            name='',
            city='',
        )
        item.save()
    context['user'] = pers_data
    return render(request, 'profile.html', context)


def edit(request):
    content = {
        'menu': gen_menu()
    }
    return render(request, 'edit.html', content)


def login_page(request):
    content = {
        'menu': gen_menu()
    }
    return render(request, 'login.html', content)
# Create your views here.
