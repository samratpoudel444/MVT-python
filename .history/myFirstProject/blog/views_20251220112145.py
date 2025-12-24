from django.shortcuts import render
from django

# Create your views here.
def home(request):
    return HttpResponse("Hello welcome to web page")