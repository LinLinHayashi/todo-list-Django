from django import forms


# Since the "CreateNewList" class inherits "forms.Form", any "CreateNewList" object will check if its attributes and values are valid with "is_valid()" method, and return true if things are valid.
class CreateNewList(forms.Form):
  name = forms.CharField(label="Name", max_length=200)
  check = forms.BooleanField(required=False)