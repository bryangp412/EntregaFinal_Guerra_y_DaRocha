# Generated by Django 4.0.6 on 2022-08-02 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppEntregaFinal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('categoria', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Prueba',
        ),
    ]