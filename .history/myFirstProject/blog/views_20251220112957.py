from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello welcome to web page")

def about(request):
    a=20
    return HttpResponse("This is about page and count is, a)