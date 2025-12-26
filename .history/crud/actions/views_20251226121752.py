from django.shortcuts import render, redirect
from .forms import userForm

def create_User(request):
    if request.method == "POST":
        form = userForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("test")   # or any url name
    else:
        form = userForm()   # ← THIS LINE FIXES IT

    return render(request, "insert.html", {"form": form})
