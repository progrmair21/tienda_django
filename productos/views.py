from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import Producto
from django.contrib import messages

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
    from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from django.contrib.auth.models import User

@method_decorator(login_required, name='dispatch')
class PerfilView(UpdateView):
    model = User
    fields = ['username', 'email', 'first_name', 'last_name']
    template_name = 'registration/perfil.html'
    success_url = reverse_lazy('producto-lista')

    def get_object(self):
        return self.request.user