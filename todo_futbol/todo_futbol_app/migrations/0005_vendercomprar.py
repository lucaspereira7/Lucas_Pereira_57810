# Generated by Django 5.0.6 on 2024-07-18 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_futbol_app', '0004_alter_buscar_rival_dia_reserva_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VenderComprar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_articulo', models.CharField(max_length=40)),
                ('estado_articulo', models.CharField(max_length=10)),
                ('talle', models.IntegerField()),
                ('precio', models.CharField(max_length=10)),
                ('numero_celular', models.IntegerField()),
            ],
            options={
                'verbose_name': 'vender/comprar',
                'verbose_name_plural': 'vender/comprar',
                'ordering': ['talle', 'precio'],
            },
        ),
    ]