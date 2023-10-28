from django.urls import path
from . import views

urlpatterns = [

    # If no path is given, then go to the "views.py" file and run the index() function.
    # If a string is given, then take this string as the "name" parameter passed to the function "views.index".
    # path("<str:name>", views.index1, name="index1"),

    path("v1/", views.v1, name="v1"),
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("view/", views.view, name="view")
]
