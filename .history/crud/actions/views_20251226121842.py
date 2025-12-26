from django.shortcuts import render, redirect
from .forms import userForm

def create_User(request):
    if request.method == "POST":
        form = userForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("test") 
    else:
        form = userForm()   

    return render(request, "insert.html", {"form": form})
