from django.contrib import admin
from .models import ToDoList, Item

# Register your models here.

# Add the ToDoList table to "Django administration".
admin.site.register(ToDoList)
admin.site.register(Item)