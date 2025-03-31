from django.urls import path, include
from django.contrib import admin
from . import views
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agregar/', views.agregar, name='agregar'),
    path("", views.home, name="home"),
] 