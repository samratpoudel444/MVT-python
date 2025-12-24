from django.shortcuts import render

# Create your views here.
def blog_details(request):
    post={
        "title":"My second Template",
        "description":"dasdfh zhjls f fihsdfds  gdkg d",
        author"":None,
        "created_at"
    }
    return render(request, "blog/home.html", {"post":post})