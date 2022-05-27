import os
import re

from django.core import paginator
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
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
from .models import Chat_room, Message


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


def post_list(request, tag_slug=None):
    object_list = Product_creator.objects.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    paginator = Paginator(object_list, 3)  # 3 поста на каждой странице
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, поставим первую страницу
        posts = paginator.page(1)
    except EmptyPage:
        # Если страница больше максимальной, доставить последнюю страницу результатов
        posts = paginator.page(paginator.num_pages)

    return render(request,
                  'goodsSearch.html',
                  {'page': page,
                   'posts': posts,
                   'tag': tag})


def gen_menu(request):
    if request.user.is_authenticated:
        user = Account.objects.get(email=request.user.email)

        context = {
            'user': Account.objects.get(email=request.user.email),
            'menu': [
                {'xpos': 'left', 'position': 'out', 'link': '/', 'text': 'BeeFreela'},
                {'xpos': 'center', 'position': 'out', 'link': '/creators/resumes', 'text': 'Исполнители'},
                {'xpos': 'center', 'position': 'out', 'link': '/creators/goods', 'text': 'Товары'},
                {'xpos': 'center', 'position': 'out', 'link': '/tasks/', 'text': 'Задачи'},
                {'xpos': 'right', 'position': 'out', 'link': '', 'text': user.email},
                {'xpos': 'right', 'position': 'in', 'link': '/orders/', 'text': 'Корзина'},
                {'xpos': 'right', 'position': 'in', 'link': '/addTask/', 'text': 'Создать задачу'},
                {'xpos': 'right', 'position': 'in', 'link': '/yourTasks/', 'text': 'Управление задачами'},
                {'xpos': 'right', 'position': 'in', 'link': '/becomeCreator/', 'text': 'Стать исполнителем'},
                {'xpos': 'right', 'position': 'in', 'link': '/edit/', 'text': 'Настройки профиля'},
                {'xpos': 'right', 'position': 'in', 'link': '/partners/', 'text': 'Сотрудничество'},
                {'xpos': 'right', 'position': 'in', 'link': '/logout/', 'text': 'Выйти'},

            ]
        }
    else:
        context = {

            'menu': [
                {'xpos': 'left', 'position': 'out', 'link': '/', 'text': 'BeeFreela'},
                {'xpos': 'center', 'position': 'out', 'link': '/creators/resumes', 'text': 'Исполнители'},
                {'xpos': 'center', 'position': 'out', 'link': '/creators/goods', 'text': 'Товары'},
                {'xpos': 'center', 'position': 'out', 'link': '/tasks/', 'text': 'Задачи'},
                {'xpos': 'right', 'position': 'out', 'link': 'accounts/login/', 'text': 'Войти'},
            ]
        }

    return context

def gen_submenu(request):
    tags = Tag.objects.all()
    context = {
            'submenu': [
                {'xpos': 'left', 'position': 'out', 'link': '', 'text': 'каталог'},

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


def goods_page(request):
    context = gen_menu(request)
    products = Product_creator.objects.all()
    creators = Creator.objects.all()
    context['products'] = [{'id': product.id,
                            'creator_id': product.id_creator,
                            'product_name': product.product_name,
                            'cost': product.price,
                            'availability': product.availability,
                            'picture': product.picture,
                            }
                           for product in products]
    
    return render(request, 'goods.html', context)


def resumes_page(request):
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
        for i in range(0, 16):
            if request.POST.get('key_{}'.format(i), None):
                t += request.POST.get('key_{}'.format(i), ' ')
                t += ','
            else:
                break
                #

        product.set = t
        product.country = request.POST['country']
        account = Account.objects.get(email=request.user)
        product.id_creator = account.email
        # TODO: как будет готов фронт для "availability", сохранить ее в БД
        # product.availability = request.POST['??????']
        product.save()
        return redirect('/becomeCreator/?3')

    if request.method == 'GET' and "product_cards" in request.GET:
        print("CARDS")

    if request.method == 'GET' and "delete" in request.GET:
        product = Product_creator.objects.get(product_id=request.GET['delete'])
        product.delete()
        return redirect('/becomeCreator/?3')

    if request.method == 'GET' and "status" in request.GET:
        product = Product_buy.objects.get(id=request.GET['status'])
        product.status1 = 'in work'
        product.status2 = 'in waiting'
        product.save()
        return redirect('/becomeCreator/?1')
    if request.method == 'GET' and "decline" in request.GET:
        product = Product_buy.objects.get(id=request.GET['decline'])
        product.status1 = 'end_partner'
        product.save()

    if request.method == 'GET' and "decline_work" in request.GET:
        product = Product_buy.objects.get(id=request.GET['decline_work'])
        product.status1 = 'end_partner'
        product.save()
    if request.method == 'GET' and "in_work" in request.GET:
        product = Product_buy.objects.get(id=request.GET['in_work'])
        product.status2 = 'in_work'
        #
        #
        product.save()
    if request.method == 'GET' and "done" in request.GET:
        product = Product_buy.objects.get(id=request.GET['done'])
        product.status2 = 'done'
        product.save()
    if request.method == 'GET' and "payment" in request.GET:
        product = Product_buy.objects.get(id=request.GET['payment'])
        product.status2 = 'payment'
        product.save()
    if request.method == 'GET' and "4" in request.GET:
        product = Product_buy.objects.get(id=request.GET['4'])
        product.status2 = 'end_partner'
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
            '1': 'in_process',
            '2': 'done',
            '3': 'awaiting_payment',
            '4': 'end_partner_late'
        }
        products = Product_buy.objects.all()
        for i in range(len(products)):
            products[i].status2 = statuses[statuses_list[i]]
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

    elif name in ['11', '12', '13']:
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


def cardProduct_page(request, product_id):
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
            product_buy.status1 = 'in waiting'
            product_buy.status2 = 'None'
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
        context['messages'] = messages
         # context['creator'] = creator
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
                            'id_creator': product.id_creator
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

def chat_page(request, id):
    content = {
        'menu': gen_menu(request)
    }
    useremail = request.user
    user = Account.objects.get(email=useremail)
    companion_id = (int(id) - int(user.id)) // int(user.id)
    companion = Creator.objects.get(id=companion_id)
    content['companion'] = companion
    return render(request, 'messanger.html', content)

def checkroom(request):
    room = request.POST['room_name']
    if room.objects.filter(name=room).exist():
        return redirect(f'/{room}/')
    else:
        new_room = Chat_room.objects.create(name=room)
        new_room.save()
        return redirect(f'/{room}/')



def orders_page(request):
    content = gen_menu(request)
    productss = Product_buy.objects.filter(id_user_buy=request.user)
    content['products'] = [{
        'id': product.id,
        'product_name': product.product_name,
        'id_user_buy': product.id_user_buy,
        'status1': product.status1,
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
    return render(request, 'orders.html', content)

def partners_page(request):
    return render(request, 'showPartner.html')

