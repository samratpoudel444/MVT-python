from . import views 
from django.urls import path
urlpatterns=[
    path('admin/', views.home, name="home")
     path('about', about, name="about")
]