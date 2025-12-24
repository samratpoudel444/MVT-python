from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def helloName(request, id):
    return HttpResponse(f"hello you are same right! and your age is {id}")

def helloNameQuery(request):
    name= request.GET.get("name")
    age= request.GET.get("age")
    return HttpResponse(f"hello you are {name} right! and your age is {age}")