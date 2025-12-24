from . import views
from django.urls import path

urlpatterns = [
    path('helloname/', ),
    path('', include('blog.urls'))
   
]