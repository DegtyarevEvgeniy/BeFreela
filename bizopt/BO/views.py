from django.shortcuts import render
def index_page(request):
    content = {}
    return render(request, 'index.html', content)

def signin_page(request):
    content = {}
    return render(request, 'signin.html', content)

def login_page(request):
    content = {}
    return render(request, 'login.html', content)
# Create your views here.
