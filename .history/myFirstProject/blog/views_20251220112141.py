from django.shortcuts import render
fr

# Create your views here.
def home(request):
    return HttpResponse("Hello welcome to web page")