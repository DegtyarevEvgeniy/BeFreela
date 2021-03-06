import os
import re

from django.core import paginator
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import formats
from django.utils.dateformat import DateFormat
from django.utils.formats import get_format

from .utils import *
from .forms import *
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404
from .forms import *
from django.contrib.auth import logout
from django.core.files.storage import FileSystemStorage
from phonenumber_field.modelfields import PhoneNumberField
from account.models import Account
import phonenumbers
from .forms import ProductCreateForm
from taggit.models import Tag
from .models import Chat_room, Message
from datetime import datetime

def gen_menu(request):
    if request.user.is_authenticated:
        user = Account.objects.get(email=request.user.email)

        context = {
            'user': Account.objects.get(email=request.user.email),
            'menu': [
                {'xpos': 'left', 'position': 'out', 'link': '/', 'text': 'BeFreela'},
                {'xpos': 'center', 'position': 'out', 'link': '/creators/resumes', 'text': 'Исполнители'},
                {'xpos': 'center', 'position': 'out', 'link': '/creators/goods', 'text': 'Товары'},
                # {'xpos': 'center', 'position': 'out', 'link': '/tasks/', 'text': 'Задачи'},
                {'xpos': 'right', 'position': 'out', 'link': '', 'text': user.email},
                # {'xpos': 'right', 'position': 'in', 'link': '/orders/', 'text': 'Корзина'},
                {'xpos': 'right', 'position': 'in', 'link': '/addTask/', 'text': 'Создать задачу'},
                # {'xpos': 'right', 'position': 'in', 'link': '/yourTasks/', 'text': 'Управление задачами'},
                {'xpos': 'right', 'position': 'in', 'link': '/becomeCreator/', 'text': 'Стать исполнителем'},
                {'xpos': 'right', 'position': 'in', 'link': '/edit/', 'text': 'Настройки профиля'},
                # {'xpos': 'right', 'position': 'in', 'link': '/partners/', 'text': 'Сотрудничество'},
                {'xpos': 'right', 'position': 'in', 'link': '/logout/', 'text': 'Выйти'},

            ]
        }
    else:
        context = {

            'menu': [
                {'xpos': 'left', 'position': 'out', 'link': '/', 'text': 'BeFreela'},
                {'xpos': 'center', 'position': 'out', 'link': '/creators/resumes', 'text': 'Исполнители'},
                {'xpos': 'center', 'position': 'out', 'link': '/creators/goods', 'text': 'Товары'},
                # {'xpos': 'center', 'position': 'out', 'link': '/tasks/', 'text': 'Задачи'},
                {'xpos': 'right', 'position': 'out', 'link': '/accounts/login/', 'text': 'Войти'},
            ]
        }

    return context

def gen_submenu(request):
    tags = Tag.objects.all()
    context = {
            'submenu': [
                # {'xpos': 'left', 'position': 'out', 'link': '', 'text': 'каталог'},

                {'xpos': 'right', 'position': 'out', 'link': '/orders/', 'text': 'Корзина' },
            ],
            'tags': [{'text': tag}
                     for tag in tags]
        }
    return context

def creators_page(request):
    context = gen_menu(request)
    return render(request, 'creators.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")

def yourTasks_page(request):
    content = gen_menu(request)
    tasks = Task.objects.filter(id_creator=request.user)
    content['tasks'] = [{
        'id': task.id,
        'name': task.name,
        'price': task.price,
        'description': task.description,
        'time': task.time,
        'status': task.status1,
    } for task in tasks]

    return render(request, 'yourTasks.html', content)

def goodsSearch_page(request, product_name):
    context = gen_menu(request)
    products = Product_creator.objects.filter(
        Q(product_name__icontains=product_name) | Q(country__icontains=product_name) | Q(brand__icontains=product_name)
        | Q(set__icontains=product_name)
    )
    print(products)
    context['products'] = [{'id': product.id,
                            'product_name': product.product_name,
                            'cost': product.price,
                            'availability': product.availability,
                            'picture': product.picture
                            }
                           for product in products]
    return render(request, 'goodsSearch.html', context)

def goods_page(request):
    context = gen_menu(request)
    creators = Creator.objects.all()
    products = Product_creator.objects.all()
    if request.method == "POST":
        rating = request.POST.get('rating', '')
        print(rating)

        if rating == '1':
            products = Product_creator.objects.filter(
                Q(rating_status__icontains=4) | Q(
                    rating_status__icontains=3)
                | Q(rating_status__icontains=2) | Q(rating_status__icontains=5)
            )
            # print("kyy")
        elif rating == '2':
            products = Product_creator.objects.filter(
                Q(rating_status__icontains=5)
                | Q(rating_status__icontains=4) | Q(rating_status__icontains=3)
            )
            # print("kyyy")
        elif rating == '3':
            products = Product_creator.objects.filter(
                Q(rating_status=5) | Q(rating_status__icontains=4)
            )
            # print("kyyyy")
            print(products)
        elif rating == '4':
            products = Product_creator.objects.filter(
                Q(rating_status__icontains=5) | Q(rating_status__icontains=4) | Q(
                    rating_status__icontains=3)
                | Q(rating_status__icontains=2) | Q(rating_status__icontains=1)
            )
            # print("kyyyyy")
    print(products)
    context['products'] = [{'id': product.id,
                            # 'creator_id':  Account.objects.get(email=product.id_creator).id, Раскоментировать если не надо видеть свои карточки
                            'product_name': product.product_name,
                            'cost': product.price,
                            'availability': product.availability,
                            'picture': product.picture,
                            'rating': product.rating,
                            'rating_status': product.rating_status,
                            }
                           for product in products]
    return render(request, 'goods.html', context)


def resumes_page(request):
    user_id = 0
    if request.user.is_authenticated:
        user_id = Account.objects.get(email=request.user.email).id
    context = gen_menu(request)
    creators = Creator.objects.all()
    persons = Account.objects.all()
    # context['persons'] = persons
    context['creators'] = [{'id':creator.id,
                            'username': creator.username,
                            'first_name':creator.first_name,
                            'email':person,
                            'cover':creator.cover,
                            'description':creator.description,
                            'is_company':creator.is_company,
                            'company_name':creator.company_name,
                            'telegram':creator.telegram,
                            'vk':creator.vk,
                            'whatsapp':creator.whatsapp,
                            'instagram':creator.instagram,
                            'tag':creator.tag,
                            'published':creator.published,
                            'link': (user_id * creator.id) + user_id + creator.id
                            }
                           for creator, person in zip(creators, persons)]
    return render(request, 'resumes.html', context)

def addTask_page(request):  # sourcery skip: hoist-statement-from-if
    context = gen_menu(request)

    if request.method == 'POST':
        form = addTasks(request.POST)
        if form.is_valid() and "addtask" in request.POST:
            print('kkk')
            task = Task()
            task.name = request.POST['task_name']
            task.description = request.POST['description']
            task.price = request.POST['price']
            task.time = request.POST['date']
            task.id_creator = str(request.user)
            task.save()
            task.tags.add(request.POST['tag'])
            task.save()
            return redirect('/yourTasks/')
        context["form"] = form

    else:
        form = addTasks()
        context["form"] = form
    return render(request, 'addTask.html', context)


def becomeCreator_page(request):  # sourcery skip: low-code-quality
    context = gen_menu(request)
    user = Account.objects.get(email=request.user)

    if request.method == 'POST' and "profile_saver" in request.POST:  # для редактирования профиля
        context['first_name'] = user.first_name
        context['email'] = user.email
        try:
            creator = Creator.objects.get(email=request.user)
            creator.description = request.POST['description']
            creator.telegram = request.POST['telegram']
            creator.vk = request.POST['vk']
            creator.whatsapp = request.POST['whatsapp']
            creator.instagram = request.POST['instagram']
            creator.username = request.user.username
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
            creator.username = request.user.username
            creator.description = request.POST['profile_description']
            creator.telegram = request.POST['telegram']
            creator.vk = request.POST['vk']
            creator.whatsapp = request.POST['whatsapp']
            creator.instagram = request.POST['instagram']
            creator.published = request.POST['published']
            creator.email = user.email
            if 'iscompany' in request.POST:
                creator.is_company = True
                creator.company_name = request.POST['profile_company_name']
            else:
                creator.is_company = False
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
        product.brand = request.POST['brand']
        t = ''
        print(request.POST)
        for i in range(0, 16):
            if request.POST.get('set_{}'.format(i), None):
                t += request.POST.get('set_{}'.format(i), ' ')
                t += ','
            else:
                break

        product.set = t

        product.country = request.POST['country']
        product.height_packaging = request.POST.get('height_packaging', '0')
        product.height_product = request.POST.get('height_product', '0')
        product.length_packaging = request.POST.get('length_packaging', '0')
        product.length_product = request.POST.get('length_product', '0')
        product.width_packaging = request.POST.get('width_packaging', '0')
        product.width_product = request.POST.get('width_product', '0')
        account = Account.objects.get(email=request.user)
        product.id_creator = account.email
        # TODO: как будет готов фронт для "availability", сохранить ее в БД
        # product.availability = request.POST['??????']
        product.save()
        for i in range(0, 16):
            if request.POST.get('key_{}'.format(i), None):
                product.tags.add(request.POST.get('key_{}'.format(i), ' '))
                product.save()
            else:
                break
        return redirect('/becomeCreator/')

    if request.method == 'GET' and "product_cards" in request.GET:
        print("CARDS")

    if request.method == 'GET' and "delete" in request.GET:
        product = Product_creator.objects.get(product_id=request.GET['delete'])
        product.delete()
        return redirect('/becomeCreator/')

    if request.method == 'POST' and "status" in request.POST:
        product = Product_buy.objects.get(id=request.POST['status'])
        product.status = 'Заказ в работе'
        product.save()
        return redirect('/becomeCreator/')
    if request.method == 'GET' and "in_work" in request.POST:
        product = Product_buy.objects.get(id=request.POST['in_work'])
        product.status = 'Заказ в работе'
        product.save()
    if request.method == 'POST' and "done" in request.POST:
        product = Product_buy.objects.get(id=request.POST['done'])
        product.status = 'Заказ готов'
        product.save()
    if request.method == 'POST' and "payment" in request.POST:
        product = Product_buy.objects.get(id=request.GET['payment'])
        product.status = 'Заказ оплачен'
        product.save()
    if request.method == 'POST' and "decline" in request.POST:
        product = Product_buy.objects.get(id=request.POST['decline'])
        product.status = 'Заказчик отказался от заказа'
        product.save()
    if request.method == 'GET' and "decline_work" in request.GET:
        product = Product_buy.objects.get(id=request.GET['decline_work'])
        product.status = 'Заказчик отказался от заказа'
        product.save()
    if request.method == 'GET' and "4" in request.GET:
        product = Product_buy.objects.get(id=request.GET['4'])
        product.status = 'Заказчик отказался от заказа'
        product.save()

    if request.method == "POST" and "partner" in request.POST:
        try:
            partner = Partner.objects.get(email=request.user)
            partner.inn = request.POST['INN']
            partner.name_small = request.POST['short_name']
            partner.payment_account = request.POST['payment_account']
            partner.reg_form = request.POST['reg_form']
            partner.first_name = request.POST['my_first_name']
            partner.last_name = request.POST['my_last_name']
            partner.email = user.email
            partner.save()
        except:
            partner = Partner()
            partner.inn = request.POST['INN']
            partner.name_small = request.POST['short_name']
            partner.payment_account = request.POST['payment_account']
            partner.reg_form = request.POST['reg_form']
            partner.first_name = request.POST['my_first_name']
            partner.last_name = request.POST['my_last_name']
            partner.email = user.email
            partner.save()

    if request.method == 'POST' and "products_in_work" in request.POST:
        print("products_in_work")
        statuses_list = request.POST.getlist('services')
        # TODO: БЕЗ ЭТОГО СЛОВАРЯ ВОЗМОЖНЫХ ЗНАЧЕНИЙ СТАТУСА ВСЕ СЛОМАЕТСЯ!!!!!
        #  ПРОВЕРИТЬ СООТВЕТСТВИЕ СЛОВАРЯ ЗНАЧЕНИЯМ НА ФРОНТЕ!

        statuses = {
            '1': 'Заказ в работе',
            '2': 'Заказ готов',
            '3': 'Заказ в ожидании оплаты',
            '4': 'Заказчик отказался от заказа'
        }
        products = Product_buy.objects.all()
        for i in range(len(products)):
            products[i].status = statuses[statuses_list[i]]
            products[i].save()
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
        print(request.user.email, creator.id)
        content['first_name'] = creator.first_name
        content['email'] = creator.email
        content['creator_avatar'] = creator.cover
    except:
        user = Account.objects.get(email=request.user.email)
        content['first_name'] = user.first_name
        content['email'] = user.email
        content['creator_avatar'] = user.userImage
    path = f"becomeCreatorTemplates/template{name}.html"
    if name == '2':
        try:
            products = Product_buy.objects.filter(id_creator=request.user)
            content['products'] = [{'id': product.id,
                                    'product_name': product.product_name,
                                    'customer': product.id_user_buy,
                                    'st':product.status,
                                    'status1': 'red' if product.status[-1] == 'е' else 'blue',
                                    'status2': 'red' if product.status[-1] == 'о' else 'blue',
                                    'status3': 'red' if product.status[-1] == 'ы' else 'blue',
                                    'chat_id':(creator.id * Account.objects.get(email=product.id_user_buy).id) + creator.id + Account.objects.get(email=product.id_user_buy).id

                                    }
                                   for product in products]
            products_v = Product_buy.objects.filter(id_creator=request.user)
            if products_v.count() > 0:
                content['products_v'] = [{'id': product.id,
                                       'product_name': product.product_name,
                                       'customer': product.id_user_buy,
                                       'status': product.status,
                                       'id_user_buy': product.id_user_buy,
                                       'chat_id':(creator.id * Account.objects.get(email=product.id_user_buy).id) + creator.id + Account.objects.get(email=product.id_user_buy).id
                                      }
                                     for product in products_v]
            
        
        except Product_buy.DoesNotExist as e:
            content['products'] = None

    # elif name == '3':
        # form = MyProfile(request.POST)
        # content['form1'] = form

    elif name == '3':
        account = Account.objects.get(email=request.user)
        products = Product_creator.objects.filter(id_creator=account.email)
        content['products'] = [{'product_name': product.product_name,
                                'cost': product.price,
                                'id': product.product_id,
                                }
                               for product in products]

    elif name == '4':
        try:
            creator = Creator.objects.get(email=request.user)
            content['creator'] = creator
        except:
            creator = Creator()
            content['creator'] = creator

    elif name == '1':
        try:
            partner = Partner.objects.get(email=request.user)
            content['partner'] = partner
        except:
            partner = Partner()
            content['partner'] = partner
    
    elif name == '6':
        form = ProductCreateForm()
        content['form8'] = form

    # elif name in ['11', '12', '13']:
    #     try:
    #         partner = Partner.objects.get(email=request.user)
    #         content['partner'] = {
    #             'first_name': partner.first_name,
    #             'last_name': partner.last_name,
    #             'email': partner.email,
    #             'INN': partner.inn,
    #             'name_small': partner.name_small,
    #             'name_full': partner.name_full,
    #             'payment_account': partner.payment_account,
    #             'reg_form': partner.reg_form
    #         }
    #     except Exception:
    #         pass

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
    context = {**gen_menu(request), **gen_submenu(request)}
    products = Product_creator.objects.all()
    context['products'] = [{'id': product.id,
                            'product_name': product.product_name,
                            'cost': product.price,
                            'availability': product.availability,
                            'picture': product.picture,
                            'description': product.description
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



def sertCardResume_page(request, username):
    context = gen_menu(request)
    useremail = request.user
    user = Account.objects.get(email=useremail)

    profile = Creator.objects.get(username=username)
    context['profile'] = profile
    products = Product_creator.objects.all()
    context['products'] = [{'id': product.id,
                            'product_name': product.product_name,
                            'cost': product.price,
                            'availability': product.availability,
                            'picture': product.picture,
                            'id_creator': product.id_creator,

                            }
                           for product in products]

    context['link'] = (user.id * profile.id) + user.id + profile.id
    return render(request, 'cardResume.html', context)


def cardTask_page(request, task_id):
    context = gen_menu(request)
    try:
        task = Task.objects.get(id=task_id)
        context['task'] = task
        return render(request, 'cardTask.html', context)
    except Task.DoesNotExist as e:
        raise Http404 from e

def cardProduct_page(request, product_id):
    flag = "day"
    dt = datetime.now()
    df = DateFormat(dt)
    df.format(get_format('DATE_FORMAT'))

    context = {**gen_menu(request), **gen_submenu(request)}
    product = Product_creator.objects.get(id=product_id)

    try:
        if request.method == "POST" and "buy_product" in request.POST:
            product_buy = Product_buy()

            # product = Product_creator.objects.get(id=product_id)
            product_buy.id_creator = product.id_creator
            product_buy.product_name = product.product_name

            user_buy = Account.objects.get(email=request.user)
            product_buy.id_user_buy = user_buy.email

            # TODO: как станет возможным добавлять таск, подумать откуда взять task_id
            # product_buy.task_id = 'aaaaaaaaaaaaaaabaaaaaaaaaaaaaaac'
            product_buy.status = 'Заказ принят на рассмотрение'
            product_buy.message = request.POST['message']
            product_buy.delivery_address = request.POST['address']
            product_buy.status_pay = False
            product_buy.save()
        # else:
        # product = Product_creator.objects.get(id=product_id)
        # creator = Creator.objects.get(email=product.id_creator)
        if request.method == "POST" and "comment_product" in request.POST:
            # product = Product_creator.objects.get(id=product_id)
            comment = Comments_product()
            comment.id_creator = product.id_creator
            comment.id_product = product.id
            comment.review = request.POST['review']
            comment.rating = request.POST.get('rating', '0')
            comment.save()
        context['products'] = product

        messages = Comments_product.objects.filter(id_product=product_id)

        id_comment = product.id_creator
        user_product = Account.objects.get(email=id_comment)
        image_user_product = user_product.userImage
        context['image_user_product'] = image_user_product

        for message in messages:
            # передача картинки пользователя, который выложил отзыв
            id_comment = message.id_creator
            user_comment = Account.objects.get(email=id_comment)
            image_user = user_comment.userImage
            message.image_user = image_user

            # передача даты создания отзыва
            df_message = DateFormat(message.created_data)
            df_message.format(get_format('DATE_FORMAT'))
            if (int(df_message.y()) - int(df.y()) == 0) and (int(df_message.m()) - int(df.m()) == 0):
                message.created_data = int(df.d()) - int(df_message.d())
                message.flag = flag
            elif (int(df_message.y()) - int(df.y()) == 0) and (int(df_message.m()) - int(df.m()) != 0):
                message.flag = "month"
                message.created_data = int(df_message.m()) - int(df.m())
                context['flag'] = flag

            else:
                message.flag = "year"
                message.created_data = int(df_message.y()) - int(df.y())
                print(message.created_data)
                context['flag'] = flag


        context['messages'] = messages

        return render(request, 'cardProduct.html', context)
    except Task.DoesNotExist as e:
        raise Http404 from e

def editTask_page(request, task_id):
    context = gen_menu(request)
    try:
        if request.method == 'POST':
            form = addTasks(request.POST)
            if form.is_valid():
                task = Task.objects.get(id=task_id)
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
    except Account.DoesNotExist as e:
        raise Http404 from e

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

def chat_page(request, room_id):
    content = {
        'menu': gen_menu(request)
    }
    useremail = request.user
    user = Account.objects.get(email=useremail)
    companion_id = (int(room_id) - int(user.id)) // (int(user.id) + 1)
    print(user.id)
    print(companion_id)
    companion = Creator.objects.get(id=companion_id)
    content['room_id'] = room_id
    content['companion'] = companion
    if not Chat_room.objects.filter(name=room_id).exists():
        new_room = Chat_room.objects.create(name=room_id)
        new_room.save()
    return render(request, 'messanger.html', content)    

def getMsg(request, room_id):
    room_detales = Chat_room.objects.get(name=room_id)
    messages = Message.objects.filter(room=room_detales.name)
    return JsonResponse({"messages":list(messages.values())})

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully.')

def orders_page(request):
    content = gen_menu(request)
    productss = Product_buy.objects.filter(id_user_buy=request.user)
    content['products'] = [{
        'id': product.id,
        'product_name': product.product_name,
        'id_user_buy': product.id_user_buy,
        'status': product.status,
    } for product in productss]
    if request.method == "POST" and "comment_product" in request.POST:
        product_id = request.POST['comment_product']
        product = Product_creator.objects.get(id=product_id)
        comment = Comments_product()
        comment.id_creator = product.id_creator
        comment.id_product = product.id
        comment.review = request.POST['review']
        comment.rating = request.POST.get('rating', '0')
        comment.save()
    if request.method == "POST" and "decline" in request.POST:
        product = Product_buy.objects.get(id=request.POST['decline'])
        product.status = 'Заказчик отказался от заказа'
        product.save()

    return render(request, 'orders.html', content)

def partners_page(request):
    return render(request, 'showPartner.html')

