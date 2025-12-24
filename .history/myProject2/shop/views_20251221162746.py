from django.shortcuts import render

# Create your views here.
def product_list(request):
    return render(request, "trmplatesshop/product_list.html")