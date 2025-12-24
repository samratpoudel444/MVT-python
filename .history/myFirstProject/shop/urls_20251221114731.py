from django.urls import path
from . import views

urlpatterns = [
    path('', include('blog.urls')),
     path('', include('helloName.urls'))
]