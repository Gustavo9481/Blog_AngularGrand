# Generated by Django 5.0.2 on 2024-03-30 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Core', '0011_alter_post_contenido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='etiqueta',
            field=models.CharField(choices=[('fotografía', 'fotografía'), ('budismo', 'budismo')], max_length=20),
        ),
    ]
