# Generated by Django 4.1 on 2022-08-23 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artesania',
            name='descripcion',
            field=models.TextField(max_length=50, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='artesania',
            name='nombre',
            field=models.TextField(max_length=20, verbose_name='Nombre'),
        ),
    ]
