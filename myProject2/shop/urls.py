from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.product_list, name="home"),
]