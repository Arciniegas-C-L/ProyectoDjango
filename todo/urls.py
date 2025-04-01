from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('agregar/', views.agregar, name='agregar'),
    path('eliminar/<int:tarea_id>', views.eliminar, name='eliminar'),
    path('agregar/<int:tarea_id>', views.editar, name='editar'),
]