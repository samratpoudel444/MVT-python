from django.urls import path
from . import views

urlpatterns = [
    path('', include('views.urls')),
     path('', include('helloName.urls'))
]