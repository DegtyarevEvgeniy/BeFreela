from django.contrib import admin
from django.urls import path
from Part import views
from account import views as partnerViews
from account.views import SignUpView
from django.conf.urls import include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', views.logout_view),
    path('login/', views.login_page),
    path('signin/', SignUpView.as_view(), name='signin'),
    path('', views.index_page),
    path('partnerTemplates/<name>/', views.partnerTemplate_page),
    path('accounts/', include('django.contrib.auth.urls')),


]