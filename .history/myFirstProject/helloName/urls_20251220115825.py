from . import views
from django.urls import path

urlpatterns = [
    path('helloname/<int:id>}/', views.helloName ),
    path('/hellonameQuery', views.helloNameQuery),
   
]
from django.urls import path
from . import views

urlpatterns = [
    path('helloname/<int:id>/', views.helloName),
    path('hellonameQuery/', views.helloNameQuery),
]
