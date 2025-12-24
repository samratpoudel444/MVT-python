from django.urls import path
from . import views

urlpatterns = [
    path('home/', include('shops.urls')),
    path('blog', include('blog.urls'))
]