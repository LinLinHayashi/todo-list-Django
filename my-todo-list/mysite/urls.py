"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from register import views as v

urlpatterns = [
    path("admin/", admin.site.urls),

    # If no path is given, then go to the "main/urls.py" file.
    path("", include("main.urls")),

    path("register/", v.register, name="register"),

    # Go to the "django.contrib.auth.urls" file. However, This file actually doesn't exist, it will go to the "registration/login" file, which is a HTML file. Here, we don't need to call a function in the views to render it.
    path("", include("django.contrib.auth.urls"))
]
