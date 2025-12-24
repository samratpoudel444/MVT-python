from django.urls import path,re_path
from . import views

urlpatterns = [
    path('test/<int:id>/', views.home, name= "test0"),
     path('/test1', views.about, name="test1"),
     re_path(r'^article/(?P<year>[0-9]{4})/$', views.year, name="year")
]