from django.shortcuts import render
def index_page(request):
    content = {}
    return render(request, 'index.html', content)

def signin_page(request):
    content = {}
    return render(request, 'signin.html', content)
# Create your views here.
