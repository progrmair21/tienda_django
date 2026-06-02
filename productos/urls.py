from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductoListView.as_view(), name='producto-lista'),
    path('<int:pk>/', views.ProductoDetailView.as_view(), name='producto-detalle'),
    path('crear/', views.ProductoCreateView.as_view(), name='producto-crear'),
    path('<int:pk>/editar/', views.ProductoUpdateView.as_view(), name='producto-editar'),
    path('<int:pk>/eliminar/', views.ProductoDeleteView.as_view(), name='producto-eliminar'),
]