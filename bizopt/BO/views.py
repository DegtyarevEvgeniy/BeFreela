import email
import os
from unicodedata import category

from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render, redirect
from django.utils.dateformat import DateFormat
from django.utils.formats import get_format

from django.urls import reverse_lazy



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
    creators = Shop.objects.all()
    products = Product_creator.objects.all()
    if request.method == "POST":
        rating = request.POST.get('rating', '')
        print(rating)

        # if rating == '1':
        #     products = Product_creator.objects.filter(
        #         Q(rating_status__icontains=4) | Q(
        #             rating_status__icontains=3)
        #         | Q(rating_status__icontains=2) | Q(rating_status__icontains=5)
        #     )
        #     # print("kyy")
        # elif rating == '2':
        #     products = Product_creator.objects.filter(
        #         Q(rating_status__icontains=5)
        #         | Q(rating_status__icontains=4) | Q(rating_status__icontains=3)
        #     )
        #     # print("kyyy")
        # elif rating == '3':
        #     products = Product_creator.objects.filter(
        #         Q(rating_status=5) | Q(rating_status__icontains=4)
        #     )
        #     # print("kyyyy")
        #     print(products)
        # elif rating == '4':
        #     products = Product_creator.objects.filter(
        #         Q(rating_status__icontains=5) | Q(rating_status__icontains=4) | Q(
        #             rating_status__icontains=3)
        #         | Q(rating_status__icontains=2) | Q(rating_status__icontains=1)
        #     )
            # print("kyyyyy")
    print(products)
    context['products'] = [{'id': product.id,
                            # 'creator_id':  Account.objects.get(email=product.id_creator).id, Раскоментировать если не надо видеть свои карточки
                            'product_name': product.product_name,
                            'cost': product.price,
                            'availability': product.availability,
                            'picture': product.picture,
                            'rating': product.rating,
                            'rate_sum': product.rate_sum,
                            'vote_sum': product.vote_sum,
                            'country': product.country,
                            }
                           for product in products]
    return render(request, 'goods.html', context)

def goodsSearch_page_category(request, category):
    context = gen_menu(request)
    products = Product_creator.objects.filter(
        Q(product_name__icontains=category) | Q(country__icontains=category) | Q(brand__icontains=category)
        | Q(set__icontains=category) | Q(category__icontains=category)
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

# def goodsSearch_page_subcategory(request, category, subcategory):
#     context = gen_menu(request)
#     products = Product_creator.objects.filter(
#         Q(product_name__icontains=category) | Q(country__icontains=category) | Q(brand__icontains=category)
#         | Q(set__icontains=category) | Q(category__icontains=category)
#     )
#     products = products.filter(
#         Q(product_name__icontains=subcategory) | Q(country__icontains=subcategory) | Q(brand__icontains=subcategory)
#         | Q(set__icontains=subcategory) | Q(subcategory__icontains=subcategory)
#     )
#     print(products)
#     context['products'] = [{'id': product.id,
#                             'product_name': product.product_name,
#                             'cost': product.price,
#                             'availability': product.availability,
#                             'picture': product.picture
#                             }
#                            for product in products]
#     return render(request, 'goodsSearch.html', context)

def resumes_page(request):
    user_id = 0
    if request.user.is_authenticated:
        user_id = Account.objects.get(email=request.user.email).id
    context = gen_menu(request)
    creators = Shop.objects.all()
    persons = Account.objects.all()
    # context['persons'] = persons
    brands = Shop.objects.all().values('name')
    print(brands)
    context['brands'] = [{'text': brand}
                         for brand in brands]
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

    print(request.POST)

    if request.method == 'POST' and "profile_saver1" in request.POST:  # для редактирования профиля

        creator = Account.objects.get(email=request.user)
        creator.name_small = request.POST['name_small']
        creator.nameFull = request.POST['nameFull']
        creator.ogrn = request.POST['ogrn']
        creator.inn = request.POST['inn']
        creator.kpp = request.POST['kpp']
        creator.street = request.POST['street']
        creator.fiz_adress = request.POST['fiz_adress']
        creator.city = request.POST['city']
        creator.index = request.POST['index']
        creator.payment_account = request.POST['payment_account']
        creator.reg_form = request.POST['reg_form']
        creator.bik = request.POST['bik']
        creator.korr_check = request.POST['korr_check']

        creator.save()

    if request.method == 'POST' and "profile_saver2" in request.POST:  # для редактирования профиля

        shop = Shop.objects.get(email=request.user.email)


        shop.name = request.POST['name']
        shop.description = request.POST['description']
        shop.status = request.POST['status']
        shop.category = request.POST['chosenCategoties']


        # if request.FILES:
        print(request.FILES)
        if request.FILES:
            file1 = request.FILES['logoImage']
            file2 = request.FILES['bgImage']
            fs = FileSystemStorage()
            filename1 = f"profile_{str(shop.email)}.png"
            filename2 = f"profile_{str(shop.email)}.png"

            path_to_local_image1 = os.path.join("images/creator/logoImage", filename1)
            fs.save(path_to_local_image1, file1)

            path_to_local_image2 = os.path.join("images/creator/bgImage", filename2)
            fs.save(path_to_local_image2, file2)

            shop.userImage = path_to_local_image1
            shop.userImage = path_to_local_image2


        shop.save()

    if request.method == 'POST' and "product_creator" in request.POST:  # для создания собственного продукта
        print("PRODUCT_CREATOR")
        product = Product_creator()
        if request.FILES:
            file = request.FILES['product_photos']
            fs = FileSystemStorage()
            local_path_to_file = fs.save(os.path.join("images/products", file.name), file)
            product.picture = local_path_to_file

        # if "product_creator_tags" in request.POST:
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
        product.category = request.POST['category']
        # product.subcategory = request.POST['subcategory']
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

    # if request.method == 'POST' and "status" in request.POST:
    #     product = Product_buy.objects.get(id=request.POST['status'])
    #     product.status = 'Заказ в работе'
    #     product.save()
    #     return redirect('/becomeCreator/')
    # if request.method == 'GET' and "in_work" in request.POST:
    #     product = Product_buy.objects.get(id=request.POST['in_work'])
    #     product.status = 'Заказ в работе'
    #     product.save()
    # if request.method == 'POST' and "done" in request.POST:
    #     product = Product_buy.objects.get(id=request.POST['done'])
    #     product.status = 'Заказ готов'
    #     product.save()
    # if request.method == 'POST' and "payment" in request.POST:
    #     product = Product_buy.objects.get(id=request.GET['payment'])
    #     product.status = 'Заказ оплачен'
    #     product.save()
    # if request.method == 'POST' and "decline" in request.POST:
    #     product = Product_buy.objects.get(id=request.POST['decline'])
    #     product.status = 'Заказчик отказался от заказа'
    #     product.save()
    # if request.method == 'GET' and "decline_work" in request.GET:
    #     product = Product_buy.objects.get(id=request.GET['decline_work'])
    #     product.status = 'Заказчик отказался от заказа'
    #     product.save()
    # if request.method == 'GET' and "4" in request.GET:
    #     product = Product_buy.objects.get(id=request.GET['4'])
    #     product.status = 'Заказчик отказался от заказа'
    #     product.save()

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





def becomeCreatorTemplate_page(request, name):
    content = gen_menu(request)

    try:
        creator = Shop.objects.get(email=request.user.email)
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
              # для редактирования профиля

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
        try:
            creator = Shop.objects.get(email=request.user)
            content['creator'] = creator
        except:
            creator = Shop()
            content['creator'] = creator

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
                                'set': product.set,
                                'price': product.price,
                                'description': product.description,
                                'width_product': product.width_product,
                                'height_product': product.height_product,
                                'length_product': product.length_product,
                                'width_packaging': product.width_packaging,
                                'height_packaging': product.height_packaging,
                                'length_packaging': product.length_packaging,
                                'availability': product.availability,
                                'picture': product.picture,
                                }
                               for product in products]

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

# def partnerTemplate_page(request, name):
#     content = {}
#     try:
#         creator = Creator.objects.get(email=request.user.email)
#         print(request.user.email, creator.id)
#         content['first_name'] = creator.first_name
#         content['email'] = creator.email
#         content['creator_avatar'] = creator.cover
#     except:
#         user = Partner.objects.get(email=request.user.email)
#         content['first_name'] = user.first_name
#         content['email'] = user.email
#         content['creator_avatar'] = user.userImage
#     path = f"partnerTemplates/template{name}.html"
#     if name == '2':
#         try:
#             products = Product_buy.objects.filter(id_creator=request.user)
#             content['products'] = [{'id': product.id,
#                                     'product_name': product.product_name,
#                                     'customer': product.id_user_buy,
#                                     'st':product.status,
#                                     'status1': 'red' if product.status[-1] == 'е' else 'blue',
#                                     'status2': 'red' if product.status[-1] == 'о' else 'blue',
#                                     'status3': 'red' if product.status[-1] == 'ы' else 'blue',
#                                     'chat_id':(creator.id * Partner.objects.get(email=product.id_user_buy).id) + creator.id + Partner.objects.get(email=product.id_user_buy).id

#                                     }
#                                    for product in products]
#             products_v = Product_buy.objects.filter(id_creator=request.user)
#             if products_v.count() > 0:
#                 content['products_v'] = [{'id': product.id,
#                                        'product_name': product.product_name,
#                                        'customer': product.id_user_buy,
#                                        'status': product.status,
#                                        'id_user_buy': product.id_user_buy,
#                                        'chat_id':(creator.id * Partner.objects.get(email=product.id_user_buy).id) + creator.id + Partner.objects.get(email=product.id_user_buy).id
#                                       }
#                                      for product in products_v]
            
        
#         except Product_buy.DoesNotExist as e:
#             content['products'] = None

#     # elif name == '3':
#         # form = MyProfile(request.POST)
#         # content['form1'] = form

#     elif name == '3':
#         account = Partner.objects.get(email=request.user)
#         products = Product_creator.objects.filter(id_creator=account.email)
#         content['products'] = [{'product_name': product.product_name,
#                                 'cost': product.price,
#                                 'id': product.product_id,
#                                 }
#                                for product in products]

#     elif name == '4':
#         try:
#             creator = Creator.objects.get(email=request.user)
#             content['creator'] = creator
#         except:
#             creator = Creator()
#             content['creator'] = creator

#     elif name == '1':
#         try:
#             partner = Partner.objects.get(email=request.user)
#             content['partner'] = partner
#         except:
#             partner = Partner()
#             content['partner'] = partner
    
#     elif name == '6':
#         form = ProductCreateForm()
#         content['form8'] = form

#     return render(request, path, content)


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
                            'picture': product.picture,
                            'description': product.description
                            }
                           for product in products]

    return render(request, 'index.html', context)

def cardResume_page(request):
    context = gen_menu(request)
    profile = Shop.objects.get(email=request.user)
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

    profile = Shop.objects.get(username=username)
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

    context = gen_menu(request)
    product = Product_creator.objects.get(id=product_id)
    try:
        if request.method == "POST" and "buy_product" in request.POST:
            product_buy = Product_buy()

            product_buy.price = product.price
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
        context['products'].set = list(filter(None,product.set.strip().split(",")))

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
            print(request.FILES)
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
    form = SignUpForm(request.POST)
    context = {
        'form': form
    }
    # вход
    if request.method == 'POST' and 'btnform2' in request.POST:
        print(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            print('Try again! username or password is incorrect')
    # регистрация
    elif request.method == 'POST' and 'btnform1' in request.POST:
        send_mail(
            'Test',
            'Всё робит)',
            'korotikhin84@mail.ru',
            ['gaamer557@gmail.com'],
            fail_silently=False,
        )
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
    print(user.id)
    print(companion_id)
    companion = Shop.objects.get(id=companion_id)
    content['room_id'] = room_id
    content['companion'] = companion
    if not Chat_room.objects.filter(name=room_id).exists():
        new_room = Chat_room.objects.create(name=room_id)
        new_room.save()
    return render(request, 'messanger.html', content)


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
    content['products'] = [{
        'id': product.id,
        'id_creator': product.id_creator,
        'id_user_buy': product.id_user_buy,
        'product_name': product.product_name,
        'task_id': product.task_id,
        'status': product.status,
        'message': product.message,
        'payed_partner': product.payed_partner,
        'payed_user': product.payed_user,
        'status_pay': product.status_pay,
        'delivery_address': product.delivery_address,
        'date_add': product.date_add,
        'img': product.img,

        
    } for product in products]
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

    user = Account.objects.get(email=request.user)
    print(user)

    shops = Shop.objects.all()

    flag = False

    if request.method == "POST":

        

        for shop in shops:
            if shop.email == request.user.email:
                flag = True

        try:
            if flag == False:
                shop = Shop()
                shop.phone = request.POST['phonenumber']
                shop.email = request.user.email
                shop.save()
                Account.objects.filter(email=request.user).update(is_partner=True)

        except:
            print("in request.")

    return render(request, 'showPartner.html')
