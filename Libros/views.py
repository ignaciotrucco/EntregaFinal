from django.shortcuts import render
from .models import Libro
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
class LibroListView(ListView):
    model = Libro
    template_name = 'Libros/libros.html'
    context_object_name = 'libros'