"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import users.views
import books.views

urlpatterns = [
    path('admin/', admin.site.urls),  # django默认包含的
    path('users/index/', users.views.index),
    path('books/to_add/', books.views.to_add),
    path('books/add/', books.views.add),
    path('books/get/', books.views.get),

    # url: weather/beijing/2018
    path('weather/<city>/<year>', users.views.weather),

    # url: weather/?city=beijing&year=2018&year=2019
    path('weather/', users.views.weather2),
]
