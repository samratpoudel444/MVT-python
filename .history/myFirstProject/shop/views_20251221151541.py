from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request, id):
    return HttpResponse(f"The name is samrat and id is ${id}")

def about(request, id):
    name= request.GET.get("name")
    return HttpResponse(f"The name is ${name}")

def year(request, year):
    return HttpResponse(f"the year is {year}")

def year(request, year):
    return HttpResponse(f"the year is {year}")