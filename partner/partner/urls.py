from django.contrib import admin
from django.urls import path
from Part import views
from partners import views as partnerViews
from partners.views import SignUpView
from django.conf.urls import include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', views.logout_view),
    path('login/', views.login_page),
    path('signin/', SignUpView.as_view(), name='signin'),
    path('', views.index_page),
    path('partnerTemplates/<name>/', views.partnerTemplate_page),
    path('accounts/', include('django.contrib.auth.urls')),
    path('start/', views.start_page),
]


handler404 = views.pageNotFound
handler403 = views.pageMistakeServ
handler400 = views.pageNotAccess
# handler500 = views.pageNotRequest