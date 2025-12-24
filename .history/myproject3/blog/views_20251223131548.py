from django.shortcuts import render
from datetime import datetime
# Create your views here.

class User:
    def __init__(self,name, age):
        self.name= name
        self.age= age
    
    def home(request):
        context={
            "name":"Samrat poudel",
            "age":22,
            "skills":["python", "javascript"],
            "user": User("Kumar", 30),
            "blog":{
                "title":"Django Template intro"
            }
        }