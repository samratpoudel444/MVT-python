from django.urls import path
from . import views

urlpatterns = [
    path('test/<int:id>/', views.home, name= "test0"),
     path('/test', views.about, name="test1")
]