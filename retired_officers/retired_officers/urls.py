from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.shortcuts import render

# import views directly from the app
from myapp.views import index, register

def handler404(request, exception):
    if request.user.is_authenticated:
        print('True')
        return render(request, '404.html')
    else:
        print('Fail')
        return render(request, '1404.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index.index,name="index"),
    path('register/', register.register, name='register'),
] 

handler404 = handler404
