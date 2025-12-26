from django import forms
from .models import user

class userForm(form.ModelForm):
    class Meta:
        model= user
        field= "__all__"
