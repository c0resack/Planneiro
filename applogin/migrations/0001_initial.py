# Generated by Django 5.0.6 on 2024-06-24 02:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_proyecto', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=50)),
                ('porcentaje', models.FloatField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_final', models.DateField()),
                ('presupuesto', models.FloatField()),
                ('costo_final', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_rol', models.CharField(max_length=50)),
                ('descripcion_rol', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Impacto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('impacto', models.TextField()),
                ('plan_de_impacto', models.TextField()),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='impactos', to='applogin.proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='Fase',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fase', models.CharField(max_length=50)),
                ('concluido', models.BooleanField()),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fases', to='applogin.proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url_documento', models.URLField()),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documentos', to='applogin.proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='RecursoMaterial',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('nombre_recurso', models.CharField(max_length=100)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recursos_materiales', to='applogin.proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='Riesgo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('porcentaje_riesgo', models.FloatField()),
                ('descripcion_riesgo', models.TextField()),
                ('plan_mitigacion_riesgo', models.TextField()),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='riesgos', to='applogin.proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('nombre_usuario', models.CharField(max_length=50, unique=True)),
                ('contrasena', models.CharField(max_length=50)),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applogin.rol')),
            ],
        ),
        migrations.CreateModel(
            name='RecursoHumano',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recursos_humanos', to='applogin.proyecto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recursos_humanos', to='applogin.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='proyecto',
            name='admin_proyecto_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proyectos', to='applogin.usuario'),
        ),
    ]