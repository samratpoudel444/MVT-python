from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def helloName(request, name):
    return HttpResponse(f"hello you are {name} right!")

def helloNameQuery(request, name, age):
    name= request.Get.get("name")
    age= request.Get.get()
