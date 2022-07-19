from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from account.models import Account


def login_page(request):
    content = {
    }

def index_page(request):
    context = {}
    return render(request, 'index.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")

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
    path = f"template{name}.html"
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


