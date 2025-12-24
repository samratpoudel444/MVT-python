from django.shortcuts import render
from datetime import datetime
# Create your views here.
def blog_details(request):
    post={
        "title":"My second Template",
        "description":"dasdfh zhjls f fihsdfds  gdkg d",
        "author":None,
        "created_at":datetime
    }
    return render(request, "blog/home.html", {"post":post})