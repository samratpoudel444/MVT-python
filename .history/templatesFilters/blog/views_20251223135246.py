from django.shortcuts import render
from datetime import datetime
# Create your views here.
def blog_details(request):
    post={
        "title":"My second Template",
        "description":"dasdfh zhjls f fihsdfds  gdkg d",
        "author":None,
        "created_at":datetime(2025,1,19,10,30),
        
    }
    return render(request, "blog/home.html", {"post":post})