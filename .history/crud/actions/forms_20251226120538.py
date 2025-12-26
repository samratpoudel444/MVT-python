from django import form
from .models import user

class userForm(orm(forms.ModelForm):
    
    class Meta:        fields = ("",)
)