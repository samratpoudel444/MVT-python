from django.db import models

# Create your models here.
class person(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    email= models.EmailField(max_length=254)
    address= models.CharField(max_length=50)

    def __str__(self):
        return super().__str__()