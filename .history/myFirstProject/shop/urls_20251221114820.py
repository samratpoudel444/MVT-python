from django.urls import path
from . import views

urlpatterns = [
    path('', vie.home),
     path('', include('helloName.urls'))
]