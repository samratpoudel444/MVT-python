from django.urls import path
from . import views

urlpatterns = [
    path('', include('view.urls')),
     path('', include('helloName.urls'))
]