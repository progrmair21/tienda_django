from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Producto

class ProductoTests(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='test', 
            password='test1234'
        )
        self.producto = Producto.objects.create(
            nombre='Producto Test',
            descripcion='Descripción test',
            precio=100.00,
            stock=10
        )
    
    def test_lista_productos(self):
        response = self.client.get('/productos/')
        self.assertEqual(response.status_code, 200)
    
    def test_crear_producto_sin_login(self):
        response = self.client.get('/productos/crear/')
        self.assertEqual(response.status_code, 302)
    
    def test_crear_producto_con_login(self):
        self.client.login(username='test', password='test1234')
        response = self.client.get('/productos/crear/')
        self.assertEqual(response.status_code, 200)

    def test_detalle_producto(self):
        response = self.client.get(f'/productos/{self.producto.pk}/')
        self.assertEqual(response.status_code, 200)