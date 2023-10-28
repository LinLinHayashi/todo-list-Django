from django.db import models
from django.contrib.auth.models import User


# A model used to define the structure of an SQL database table, inheriting from "models.Model".
# Here ToDoList is an SQL database table and a Python class at the same time. 
class ToDoList(models.Model):

    User = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)

    # A character field with a maximum length of 200 character.
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text

# After models are created, run "python manage.py makemigrations" and "python manage.py migrate" in the shell to update the database structure. Run these each time we change the database structure.


# Run "python .\manage.py shell" in the shell to go into the Python shell. 

# Run
# "
# from main.models import Item, ToDoList
# t = ToDoList(name="Tim\'s List")
# t.save()
# "
# in the Python shell to create and save an object of ToDoList.

# Run "ToDoList.objects.all()" to show all objects of ToDoList.
# Run "ToDoList.objects.get(id=1)" to show the first object/record of ToDoList.
# Run "ToDoList.objects.get(name="Tim\'s List")" to show objects with their "name" attribute equal to "Tim\'s List".

# Run "t.item_set.create(text="Go to the mall", complete=False)" to create an object of Item, since the Item table uses the ToDoList table as a foreign key.

# Now run "t.item_set.all()", we can see the Item objects relating to the ToDoList object "t".
# Run "t.item_set.get()" function with parameters to show the Item objects we want.

# Run
# "
# from main.models import Item, ToDoList
# t = ToDoList.objects
# t.all()
# t.filter(name__startswith="Tim")
# "
# to make a query to the ToDoList table.

# Run
# "
# del_object = t.get(id=1)
# del_object.delete()
# "
# to delete the ToDoList object and its cascaded Item object.

# Run "python manage.py createsuperuser" to create a user for "Django administration".
