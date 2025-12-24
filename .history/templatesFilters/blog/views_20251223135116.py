from django.shortcuts import render

# Create your views here.
def blog_details(request):
    post={
        "title":"My second Template"
    }
    return render(request, "blog/home.html", {"post":post})