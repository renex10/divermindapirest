from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLES = [
        ('padre', 'Padre'),
        ('educador', 'Educador'),
        ('terapeuta', 'Terapeuta')
    ]
    telefono = models.CharField(max_length=20, blank=True)
    rol = models.CharField(max_length=10, choices=ROLES, default='padre')
    estado = models.CharField(
        max_length=10,
        choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')],
        default='activo'
    )

    def __str__(self):
        return self.email  # ✅ Correcto si prefieres mostrar el email en lugar del username

    # Añade esto para evitar advertencias de Django
    class Meta:
        swappable = 'AUTH_USER_MODEL'  # Indica que este es el modelo de usuario personalizado