from django.urls import path

from . import views

app_name = "Libros"

urlpatterns = [
    path('libros/', views.LibroListView.as_view(), name='libros'),
    path("libros/detalle/<int:pk>/", views.LibroDetailView.as_view(), name="libro_detail"),
    path("libros/crear/", views.LibroCreateView.as_view(), name="libro_create"),
    path("libros/editar/<int:pk>/", views.LibroUpdateView.as_view(), name="libro_update"),
    path("libros/borrar/<int:pk>/", views.LibroDeleteView.as_view(), name="libro_delete"),
]