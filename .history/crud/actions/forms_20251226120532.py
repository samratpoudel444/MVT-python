from django import form
from .models import user

class userForm(Form(forms.ModelForm):
    
    class Meta:
        fields = ("",)
)