from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("Hello welcome to web page")