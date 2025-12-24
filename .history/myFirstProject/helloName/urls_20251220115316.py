from . import views
from django.urls import path

urlpatterns = [
    path('helloname/<int:id>}/', views.helloName ),
    path('/hellonameQuery', views.helloNameQuery))
   
]