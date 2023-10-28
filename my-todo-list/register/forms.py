from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):

  # This attribute/field is not in "UserCreationForm", we add it additionally.
  email = forms.EmailField()

  class Meta:

    # This specifies the model, i.e., the database table, that this form class is associated with, which is the built-in Django "User" model.
    model = User

    # This specifies the fields to include in this form class.
    fields = ["username", "email", "password1", "password2"]