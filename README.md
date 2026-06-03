# Tienda Django

Aplicación web de gestión de productos desarrollada con Django.
Permite realizar operaciones CRUD con autenticación de usuarios.

## Requisitos
- Python 3.x
- pip

## Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/progrmair21/tienda_django.git
cd tienda_django
```

### 2. Crear y activar el entorno virtual
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones
```bash
python manage.py migrate
```

### 5. Crear superusuario
```bash
python manage.py createsuperuser
```

### 6. Correr el servidor
```bash
python manage.py runserver
```

## Credenciales de prueba
- **Usuario:** admin
- **Contraseña:** admin1234

## URLs principales
- `/productos/` → Lista de productos
- `/productos/crear/` → Crear producto (requiere login)
- `/admin/` → Panel de administración
- `/login/` → Iniciar sesión
- `/logout/` → Cerrar sesión