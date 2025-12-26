from django import forms
from .models import person

class userForm(forms.ModelForm):
    class Meta:
        model= user
        fields= "__all__"
