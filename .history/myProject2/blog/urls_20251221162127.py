from django.urls import path
from . import views

urlpatterns = [
    path('home/', view),
    path('blog', include('blog.urls'))
]