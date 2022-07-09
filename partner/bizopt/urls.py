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
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

from account.views import SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', views.logout_view),
    path('signin/', SignUpView.as_view(), name='signin'),
    path('login/', views.login_page),
    path('restorePassword/', views.forgot_password_page),
    path('', views.partners_page),
    path('becomeCreator/', views.becomeCreator_page),
    path('becomeCreator/becomeCreatorTemplates/<name>/', views.becomeCreatorTemplate_page),

    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]
