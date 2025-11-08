from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="homepage"),
    path("about/", views.about, name="about"),
    path("roti/", views.roti, name="roti"),
    path("coconut/", views.coconut, name="coconut"),
    path("biryani/", views.biryani, name="biryani"),
    path("fruits/", views.fruits, name="fruits"),
    
]
