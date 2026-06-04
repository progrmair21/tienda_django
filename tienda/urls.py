from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from productos.views import RegistroView
from productos.views import RegistroView, PerfilView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', include('productos.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('registro/', RegistroView.as_view(), name='registro'),
    path('logout/', LogoutView.as_view(next_page='/productos/'), name='logout'),
    path('perfil/', PerfilView.as_view(), name='perfil'),
]