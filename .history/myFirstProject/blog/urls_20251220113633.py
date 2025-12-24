from . import views 

urlpatterns=[
    path('admin/', views.home, name="home")
     path('about', about, name="about")
]