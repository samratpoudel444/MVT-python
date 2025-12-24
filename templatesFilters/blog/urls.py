from django.urls import path
from . import views
urlpatterns=[
    path('home/', views.blog_details , name="test")
]