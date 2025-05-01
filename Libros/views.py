from django.shortcuts import render
from .models import Libro
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import LibroForm
from django.contrib.auth.mixins import LoginRequiredMixin

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

class LibroCreateView(LoginRequiredMixin, CreateView):
    model = Libro
    form_class = LibroForm
    success_url = reverse_lazy('Libros:libros')

class LibroUpdateView(LoginRequiredMixin, UpdateView):
    model = Libro
    form_class = LibroForm
    success_url = reverse_lazy('Libros:libros')

class LibroDeleteView(LoginRequiredMixin, DeleteView):
    model = Libro
    success_url = reverse_lazy('Libros:libros')