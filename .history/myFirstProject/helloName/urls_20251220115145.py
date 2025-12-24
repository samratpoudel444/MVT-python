from . import views
from django.urls import path

urlpatterns = [
    path('/', ),
    path('', include('blog.urls'))
   
]