from django.shortcuts import render
from django.http import HttpResponse
from .forms import userForm

def create_User(request):
    if request.method =="POST":
        form= userForm(request.POST)
        if form.isValid():
            form.save()
            return HttpResponse("")