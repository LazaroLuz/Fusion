# Generated by Django 4.2.7 on 2023-11-06 20:23

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_funcionario_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='imagem',
            field=models.ImageField(height_field=480, upload_to=core.models.get_file_path, verbose_name='Imagem', width_field=480),
        ),
    ]
