from django.shortcuts import render

# Create your views here.
from RPGGAME.forms import PersForm

from RPGGAME.models import Pers


def menu_gen():
    return [
        {'link':'/',            'title':'Начало'},
        {'link':'/choose',      'title':'Выбор'},
        {'link':'/inventar',    'title':'Вещи'},
        {'link': 'http://www.ya.ru', 'title': 'гуглить'},
    ]

def index(request):
    pers = PersForm(request.POST)
    if pers.is_valid():
        pers_data=pers.data

        if (pers_data['name'],) in Pers.objects.values_list('name'):

            pers_data = Pers.objects.get(name=pers_data['name'])
        else:
            item = Pers(name=pers_data['name'],
                        desc=pers_data['desc'],
                        age=pers_data['age'])
            item.save()
    else:
        pers_data={'name':'Никто',
                   'desc':'мимо прохожий на нас не похожий',
                   'age':'недостаточно'}
    data = {
        'users':Pers.objects.all(),
        'pers':pers_data,
        'menu':menu_gen(),
    }
    return render(request,'index.html',data)

def choose(request):
    form = PersForm()
    data = {
        'form': form,
        'menu': menu_gen(),
    }
    return render(request,'choose.html',data)

def inventar(request):
    data = {
        'menu': menu_gen(),
    }
    return render(request,'inventar.html',data)