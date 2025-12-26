from django.db import models

# Create your models here.
class person(models.Model):
    name=models.CharField(_(""), max_length=50)
    age=models.