# Generated by Django 4.2.2 on 2023-07-02 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionpedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='telefono',
            field=models.FloatField(),
        ),
    ]
