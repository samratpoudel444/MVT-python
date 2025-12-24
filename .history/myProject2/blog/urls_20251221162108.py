from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shops.urls')),
    path('blog', include('blog.urls'))
]