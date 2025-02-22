# core/models.py
from django.db import models
from users.models import CustomUser
from geografia.models import Comuna

class PerfilPersonal(models.Model):
    rut = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    lugar_nacimiento = models.CharField(max_length=100, blank=True)
    foto_perfil = models.ImageField(upload_to='perfiles/', null=True, blank=True)
    genero = models.CharField(max_length=10, blank=True)
    nacionalidad = models.CharField(max_length=50, blank=True)
    lengua_materna = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.nombre

class Direccion(models.Model):
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=20, blank=True)
    comuna = models.ForeignKey(Comuna, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"{self.calle} {self.numero}, {self.comuna}"

class Nino(models.Model):
    id_perfil = models.OneToOneField(PerfilPersonal, on_delete=models.CASCADE, related_name='nino')
    necesidades_especiales = models.TextField(blank=True)
    familias = models.ManyToManyField('Familia', through='NinoFamilia')
    direccion = models.ForeignKey(Direccion, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.id_perfil.nombre

class Familia(models.Model):
    nombre_familia = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    miembros = models.ManyToManyField(CustomUser, related_name='familias')
    foto_perfil = models.ImageField(upload_to='familias/', null=True, blank=True)

    def __str__(self):
        return self.nombre_familia

class NinoFamilia(models.Model):
    nino = models.ForeignKey(Nino, on_delete=models.CASCADE)
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE)
    fecha_inicio = models.DateField(auto_now_add=True)
    fecha_fin = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.nino} - {self.familia}"

class Autismo(models.Model):
    NIVELES = [('leve', 'Leve'), ('moderado', 'Moderado'), ('severo', 'Severo')]
    nivel = models.CharField(max_length=10, choices=NIVELES)
    descripcion = models.TextField(blank=True)
    nino = models.OneToOneField(Nino, on_delete=models.CASCADE, related_name='autismo')

    def __str__(self):
        return f"Autismo ({self.nivel}) - {self.nino}"

# Nuevos modelos para el formulario completo
class HitoDesarrollo(models.Model):
    hito = models.CharField(max_length=100)
    edad_alcanzada = models.IntegerField(null=True, blank=True)
    regresion = models.BooleanField(default=False)
    descripcion = models.TextField(blank=True)
    nino = models.ForeignKey(Nino, on_delete=models.CASCADE, related_name='hitos_desarrollo')

    def __str__(self):
        return f"{self.hito} - {self.nino}"

class ControlEsfinteres(models.Model):
    usa_panales_diurno = models.BooleanField(default=False)
    usa_panales_nocturno = models.BooleanField(default=False)
    frecuencia_accidentes = models.CharField(max_length=50, blank=True)
    senales_bano = models.TextField(blank=True)
    miedo_inodoro = models.BooleanField(default=False)
    estrategias = models.TextField(blank=True)
    nino = models.ForeignKey(Nino, on_delete=models.CASCADE, related_name='control_esfinteres')

    def __str__(self):
        return f"Control Esfínteres - {self.nino}"

class Alimentacion(models.Model):
    preferencias = models.TextField(blank=True)
    aversiones = models.TextField(blank=True)
    problemas_masticacion = models.BooleanField(default=False)
    problemas_atragantamiento = models.BooleanField(default=False)
    nino = models.ForeignKey(Nino, on_delete=models.CASCADE, related_name='alimentacion')

    def __str__(self):
        return f"Alimentación - {self.nino}"

class Sueno(models.Model):
    horas_sueno_noche = models.IntegerField(null=True, blank=True)
    siestas_diurnas = models.BooleanField(default=False)
    dificultad_dormir = models.BooleanField(default=False)
    despertares_nocturnos = models.BooleanField(default=False)
    rutinas_previas = models.TextField(blank=True)
    duerme_solo = models.BooleanField(default=False)
    nino = models.ForeignKey(Nino, on_delete=models.CASCADE, related_name='sueno')

    def __str__(self):
        return f"Sueño - {self.nino}"

class SensibilidadSensorial(models.Model):
    TIPOS = [
        ('auditiva', 'Auditiva'),
        ('visual', 'Visual'),
        ('táctil', 'Táctil'),
        ('olfativa/gustativa', 'Olfativa/Gustativa')
    ]
    tipo = models.CharField(max_length=20, choices=TIPOS)
    descripcion = models.TextField(blank=True)
    nino = models.ForeignKey(Nino, on_delete=models.CASCADE, related_name='sensibilidades_sensoriales')

    def __str__(self):
        return f"Sensibilidad {self.tipo} - {self.nino}"

class ActividadExtracurricular(models.Model):
    TIPOS = [
        ('terapia', 'Terapia'),
        ('deporte', 'Deporte'),
        ('arte', 'Arte'),
        ('taller', 'Taller')
    ]
    tipo = models.CharField(max_length=10, choices=TIPOS)
    descripcion = models.TextField()
    frecuencia = models.CharField(max_length=50, blank=True)
    nino = models.ForeignKey(Nino, on_delete=models.CASCADE, related_name='actividades_extracurriculares')

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.nino}"

class Autorizacion(models.Model):
    consentimiento_informado = models.BooleanField(default=False)
    contacto_escuela = models.BooleanField(default=False)
    proteccion_datos = models.BooleanField(default=False)
    nino = models.OneToOneField(Nino, on_delete=models.CASCADE, related_name='autorizacion')

    def __str__(self):
        return f"Autorizaciones - {self.nino}"

# Modelos restantes manteniendo la estructura original
class Diagnostico(models.Model):
    descripcion = models.TextField()
    fecha_diagnostico = models.DateField()
    nino = models.ForeignKey(Nino, on_delete=models.CASCADE, related_name='diagnosticos')

    def __str__(self):
        return f"Diagnóstico - {self.nino}"

class ObservacionEscuela(models.Model):
    ESTADOS = [('pendiente', 'Pendiente'), ('revisado', 'Revisado'), ('rechazado', 'Rechazado')]
    fecha = models.DateField(auto_now_add=True)
    comportamiento = models.TextField(blank=True)
    nino = models.ForeignKey(Nino, on_delete=models.CASCADE, related_name='observaciones_escuela')
    profesor = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='pendiente')

    def __str__(self):
        return f"Observación Escuela - {self.nino}"

class ObservacionFamilia(models.Model):
    fecha = models.DateField(auto_now_add=True)
    rutinas = models.TextField(blank=True)
    nino = models.ForeignKey(Nino, on_delete=models.CASCADE, related_name='observaciones_familia')
    usuario = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    estado = models.CharField(max_length=10, choices=ObservacionEscuela.ESTADOS, default='pendiente')

    def __str__(self):
        return f"Observación Familia - {self.nino}"

class DetonanteCrisis(models.Model):
    descripcion = models.TextField()
    nino = models.ForeignKey(Nino, on_delete=models.CASCADE, related_name='detonantes_crisis')

    def __str__(self):
        return f"Detonante Crisis - {self.nino}"

class Debilidad(models.Model):
    CATEGORIAS = [('sensorial', 'Sensorial'), ('comunicacion', 'Comunicación'), ('emocional', 'Emocional'), ('otros', 'Otros')]
    NIVELES = [('leve', 'Leve'), ('moderado', 'Moderado'), ('severo', 'Severo')]
    descripcion = models.TextField()
    categoria = models.CharField(max_length=15, choices=CATEGORIAS)
    nivel = models.CharField(max_length=10, choices=NIVELES)
    nino = models.ForeignKey(Nino, on_delete=models.CASCADE, related_name='debilidades')

    def __str__(self):
        return f"Debilidad ({self.categoria}) - {self.nino}"

class Escuela(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True)
    comuna = models.ForeignKey(Comuna, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE, related_name='profesores')
    usuario = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre