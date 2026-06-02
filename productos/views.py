from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Producto

class ProductoListView(ListView):
    model = Producto
    template_name = 'productos/lista.html'

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'productos/detalle.html'

class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    fields = ['nombre', 'descripcion', 'precio', 'stock']
    template_name = 'productos/formulario.html'
    success_url = reverse_lazy('producto-lista')

class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = Producto
    fields = ['nombre', 'descripcion', 'precio', 'stock']
    template_name = 'productos/formulario.html'
    success_url = reverse_lazy('producto-lista')

class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = 'productos/confirmar_eliminar.html'
    success_url = reverse_lazy('producto-lista')