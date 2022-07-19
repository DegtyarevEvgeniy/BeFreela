from django.contrib import admin
from django.urls import path
from Part import views
from account import views as partnerViews
from account.views import SignUpView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page),
    path('becomeCreatorTemplates/<name>/', views.becomeCreatorTemplate_page),
    path('signin/', SignUpView.as_view(), name='signin'),


]