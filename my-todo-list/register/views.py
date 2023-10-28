from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, authenticate

# Create your views here.

def register(request):
  if request.method == "POST":
    form = RegisterForm(request.POST)
    if form.is_valid():

      # Save the new user into the user database. This is a built-in method of Django.
      form.save()

    return redirect("/")
  else:
    form = RegisterForm()
  return render(request, "register/register.html", {"form":form})
