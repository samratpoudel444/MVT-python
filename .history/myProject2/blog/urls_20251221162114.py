from django.urls import path
from . import views

urlpatterns = [
    path('shop/', include('shops.urls')),
    path('blog', include('blog.urls'))
]