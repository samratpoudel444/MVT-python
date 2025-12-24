from django.shortcuts import render
from datetime import datetime
# Create your views here.
def blog_details(request):
    post={
        "title":"My second Template",
        "description":"dasdfh zhjls f fihsdfds  gdkg d",
        "author":"ssdhdhhd ddds ss",
        "created_at":datetime(2025,1,19,10,30),
        "comment_count":5,
        "tags":["Django","python","web Deve"],
        "price":100
    }
    return render(request, "blog/home.html", {"post":post})