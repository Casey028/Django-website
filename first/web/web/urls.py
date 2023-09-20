from django.contrib import admin
from django.urls import path,include
from index import views
from django.views.generic import TemplateView, ListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="Index"),
    path('register',views.sign_up,name="Register"),
    path('home',views.sr,name="Home"),
    path('logout',views.log_out,name='Logout'),
    path('all',views.all,name='all'),
    path('intro',views.intro,name='intro')
]
