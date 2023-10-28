from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList
from .forms import CreateNewList

# Create your views here.

'''
def index(request, name):
    ls = ToDoList.objects.get(name=name)
    item = ls.item_set.get(id=1)
    return HttpResponse("<h1>%s</h1><br><br><p>%s</p>" %(ls.name, item.text))
'''

def v1(request):
    return HttpResponse("<h1>View 1!</h1>")


def index(request, id):
    ls = ToDoList.objects.get(id=id)

    if ls in request.user.todolist.all():

        # If the user submits data on the rendered HTML page, i.e., a button whose type is "submit" is clicked.
        if request.method == "POST":

            # If the button whose name is "save" is clicked.
            if request.POST.get("save"):

                for item in ls.item_set.all():
                    if request.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()

            # If the button whose name is "newItem" is clicked.
            elif request.POST.get("newItem"):

                # Store into "txt" what's input to the <input> element whose name is "new".
                txt = request.POST.get("new")

                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("invalid")

        return render(request, "main/list.html", {"ls": ls})
    return render(request, "main/list.html", {})


def home(request):
    return render(request, "main/home.html", {})


def create(request):

    # If the user submits data on the rendered HTML page.
    if request.method == "POST":

        # This will create a "CreateNewList" object that stores the data submitted, which is also a "forms.Form" object.
        form = CreateNewList(request.POST)

        if form.is_valid():

            # "cleaned_data" is an attribute of a "forms.Form" object, used to store validated data.
            n = form.cleaned_data["name"]

            t = ToDoList(name=n)
            t.save()

            # Connect the ToDoList object t with the current user.
            request.user.todolist.add(t)

        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()
    return render(request, "main/create.html", {"form":form})

def view(request):
    if request.method == "POST":
        deleteStr = request.POST.get("delete")
        deleteInt = int(deleteStr)
        delete = ToDoList.objects.get(id=deleteInt)
        delete.delete()
    return render(request, "main/view.html", {})
