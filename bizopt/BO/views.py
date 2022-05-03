import os
import re

from django.shortcuts import render, redirect
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
from .forms import ProductCreateForm
from taggit.models import Tag

def gen_menu(request):
    if request.user.is_authenticated:
        user = Account.objects.get(email=request.user.email)

        context = {
            'user': Account.objects.get(email=request.user.email),
            'menu': [
                {'position': 'out', 'link': '/creators/resume', 'text': 'Исполнители'},
                {'position': 'out', 'link': '/creators/goods', 'text': 'Товары'},
                {'position': 'out', 'link': '/tasks/', 'text': 'Задачи'},
                {'position': 'out', 'link': '', 'text': user.email},
                {'position': 'in', 'link': '/orders/', 'text': 'Корзина'},
                {'position': 'in', 'link': '/addTask/', 'text': 'Создать задачу'},
                {'position': 'in', 'link': '/yourTasks/', 'text': 'Управление задачами'},
                {'position': 'in', 'link': '/becomeCreator/', 'text': 'Стать исполнителем'},
                {'position': 'in', 'link': '/edit/', 'text': 'Настройки профиля'},
                {'position': 'in', 'link': '/logout/', 'text': 'Выйти'},

            ]
        }
    else:
        context = {

            'menu': [
                {'position': 'out', 'link': '/creators/', 'text': 'Исполнители'},
                {'position': 'out', 'link': '/creators/', 'text': 'Товары'},
                {'position': 'out', 'link': '/tasks/', 'text': 'Задачи'},
                {'position': 'out', 'link': 'accounts/login/', 'text': 'Войти'},
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
                            'tag': creator.tag,
                            'avatar': creator.cover.url
                            }
                           for creator in creators]

    return render(request, 'baseResumeCard.html', context)


def yourTasks_page(request):
    content = gen_menu(request)
    tasks = Task.objects.filter(id_creator=request.user)
    content['tasks'] = [{
        'name': task.name,
        'price': task.price,
        'description': task.description
    } for task in tasks]

    return render(request, 'yourTasks.html', content)


def baseProductCard_page(request):
    context = gen_menu(request)
    products = Product_creator.objects.all()
    context['products'] = [{'id': product.id,
                            'product_name': product.product_name,
                            'cost': product.price,
                            'availability': product.availability,
                            'picture': product.picture
                            }
                           for product in products]
    return render(request, 'baseProductCard.html', context)


def addTask_page(request):  # sourcery skip: hoist-statement-from-if
    context = gen_menu(request)
    if request.method == 'POST':
        form = addTasks(request.POST)
        if form.is_valid():
            task = Task()
            task.name = request.POST['task_name']
            task.description = request.POST['description']
            task.price = request.POST['price']
            task.time = request.POST['date']
            task.id_creator = str(request.user)
            task.save()
            task.tags.add(form.cleaned_data['select'])
            task.save()
        context["form"] = form
        return redirect('/yourTasks/')
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
        try:
            creator = Creator.objects.get(email=request.user)
            if request.POST.get('description', None):
                creator.description = request.POST['description']
            if request.POST.get('telegram', None):
                creator.telegram = request.POST['telegram']
            if request.POST.get('vk', None):
                creator.vk = request.POST['vk']
            if request.POST.get('whatsapp', None):
                creator.whatsapp = request.POST['whatsapp']
            if request.POST.get('instagram', None):
                creator.instagram = request.POST['instagram']
            creator.save()
        except:
            creator = Creator()
            if request.FILES:
                file = request.FILES['profile_images']
                fs = FileSystemStorage()
                filename = f"creator_{str(user.email)}.png"
                local_path_to_file = fs.save(os.path.join("images/creator", filename), file)
                creator.cover = local_path_to_file
            creator.first_name = user.first_name
            if request.POST.get('description', None):
                creator.description = request.POST['description']
            if request.POST.get('telegram', None):
                creator.telegram = request.POST['telegram']
            if request.POST.get('vk', None):
                creator.vk = request.POST['vk']
            if request.POST.get('whatsapp', None):
                creator.whatsapp = request.POST['whatsapp']
            if request.POST.get('instagram', None):
                creator.instagram = request.POST['instagram']
            if request.POST.get('published', 0):
                creator.published = request.POST['published']
            creator.email = user.email
            if 'iscompany' in request.POST:
                creator.is_company = True
                creator.company_name = request.POST['profile_company_name']
            else:
                creator.company = False
            creator.save()

    if request.method == 'POST' and "product_creator" in request.POST:  # для создания собственного продукта
        print("PRODUCT_CREATOR")
        product = Product_creator()
        if request.FILES:
            file = request.FILES['product_photos']
            fs = FileSystemStorage()
            local_path_to_file = fs.save(os.path.join("images/products", file.name), file)
            product.picture = local_path_to_file
        #if "product_creator_tags" in request.POST:
        #   form = MyForm(request.POST)
        #   product.tags.add(form.cleaned_data['select'])
        product.product_name = request.POST['product_name']
        product.price = request.POST['price']
        product.description = request.POST['description']
        account = Account.objects.get(email=request.user)
        product.id_creator = account.email
        # TODO: как будет готов фронт для "availability", сохранить ее в БД
        # product.availability = request.POST['??????']
        product.save()
        return redirect('/becomeCreator/')

    if request.method == 'GET' and "product_cards" in request.GET:
        print("CARDS")

    if request.method == 'GET' and "delete" in request.GET:
        print('qq')
        product = Product_creator.objects.get(product_id=request.GET['delete'])
        product.delete()

    if request.method == 'GET' and "status" in request.GET:
        print('keff')
        product = Product_buy.objects.get(id=request.GET['status'])
        product.status1 = 'in work'
        product.status2 = 'in waiting'
        product.save()

    if request.method == "POST" and "partner" in request.POST:
        partner = Partner()
        # TODO: сделать что-то с сохранением единажды на template13
        #  и доделать сохранение с template12 полностью(там заглушка).
        #  Сейчас нет возможности контролировать дублирующихся партнеров по-людски.
        # TODO: как идентифицировать пользователя в будущем? уникальность по email?
        if request.POST.get('INN', None):
            partner.inn = request.POST['INN']
        if request.POST.get('short_name', None):
            partner.name_small = request.POST['short_name']
        if request.POST.get('full_name', None):
            partner.name_full = request.POST['full_name']
        if request.POST.get('payment_account', None):
            partner.payment_account = request.POST['payment_account']
        if request.POST.get('payment_account', None):
            partner.payment_account = request.POST['payment_account']
        if request.POST.get('reg_form', None):
            partner.reg_form = request.POST.get('reg_form', None)
        if request.POST.get('my_first_name', None):
            partner.first_name = request.POST['my_first_name']
        if request.POST.get('my_last_name', None):
            partner.last_name = request.POST['my_last_name']
        if request.POST.get('my_email', None):
            partner.email = request.POST['my_email']
        partner.save()
    return render(request, 'becomeCreator.html', context)



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
#                         password=123,becomeCreator_page
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
    if name == '1':
        try:
            products = Product_buy.objects.filter(id_creator=request.user, status1="in work")
            content['products'] = [{'id': product.id,
                                    'product_name': product.product_name,
                                    'customer': product.id_user_buy,
                                    'status2': product.status2,
                                    }
                                   for product in products]
            products_v = Product_buy.objects.filter(id_creator=request.user, status1="in waiting")
            content['products_v'] = [{'id': product.id,
                                       'product_name': product.product_name,
                                       'customer': product.id_user_buy,
                                       'status1': product.status1,
                                       'id_user_buy': product.id_user_buy,
                                      }
                                     for product in products_v]
        except Product_buy.DoesNotExist as e:
            content['products'] = None 

    elif name == '3':
        account = Account.objects.get(email=request.user)
        products = Product_creator.objects.filter(id_creator=account.email)
        content['products'] = [{'product_name': product.product_name,
                                'cost': product.price,
                                'id': product.product_id,
                                }
                               for product in products]

    elif name == '2':
        form = MyProfile(request.POST)
        content['form1'] = form

    elif name == '6':
        form = ProductCreateForm()
        content['form8'] = form

    elif name == '4':
        try:
            creator = Creator.objects.get(email=request.email)
            content['creator'] = creator
        except:
            creator = Creator()
            content['creator'] = creator

    elif name == '11' or name == '12' or name == '13':
        try:
            partner = Partner.objects.get(email=request.user)
            content['partner'] = {
                'first_name': partner.first_name,
                'last_name': partner.last_name,
                'email': partner.email,
                'INN': partner.inn,
                'name_small': partner.name_small,
                'name_full': partner.name_full,
                'payment_account': partner.payment_account,
                'reg_form': partner.reg_form
            }
        except Exception:
            pass

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
    products = Product_creator.objects.all()
    context['products'] = [{'id': product.id,
                            'product_name': product.product_name,
                            'cost': product.price,
                            'availability': product.availability,
                            'picture': product.picture
                            }
                           for product in products]
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
    if request.method == "POST":
        try:
            product_buy = Product_buy()

            product = Product_creator.objects.get(id=product_id)
            product_buy.id_creator = product.id_creator
            product_buy.product_name = product.product_name

            user_buy = Account.objects.get(email=request.user)
            product_buy.id_user_buy = user_buy.email

            # TODO: как станет возможным добавлять таск, подумать откуда взять task_id
            # product_buy.task_id = 'aaaaaaaaaaaaaaabaaaaaaaaaaaaaaac'
            product_buy.status1 = 'in waiting'
            product_buy.status2 = 'None'
            product_buy.save()
            context['product'] = {'product_name': product.product_name,
                                  'cost': product.price,
                                  'availability': product.availability,
                                  'picture': product.picture,
                                  'description': product.description
                                  }
            return render(request, 'cardProduct.html', context)
        except Task.DoesNotExist as e:
            raise Http404 from e
    else:
        try:
            product = Product_creator.objects.get(id=product_id)
            context['product'] = {'product_name': product.product_name,
                                  'cost': product.price,
                                  'availability': product.availability,
                                  'picture': product.picture,
                                  'description': product.description
                                  }

            return render(request, 'cardProduct.html', context)
        except Task.DoesNotExist as e:
            raise Http404 from e


def cardResume_page(request):
    context = gen_menu(request)
    profile = Creator.objects.get(email=request.user)
    context['profile'] = profile
    products = Product_creator.objects.all()
    context['products'] = [{'id': product.id,
                            'product_name': product.product_name,
                            'cost': product.price,
                            'availability': product.availability,
                            'picture': product.picture,
                            'id_creator': product.id_creator
                            }
                           for product in products]
    return render(request, 'cardResume.html', context)


def cardTask_page(request, task_id):
    context = gen_menu(request)
    try:
        task = Task.objects.get(id=task_id)
        context['task'] = task
        return render(request, 'cardTask.html', context)
    except Task.DoesNotExist as e:
        raise Http404 from e

def editTask_page(request):
    context = gen_menu(request)
    if request.method == 'POST':
        form = addTasks(request.POST)
        if form.is_valid():
            task = Task()
            task.name = request.POST['task_name']
            task.description = request.POST['description']
            task.price = request.POST['price']
            task.time = request.POST['date']
            task.id_creator = str(request.user)
            task.save()
            task.tags.add(form.cleaned_data['select'])
            task.save()
        context["form"] = form
        return redirect('/yourTasks/')
    else:
        form = addTasks()
        context["form"] = form
    return render(request, 'editTask.html', context)

def infoTask_page(request):
    context = gen_menu(request)
    form = addTasks()
    context["form"] = form
    return render(request, 'infoTask.html', context)

def edit_profile(request):
    context = gen_menu(request)
    try:
        email = request.user
        person = Account.objects.get(email=email)
        if request.method == "POST":
            if request.FILES:
                file = request.FILES['profile_photo']
                fs = FileSystemStorage()
                filename = f"profile_{str(person.username)}.png"
                path_to_local_image = os.path.join("images/profile", filename)
                fs.save(path_to_local_image, file)
                person.userImage = path_to_local_image
            if request.POST.get('first_name', None):
                print(request.POST['first_name'])
                person.first_name = request.POST['first_name']
            if request.POST.get('last_name', None):
                person.last_name = request.POST['last_name']
            if request.POST.get('phone', None):
                person.phone = request.POST['phone']
            if request.POST.get('city', None):
                person.city = request.POST['city']
            person.save()
            return HttpResponseRedirect("/")
        else:
            context['user'] = person
            return render(request, "editProfile.html", context)

    except Account.DoesNotExist as e:
        raise Http404 from e


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
    content = gen_menu(request)
    productss = Product_buy.objects.filter(id_user_buy=request.user)
    content['products'] = [{
        'id': product.id,
        'product_name': product.product_name,
        'id_user_buy': product.id_user_buy,
    } for product in productss]

    return render(request, 'orders.html', content)

