from django.urls import path

urlpatterns = [
    path('', include('blog.urls')),
     path('', include('helloName.urls'))
]