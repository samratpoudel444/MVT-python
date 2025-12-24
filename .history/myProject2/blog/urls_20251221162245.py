from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.post_list, name="home_list              "),
]