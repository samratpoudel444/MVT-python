from django.urls import path
from . import views

urlpatterns = [
    path('/<int:id>', views.home, name= "test0"),
     path('', views.about, name="test1")
]