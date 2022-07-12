from django.contrib import admin
from django.urls import path
from Part import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.becomeCreator_page),
    path('becomeCreatorTemplates/<name>/', views.becomeCreatorTemplate_page),
    

]