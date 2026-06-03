from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
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

from django.contrib import messages

class RegistroView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('producto-lista')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, f'¡Bienvenido {user.username}! Tu cuenta fue creada exitosamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Por favor corregí los errores del formulario.')
        return super().form_invalid(form)