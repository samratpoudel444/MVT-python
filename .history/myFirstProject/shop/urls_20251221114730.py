from django.urls import path
from . import view

urlpatterns = [
    path('', include('blog.urls')),
     path('', include('helloName.urls'))
]