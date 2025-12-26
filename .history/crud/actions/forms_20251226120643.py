from django import form
from .models import user

class userForm(form.ModelForm):
    class Meta:
        model= user
        field= ""