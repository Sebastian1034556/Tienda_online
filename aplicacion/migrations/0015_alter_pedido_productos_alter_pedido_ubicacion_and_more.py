# Generated by Django 5.0.2 on 2024-04-23 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aplicacion", "0014_alter_cliente_dni"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pedido",
            name="productos",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="pedido",
            name="ubicacion",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="producto",
            name="stock",
            field=models.PositiveIntegerField(),
        ),
    ]