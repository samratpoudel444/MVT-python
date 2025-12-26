from django.shortcuts import render
from django.http import HttpResponse
from .forms import user

def create_User(request):
    return HttpResponse("k xa")