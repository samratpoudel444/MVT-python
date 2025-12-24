from django.urls import path
from . im

urlpatterns = [
    path('', include('blog.urls')),
     path('', include('helloName.urls'))
]