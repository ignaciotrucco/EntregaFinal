from django.urls import path

from . import views

app_name = "Libros"

urlpatterns = [
    path('libros/', views.LibroListView.as_view(), name='libros'),
    path("libros/detalle/<int:pk>/", views.LibroDetailView.as_view(), name="libro_detail"),
]