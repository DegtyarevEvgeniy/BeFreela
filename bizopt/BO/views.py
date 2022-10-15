import os
from unicodedata import category

from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render, redirect
from django.utils.dateformat import DateFormat
from django.utils.formats import get_format
from django.urls import reverse_lazy
import email
import math
import base64
import requests
import random


from .utils import *
from .forms import *
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404
from .forms import *
# from partner.partners.models import Partner
from django.contrib.auth import logout, authenticate, login
from django.core.files.storage import FileSystemStorage
from account.models import Account
from .forms import ProductCreateForm
from taggit.models import Tag
from .models import Chat_room, Message
from datetime import datetime

from .forms import CustomUserChangeForm



def pageNotAccess(request, exception):
    return render(request, 'errorPages/400.html')
    
def pageMistakeServ(request, exception):
    return render(request, 'errorPages/403.html')

def pageNotFound(request, exception):
    return render(request, 'errorPages/404.html')

def pageNotRequest(request):
    return render(request, 'errorPages/500.html')

def gen_menu(request):
    if request.user.is_authenticated:
        user = Account.objects.get(email=request.user.email)

        return {'user': Account.objects.get(email=request.user.email), }

    else:
        return {}

def upload_image(image, name):

    url = "https://api.imgbb.com/1/upload"
    payload = {
        "key": '4d8bfed1807797ed805abf76382f3ed9',
        "image": base64.b64encode(image.read()),
        "name": name
    }

    res = requests.post(url, payload)
    link = res.text.split('thumb')[-1].split("delete")[0][3:-3].split(",")[-1].split('":"')[-1][:-1].replace('\\', '') 
    name = res.text.split('name":"')[-1].split('"')[0]
    return [link, name]



def gen_submenu(request):
    tags = Tag.objects.all()
    context = {
        'submenu': [
            {'xpos': 'left', 'position': 'out', 'link': '', 'text': 'каталог'},
            {'xpos': 'right', 'position': 'out', 'link': '/orders/', 'text': 'Корзина'},
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
    )
    context['products'] = products
    return render(request, 'goods.html', context)

def goods_page(request):
    context = gen_menu(request)
    products = Product_creator.objects.all()
    context['products'] = products
    for element in context['products']:
        element.flooredrating = math.floor(element.rating)
    # context['products'].show_price = list(filter(None, products.price.split(",")))[0]
    
    return render(request, 'goods.html', context)

def goodsSearch_page_category(request, category):
    context = gen_menu(request)
    cat = {
        'Clothing':'Одежда',
        'Shoes':'Обувь',
        'Bags':'Сумки',
        'Interior':'Интерьер',
        'Accessories':'Аксессуары',
    }
    print(category)
    products = Product_creator.objects.filter( Q(category__icontains=cat[category]) )

    context['category'] = cat[category]
    context['products'] = products
    return render(request, 'goods.html', context)

# def goodsSearch_page_subcategory(request, category, subcategory):
#     context = gen_menu(request)
#     products = Product_creator.objects.filter(
#         Q(product_name__icontains=category) | Q(country__icontains=category) | Q(brand__icontains=category) | Q(category__icontains=category)
#     )
#     products = products.filter(
#         Q(product_name__icontains=subcategory) | Q(country__icontains=subcategory) | Q(brand__icontains=subcategory)
#         | Q(set__icontains=subcategory) | Q(subcategory__icontains=subcategory)
#     )
#     context['products'] = [{'id': product.id,
#                             'product_name': product.product_name,
#                             'cost': product.price,
#                             'availability': product.availability,
#                             }
#                            for product in products]
#     return render(request, 'goodsSearch.html', context)

def brands_page(request):
    user_id = 0
    if request.user.is_authenticated:
        user_id = Account.objects.get(email=request.user.email).id
    context = gen_menu(request)
    creators = Shop.objects.all()
    persons = Account.objects.all()
    # context['persons'] = persons
    brands = Shop.objects.all()
    context['brands'] = [{
        'name': brand.name,
        'logoImage': brand.logoImage,
        'bgImage': brand.bgImage,
        'description': brand.description,
        'category': brand.category,
        'status': brand.status,
        'email': brand.email,
        'phone': brand.phone,
    }for brand in brands]
    context['creators'] = [{'name': creator.name,
                            'logoImage': creator.logoImage,
                            'bgImage': creator.bgImage,
                            'description': creator.description,
                            'category': creator.category,
                            'status': creator.status,
                            'email': creator.email,
                            'phone': creator.phone,
                            }
                           for creator, person in zip(creators, persons)]
    return render(request, 'brands.html', context)

def sertCardBrend_page(request, shopnmae):
    context = gen_menu(request)
    profile = Shop.objects.get(name=shopnmae)
    context['profile'] = profile
    products = Product_creator.objects.all()
    context['products'] = [{'id': product.id,
                            'product_name': product.product_name,
                            'cost': product.price,
                            'availability': product.availability,
                            'picture1': product.picture1,
                            'picture2': product.picture2,
                            'picture3': product.picture3,
                            'id_creator': product.id_creator,
                            }
                           for product in products]
    if request.user.is_authenticated:
        user = Account.objects.get(email=request.user.email)
        context['link'] = (user.id * profile.id) + user.id + profile.id
    return render(request, 'cardBrand.html', context)

def addTask_page(request):  # sourcery skip: hoist-statement-from-if
    context = gen_menu(request)

    if request.method == 'POST':
        form = addTasks(request.POST)
        if form.is_valid() and "addtask" in request.POST:
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
    shop = Shop.objects.get(email=request.user.email)

    if request.method == 'POST' and "profile_saver1" in request.POST:  # для редактирования профиля

        
        user.name_small = request.POST['name_small']
        user.nameFull = request.POST['nameFull']
        user.ogrn = request.POST['ogrn']
        user.inn = request.POST['inn']
        user.kpp = request.POST['kpp']
        user.street = request.POST['street']
        user.fiz_adress = request.POST['fiz_adress']
        user.city = request.POST['city']
        user.index = request.POST['index']
        user.payment_account = request.POST['payment_account']
        user.reg_form = request.POST['reg_form']
        user.bik = request.POST['bik']
        user.korr_check = request.POST['korr_check']
        user.save()
        return HttpResponseRedirect("/becomeCreator/")

    if request.method == 'POST' and "profile_saver2" in request.POST:  # для редактирования профиля

        link_logo = ''
        link_bg = ''


        shop.name = request.POST['name']
        shop.description = request.POST['description']
        shop.status = request.POST['status']
        shop.category = request.POST['chosenCategoties']


        if request.FILES:

            try:
                if request.FILES['logoImage']:

                    file = request.FILES['logoImage']
                    filename = f"prof_{str(shop.email)}"

                    logoImageData = upload_image(file, filename)
                    shop.logoImage = logoImageData[0]
                    # shop.prevLogoImage = logoImageData[-1]

                else:
                    pass
            except:
                pass

            try:
                    
                if request.FILES['bgImage']:

                    file = request.FILES['bgImage']
                    filename = f"bg_{str(shop.email)}"

                    logoImageData = upload_image(file, filename)
                    shop.bgImage = logoImageData[0]

                    # shop.prevLogoImage = logoImageData[-1]

                else:                        
                    pass
            except:
                pass


        shop.save()
        return HttpResponseRedirect("/becomeCreator/")

    if request.method == 'POST' and "product_creator" in request.POST:  # для создания собственного продукта
        product = Product_creator()

        if request.FILES:

            

            file1 = request.FILES['product_photo1']
            file2 = request.FILES['product_photo2']
            file3 = request.FILES['product_photo3']

            filename1 = f'product_photo1_{str(request.user.email)}'
            filename2 = f'product_photo2_{str(request.user.email)}'
            filename3 = f'product_photo3_{str(request.user.email)}'

            logoImageData1 = upload_image(file1, filename1)
            logoImageData2 = upload_image(file2, filename2)
            logoImageData3 = upload_image(file3, filename3)
    
            product.picture1 = logoImageData1[0]
            product.picture2 = logoImageData2[0]
            product.picture3 = logoImageData3[0]

        # if "product_creator_tags" in request.POST:
        #   form = MyForm(request.POST)
        #   product.tags.add(form.cleaned_data['select'])
        product.product_name = request.POST['product_name']
        # product.price = request.POST['price']
        product.description = request.POST['description']
        product.brand = shop.name
        size = ''
        compound_name = ''
        compound_percentage = ''
        compound = ''
        price = ''
        amount = ''
        for i in range(0, 16):
            if request.POST.get(f'size_{i}'):
                size += request.POST.get(f'size_{i}')
                size += ','
            else:
                break
            if request.POST.get(f'compName_{i}'):
                compound_name += request.POST.get(f'compName_{i}')
            if request.POST.get(f'compPercentage_{i}'):
                compound_percentage += request.POST.get(f'compPercentage_{i}')
            if request.POST.get(f'price_{i}'):
                price += request.POST.get(f'price_{i}')
                price += ','
            if request.POST.get(f'amount_{i}'):
                amount += request.POST.get(f'amount_{i}')
                amount += ','
        for name, percentage in zip(compound_name, compound_percentage):
            compound += f"{name} {percentage},"
        compound = list(filter(None, compound.split(",")))
        product.size = size
        product.compound = compound
        product.price = price
        product.amount = amount
        product.show_price = price.split(',')[0]
        product.country = request.POST['country']
        product.category = request.POST['category']
        product.duration = request.POST['duration']
        product.sex = request.POST['sex']
        account = Account.objects.get(email=request.user)
        product.id_creator = account.email
        product.save()
        return HttpResponseRedirect("/becomeCreator/")

    if request.method == 'GET' and "product_cards" in request.GET:
        print("CARDS")

    if request.method == 'GET' and "delete" in request.GET:
        product = Product_creator.objects.get(product_id=request.GET['delete'])
        product.delete()
        return HttpResponseRedirect("/becomeCreator/")

    if request.method == 'POST' and "decline" in request.POST:
        product = Product_buy.objects.get(id=request.POST['decline'])
        product.delete()
        return HttpResponseRedirect("/becomeCreator/")

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





def becomeCreatorTemplate_page(request, name):
    content = gen_menu(request)

    try:
        creator = Shop.objects.get(email=request.user.email)
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
            partner = Partner.objects.get(email=request.user)
            content['partner'] = partner
        except:
            partner = Partner()
            content['partner'] = partner

    elif name == '2':
        user = Account.objects.get(email=request.user)

        try:
             
            creator = Account.objects.get(email=request.user)
            content['creator'] = creator

        except:

            creator.save()


    elif name == '3':
        shop = Shop.objects.get(email=request.user)
        categorys = shop.category
        content['shop'] = shop
        content['categorys_saver'] = categorys
        
        content['categorys'] = categorys.strip().split(' ') if categorys.strip().split(' ') != [""] else ""


    elif name == '4':
        account = Account.objects.get(email=request.user)
        products = Product_buy.objects.filter(id_creator=account.email)
        content['products'] = [{'id': product.id,
                                'id_creator': product.id_creator,
                                'customer': product.id_user_buy,
                                'product_name': product.product_name,
                                'price': product.price,
                                'picture': product.img,
                                }
                            for product in products]
    elif name == '5':
        account = Account.objects.get(email=request.user)
        products = Product_creator.objects.filter(id_creator=account.email)
        content['products'] = [{'id': product.product_id,
                                'id_creator': product.id_creator,
                                'product_name': product.product_name,
                                'country': product.country,
                                'brand': product.brand,
                                'rate_sum': product.rate_sum,
                                'vote_sum': product.vote_sum,
                                'category': product.category,
                                'set': product.size,
                                'price': product.price.split(",")[0],
                                'description': product.description,
                                # 'width_product': product.width_product,
                                # 'height_product': product.height_product,
                                # 'length_product': product.length_product,
                                # 'width_packaging': product.width_packaging,
                                # 'height_packaging': product.height_packaging,
                                # 'length_packaging': product.length_packaging,
                                'availability': product.availability,
                                'picture1': product.picture1,
                                'picture2': product.picture2,
                                'picture3': product.picture3,
                                }
                               for product in products]

    elif name == '6':
        form = ProductCreateForm()
        content['form8'] = form
        content['shop'] = Shop.objects.get(email=request.user.email)

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

# get rundom amount of ids from sertain DB element
def random_DB_id(segment, amount):
    ev_id = [i.id for i in eval('segment.objects.all()')]
    size = amount if amount <= len(ev_id) else len(ev_id)
    id_arr, ret_arr = [], []
    while len(id_arr) != min(len(ev_id), amount):
        id_arr = [*set([ random.choice(ev_id) for i in range(size) ])]  
    for i in range(len(id_arr)):
        ret_arr.append(eval('segment.objects.filter(id = id_arr[i])'))
    return ret_arr



def index_page(request):
    context = gen_menu(request)
    if request.user.is_authenticated:
        context['prom_shops'] =  [i for i in random_DB_id(Shop, 8)]
        context['prom_items'] = [i for i in random_DB_id(Product_creator, 8)]
        return render(request, 'main.html', context)
    else:
        return render(request, 'index.html', context)



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
    context = gen_menu(request)
    product = Product_creator.objects.get(id=product_id)
    shop = Shop.objects.get(email=product.id_creator)
    try:
        if request.method == "POST" and "buy_product" in request.POST:
            product_buy = Product_buy()

            product_buy.price = product.show_price
            product_buy.duration = product.duration
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
            product_buy.amount = request.POST['amount']
            product_buy.status_pay = False
            product_buy.save()
            return HttpResponseRedirect(f'/goods/{product_id}/')
        # else:
        # product = Product_creator.objects.get(id=product_id)
        # creator = Creator.objects.get(email=product.id_creator)
        if request.method == "POST" and "comment_product" in request.POST:
            product = Product_creator.objects.get(id=product_id)
            comment = Comments_product()
            comment.id_creator = product.id_creator
            comment.comentator_email = request.user
            comment.id_product = product.id
            comment.review = request.POST['review']
            comment.rating = request.POST.get('rating', '0')

            product.rate_sum = product.rate_sum + 1
            product.vote_sum = product.vote_sum + int(request.POST.get('rating', '0'))
            product.rating = (product.vote_sum + int(request.POST.get('rating', '0')))/(product.rate_sum + 1)

            comment.save()
            product.save()
            return HttpResponseRedirect(f'/goods/{product_id}/')
        context['product'] = product
        context['product'].show_price = list(filter(None, product.price.split(",")))[0]
        context['product'].sizes = list(filter(None, product.size.split(",")))
        context['product'].prices = list(filter(None, product.price.split(",")))
        context['product'].compounds = list(filter(None, product.compound.split(",")))
        context['product'].rating = float(str(product.rating)[0:4])
        context['product'].flooredrating = math.floor(product.rating)
        context['shop'] = shop



        messages = Comments_product.objects.filter(id_product=product_id)

        id_comment = product.id_creator
        user_product = Account.objects.get(email=id_comment)
        image_user_product = user_product.userImage
        context['image_user_product'] = image_user_product

        for message in messages:
            # передача картинки пользователя, который выложил отзыв
            id_comment = message.comentator_email
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
                filename = f"profile_{str(person.email)}"

                logoImageData = upload_image(file, filename)
                person.userImage = logoImageData[0]
                # shop.prevLogoImage = logoImageData[-1]

             
            if request.POST.get('first_name', None):
                person.first_name = request.POST['first_name']
            if request.POST.get('last_name', None):
                person.last_name = request.POST['last_name']
            if request.POST.get('phone', None):
                person.phone = request.POST['phone']
            if request.POST.get('city', None):
                person.city = request.POST['city']
            person.save()
            return HttpResponseRedirect("/edit/")
        else:
            context['user'] = person
            return render(request, "editProfile.html", context)

    except Account.DoesNotExist as e:
        raise Http404 from e


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
    form = SignUpForm(request.POST)
    context = {
        'form': form
    }
    # вход
    if request.method == 'POST' and 'btnform2' in request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        elif request.POST.get('password') != '':
            print('Try again! username or password is incorrect')
            context['errors'] = 'Try again! username or password is incorrect'
    # регистрация
    elif request.method == 'POST' and 'btnform1' in request.POST:
        # send_mail(
        #     'Test',
        #     'Всё робит)',
        #     'korotikhin84@mail.ru',
        #     ['gaamer557@gmail.com'],
        #     fail_silently=False,
        # )
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')
            username = email
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password, first_name=first_name)
            # login(request, user)
            return redirect('/login/')
        else:
            print(form.errors)

    return render(request, 'signin.html', context)


def signup(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('/')
    else:
        print(form.errors)

    context = {
        'form': form
    }
    return render(request, 'signup.html', context)


def forgot_password_page(request):
    content = {
        'menu': gen_menu(request)
    }
    return render(request, 'forgotPassword.html', content)


def documents_page(request):
    content = {
        'menu': gen_menu(request)
    }
    return render(request, 'documents.html', content)


def documentTemplates_page(request, name):
    content = {
        'menu': gen_menu(request)
    }
    path = f"documentsTemplates/template{name}.html"
    return render(request, path, content)


def chat_page(request, room_id):
    content = {
        'menu': gen_menu(request)
    }

    useremail = request.user
    user = Account.objects.get(email=useremail)
    companion_id = (int(room_id) - int(user.id)) // (int(user.id) + 1)
    companion = Account.objects.get(id=companion_id)
    content['room_id'] = room_id
    content['companion'] = companion
    if not Chat_room.objects.filter(name=room_id).exists():
        new_room = Chat_room.objects.create(name=room_id, user1 = user.id, user2 = companion_id)
        new_room.save()
    return render(request, 'messanger.html', content)

def chat_page_list(request):
    content = {
        'menu': gen_menu(request)
    }
    
    chats = [ chat.name for chat in Chat_room.objects.filter( Q(user1=request.user.id) | Q(user2=request.user.id))]
    components = [ Account.objects.get(id=((int(i) - request.user.id) // request.user.id))  for i in chats ]
    print(components, chats)
    content['chats'] = [ {'chat_room': chat,
                          'first_name': component.first_name,
                          'last_name': component.last_name,
                          'img': component.userImage.url
                          }  for chat, component in zip(chats, components)]
    print(content['chats'])
    return render(request, 'chatRoom.html', content)


def getMsg(request, room_id):
    room_detales = Chat_room.objects.get(name=room_id)
    messages = Message.objects.filter(room=room_detales.name)
    return JsonResponse({"messages": list(messages.values())})

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully.')


def orders_page(request):
    content = gen_menu(request)
    products = Product_buy.objects.filter(id_user_buy=request.user)
    content['products'] = [{'id': product.id,
                        'id_creator': product.id_creator,
                        'id_user_buy': product.id_user_buy,
                        'price': product.price,
                        'product_name': product.product_name,
                        'task_id': product.task_id,
                        'status': product.status,
                        'message': product.message,
                        'payed_partner': product.payed_partner,
                        'payed_user': product.payed_user,
                        'status_pay': product.status_pay,
                        'delivery_address': product.delivery_address,
                        'delivery_address': product.delivery_address,
                        'date_add': product.date_add,
                        'img': product.img,
                        'chat': (Account.objects.get(email=product.id_creator).id * Account.objects.get(email=product.id_user_buy).id) + Account.objects.get(email=product.id_creator).id + Account.objects.get(email=product.id_user_buy).id,
                        } for product in products]
    

    if request.method == "POST" and "decline" in request.POST:
        Product_buy.objects.get(id=request.POST['decline']).delete()
        return HttpResponseRedirect('/orders/')

    return render(request, 'orders.html', content)


def partners_page(request):

    if request.user.is_authenticated:

        if request.method == "POST":
            
            mail = BePartner.objects.create()
            mail.brand_name = request.POST['brand_name']
            mail.name = request.POST['name']
            mail.phone = request.POST['phone']
            mail.city = request.POST['city']
            mail.link = request.POST['link']
            mail.email = request.user.email
            mail.save()
            return HttpResponseRedirect('/')

            
    
        return render(request, 'showPartner.html')
    else:
        return HttpResponseRedirect('/')

def admin_page(request):
    content = gen_menu(request)
    if request.user.is_authenticated and request.user.is_admin and request.user.is_staff and request.user.is_superuser :

        content['partners'] = BePartner.objects.all()
        if request.method == 'POST' and "deletePaartner" in request.POST:
            BePartner.objects.get(id=request.POST['deletePaartner']).delete()
            return HttpResponseRedirect('/admin')
        if request.method == 'POST' and "submitPaartner" in request.POST:
            part = BePartner.objects.get(id=request.POST['submitPaartner'])
            shop = Shop.objects.create()
            user = User.objects.get(email=part.email)
            shop.email = part.email
            shop.phone = part.phone
            shop.name = part.brand_name
            shop.save()

            user.is_partner = 1
            user.save()
            part.delete()
            return HttpResponseRedirect('/admin')
        return render(request, 'admin.html', content)

            
    else:
        return HttpResponseRedirect('/')

