"""bizopt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as authViews
from BO import views
from BO.views import RegisterUser, LoginUser


urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', authViews.LogoutView.as_view(), name='logout'),
    path('', views.index_page),
    path('tasks/', views.tasks_page),
    # path('employers/', views.employers_page),
    path('creators/', views.creators_page),
    path('signin/', RegisterUser.as_view(), name='signin'),
    path('login/', LoginUser.as_view(), name='login'),
]
