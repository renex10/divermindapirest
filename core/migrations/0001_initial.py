# Generated by Django 5.1.6 on 2025-02-20 03:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('geografia', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Nino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('necesidades_especiales', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PerfilPersonal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=20, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('lugar_nacimiento', models.CharField(blank=True, max_length=100)),
                ('foto_perfil', models.ImageField(blank=True, null=True, upload_to='perfiles/')),
            ],
        ),
        migrations.CreateModel(
            name='Escuela',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(blank=True, max_length=20)),
                ('comuna', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='geografia.comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_familia', models.CharField(max_length=100)),
                ('telefono', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('miembros', models.ManyToManyField(related_name='familias', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('fecha_diagnostico', models.DateField()),
                ('nino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diagnosticos', to='core.nino')),
            ],
        ),
        migrations.CreateModel(
            name='DetonanteCrisis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('nino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detonantes_crisis', to='core.nino')),
            ],
        ),
        migrations.CreateModel(
            name='Debilidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('categoria', models.CharField(choices=[('sensorial', 'Sensorial'), ('comunicacion', 'Comunicación'), ('emocional', 'Emocional'), ('otros', 'Otros')], max_length=15)),
                ('nivel', models.CharField(choices=[('leve', 'Leve'), ('moderado', 'Moderado'), ('severo', 'Severo')], max_length=10)),
                ('nino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='debilidades', to='core.nino')),
            ],
        ),
        migrations.CreateModel(
            name='Autismo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel', models.CharField(choices=[('leve', 'Leve'), ('moderado', 'Moderado'), ('severo', 'Severo')], max_length=10)),
                ('descripcion', models.TextField(blank=True)),
                ('nino', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='autismo', to='core.nino')),
            ],
        ),
        migrations.CreateModel(
            name='NinoFamilia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField(auto_now_add=True)),
                ('fecha_fin', models.DateField(blank=True, null=True)),
                ('familia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.familia')),
                ('nino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.nino')),
            ],
        ),
        migrations.AddField(
            model_name='nino',
            name='familias',
            field=models.ManyToManyField(through='core.NinoFamilia', to='core.familia'),
        ),
        migrations.CreateModel(
            name='ObservacionEscuela',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('comportamiento', models.TextField(blank=True)),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('revisado', 'Revisado'), ('rechazado', 'Rechazado')], default='pendiente', max_length=10)),
                ('nino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='observaciones_escuela', to='core.nino')),
                ('profesor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ObservacionFamilia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('rutinas', models.TextField(blank=True)),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('revisado', 'Revisado'), ('rechazado', 'Rechazado')], default='pendiente', max_length=10)),
                ('nino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='observaciones_familia', to='core.nino')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='nino',
            name='id_perfil',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='nino', to='core.perfilpersonal'),
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('escuela', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profesores', to='core.escuela')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
