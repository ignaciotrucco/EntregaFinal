from django.shortcuts import render
from .models import Libro
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
class LibroListView(ListView):
    model = Libro
    template_name = 'Libros/libros.html'
    context_object_name = 'libros'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get('busqueda', None)
        if busqueda:
            queryset = queryset.filter(titulo__icontains=busqueda)
        return queryset

class LibroDetailView(DetailView):
    model = Libro