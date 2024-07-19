# Generated by Django 5.0.6 on 2024-07-03 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('empresa', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='InformeSectorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector', models.CharField(max_length=50)),
                ('informesDisponibles', models.BooleanField()),
                ('UltimaPublicacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Prensa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TituloNoticia', models.CharField(max_length=50)),
                ('medio', models.CharField(max_length=50)),
                ('LinkNoticia', models.CharField(max_length=50)),
            ],
        ),
    ]
