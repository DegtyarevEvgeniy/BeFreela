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
from .forms import *
from django.contrib.auth import logout
from django.core.files.storage import FileSystemStorage
from phonenumber_field.modelfields import PhoneNumberField
from account.models import Account
import phonenumbers


def gen_menu(request):
    if request.user.is_authenticated:
        user = Account.objects.get(email=request.user.email)

        context = {
            'user': Account.objects.get(email=request.user.email),
            'menu': [
                {'position': 'out', 'link': '/', 'text': 'Главная'},
                {'position': 'out', 'link': '/creators/', 'text': 'Создатели'},
                # {'position': 'out', 'link': '/employers/', 'text': 'Предприниматели'},
                # {'position': 'mid', 'link': 'accounts/login/', 'text': 'Войти'},
                {'position': 'out', 'link': '/tasks/', 'text': 'Задачи'},
                {'position': 'out', 'link': '', 'text': user.email},
                {'position': 'in', 'link': '/yourTasks/', 'text': 'Ваши задачи'},
                {'position': 'in', 'link': '/orders/', 'text': 'Заказы'},
                {'position': 'in', 'link': '/edit/', 'text': 'Настройки профиля'},
                {'position': 'in', 'link': '/becomeCreator/', 'text': 'Криейтерам'},
                {'position': 'in', 'link': '/logout/', 'text': 'Выйти'},

            ]
        }
    else:
        context = {

            'menu': [
                {'position': 'out', 'link': '/', 'text': 'Главная'},
                {'position': 'out', 'link': '/creators/', 'text': 'Создатели'},
                # {'position': 'out', 'link': '/employers/', 'text': 'Предприниматели'},
                # {'position': 'mid', 'link': 'accounts/login/', 'text': 'Войти'},
                {'position': 'out', 'link': '/tasks/', 'text': 'Задачи'},
                {'position': 'out', 'link': '', 'text': 'user.email'},
                {'position': 'in', 'link': '/yourTasks/', 'text': 'Ваши задачи'},
                {'position': 'in', 'link': '/orders/', 'text': 'Заказы'},
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
    context = gen_menu(request)
    return render(request, 'creators.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")


def baseResumeCard_page(request):
    context = gen_menu(request)
    creators = Creator.objects.all()
    context['creators'] = [{'first_name': creator.first_name,
                            'activity_type': creator.activity_type,
                            'avatar': creator.cover.url
                            }
                           for creator in creators]

    return render(request, 'baseResumeCard.html', context)


def yourTasks_page(request):
    context = gen_menu(request)
    return render(request, 'yourTasks.html', context)


def baseProductCard_page(request):
    context = gen_menu(request)
    products = Product.objects.all()
    context['products'] = [{'id': product.id,
                            'product_name': product.product_name,
                            'cost': product.cost,
                            'availability': product.availability,
                            'picture': product.picture
                            }
                           for product in products]
    return render(request, 'baseProductCard.html', context)


def addTask_page(request):
    context = gen_menu(request)
    if request.method == 'POST':
        form = addTasks(request.POST)
        task = Task()
        task.name = request.POST['task_name']
        task.select = request.POST['select']
        task.description = request.POST['description']
        task.price = request.POST['price']
        task.time = request.POST['data']
        task.save()
        context["form"] = form
    else:
        form = addTasks()
        context["form"] = form
    return render(request, 'addTask.html', context)


def becomeCreator_page(request):
    context = gen_menu(request)
    user = Account.objects.get(email=request.user)
    if request.method == 'POST' and "profile_saver" in request.POST:  # для редактирования профиля
        context['first_name'] = user.first_name
        context['email'] = user.email
        the_same_creator_by_email = Creator.objects.filter(email=user.email)
        if len(the_same_creator_by_email) != 0:
            # TODO: вывести на экране где нибудь сообщение об ошибке, предложенное в данном context
            context[
                'error'] = "You are unable to become another CREATOR because of existed one associated with your account email"
        else:
            creator = Creator()
            if request.FILES:
                file = request.FILES['profile_images']
                # TODO: надо сделать сохранение нескольких фоток товара в базу
                #  и multiple вернуть на фронт
                fs = FileSystemStorage()
                filename = "creator_" + str(user.email) + ".png"
                local_path_to_file = fs.save(os.path.join("images/creator", filename), file)
                creator.cover = local_path_to_file
            creator.first_name = user.first_name
            # TODO: creator.cover и creator.achievements - фантастические поля
            creator.description = request.POST['profile_description']
            creator.email = user.email
            if 'iscompany' in request.POST:
                creator.is_company = True
                creator.company_name = request.POST['profile_company_name']
            else:
                creator.company = False
            creator.save()
    if request.method == 'POST' and "product_creator" in request.POST:  # для создания собственного продукта
        print("PRODUCT_CREATOR")
        product = Product()
        if request.FILES:
            file = request.FILES['product_photos']
            fs = FileSystemStorage()
            # TODO: надо сделать сохранение нескольких фоток товара в базу
            #  и multiple вернуть на фронт
            local_path_to_file = fs.save(os.path.join("images/products", file.name), file)
            product.picture = local_path_to_file
        product.product_name = request.POST['product_name']
        product.cost = request.POST['product_cost']
        product.description = request.POST['product_description']
        # TODO: как будет готов фронт для "availability", сохранить ее в БД
        # product.availability = request.POST['??????']
        product.save()
    if request.method == 'GET' and "product_cards" in request.GET:
        print("CARDS")
    return render(request, 'becomeCreator.html', context)


#
# def edit_profile_page(request):
#     content = {
#         'menu': gen_menu()
#     }
#     if request.method == 'POST':
#         if request.FILES:
#             # получаем загруженный файл
#             file = request.FILES['myfile']
#             fs = FileSystemStorage()
#             # сохраняем на файловой системе
#             filename = fs.save(os.path.join("images", file.name), file)
#             # TODO: Будем сохранять картинку в базу,
#             #       когда напишется логика сохранения всего контента формы в базу
#             #       Текущие недостатки:
#             #           1. /edit должен быть доступен только залогиненым пользователям,
#             #               а значит на странице сразу будут заполнены все поля(имя, ...).
#             #               Сейчас - нет. Поэтому в базу не update, а insert
#             #           2. Нет web-формы на /edit, значит по нажатию на кнопку ничего не случится.
#             #              Добавил кнопку, понимающую только картинку, текстовый контент не отправляется на backend
#             #           3. Что делать, если картинка с именем уже существует.
#             #               а) переименовать на рандом и сохранить.
#             #               б) игнорировать
#             item = Account(login='default',
#                         password=123,
#                         email='example@example.com',
#                         name='Name',
#                         surname='Surname',
#                         phone=123456789,
#                         city='Orlando',
#                         userImage=filename
#                         )
#             item.save()
#             content['imgPath'] = filename
#             return render(request, 'edit.html', content)
#     # content['imgPath'] = '/images/default.png'
#     return render(request, 'edit.html', content)


def becomeCreatorTemplate_page(request, name):
    content = gen_menu(request)
    try:
        creator = Creator.objects.get(email=request.user.email)
        content['first_name'] = creator.first_name
        content['email'] = creator.email
        content['creator_avatar'] = creator.cover
    except:
        user = Account.objects.get(email=request.user.email)
        content['first_name'] = user.first_name
        content['email'] = user.email
        content['creator_avatar'] = user.userImage
    path = f"becomeCreatorTemplates/template{name}.html"
    if name == '3':
        products = Product.objects.all()
        content['products'] = [{'product_name': product.product_name,
                                'cost': product.cost
                                }
                               for product in products]
    if name == '2':
        form = MyProfile(request.POST)
        content['form1'] = form
    return render(request, path, content)


def tasks_page(request):
    context = gen_menu(request)
    tasks = Task.objects.all()
    context['task_cards'] = [{'id': task.id,
                              'name': task.name,
                              'description': task.description
                            } for task in tasks]
    return render(request, 'tasks.html', context)


def employers_page(request):
    context = gen_menu(request)
    return render(request, 'employers.html', context)


def index_page(request):
    context = gen_menu(request)
    return render(request, 'index.html', context)


# def cardProduct_page(request):
#     context = gen_menu()
#     products = Product.objects.all()
#     context['products'] = [{'product_name': product.product_name,
#                             'cost': product.cost
#                             }
#                            for product in products]
#     return render(request, 'cardProduct.html', context)


def cardProduct_page(request, product_id):
    context = gen_menu(request)
    try:
        product = Product.objects.get(id=product_id)
        context['product'] = {'product_name': product.product_name,
                              'cost': product.cost,
                              'availability': product.availability,
                              'picture': product.picture,
                              'description': product.description
                              }

        return render(request, 'cardProduct.html', context)
    except Task.DoesNotExist:
        raise Http404


def cardResume_page(request):
    context = gen_menu(request)
    profile = Creator.objects.get(email=request.user)
    context['profile'] = profile
    return render(request, 'cardResume.html', context)


def cardTask_page(request, task_id):
    context = gen_menu(request)
    try:
        task = Task.objects.get(id=task_id)
        context['task'] = {'name': task.name,
                           'description': task.description
                           }
        return render(request, 'cardTask.html', context)
    except Task.DoesNotExist:
        raise Http404


def edit_profile(request):
    context = gen_menu(request)
    try:
        email = request.user
        person = Account.objects.get(email=email)
        if request.method == "POST":
            if request.FILES:
                file = request.FILES['profile_photo']
                fs = FileSystemStorage()
                filename = "profile_" + str(person.username) + ".png"
                path_to_local_image = os.path.join("images/profile", filename)
                fs.save(path_to_local_image, file)
                person.userImage = path_to_local_image
            person.first_name = request.POST.get("first_name")
            person.last_name = request.POST.get("last_name")
            person.phone = request.POST.get("phone")

            person.city = request.POST.get("city")
            person.save()
            return HttpResponseRedirect("/")
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
    context = gen_menu(request)
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
        'menu': gen_menu(request)
    }
    return render(request, 'edit.html', content)


def login_page(request):
    content = {
        'menu': gen_menu(request)
    }

    return render(request, 'login.html', content)


def forgot_password_page(request):
    content = {
        'menu': gen_menu(request)
    }
    return render(request, 'forgotPassword.html', content)




def orders_page(request):
    content = {
        'menu': gen_menu(request)
    }
    tasks = Task.objects.all()
    content['tasks'] = [{
        'name': task.name,
        'price': task.price,
        'description': task.description
    } for task in tasks]

    return render(request, 'orders.html', content)

