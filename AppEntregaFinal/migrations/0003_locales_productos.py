# Generated by Django 4.0.6 on 2022-08-02 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppEntregaFinal', '0002_pelicula_delete_prueba'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.FloatField()),
            ],
        ),
    ]
