from . import views
from django.urls import path

urlpatterns = [
    path('admin/', ),
    path('', include('blog.urls'))
   
]