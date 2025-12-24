from . import views
from django.urls import path

urlpatterns = [
    path('helloname/<int:id>}/', ),
    path('', include('blog.urls'))
   
]