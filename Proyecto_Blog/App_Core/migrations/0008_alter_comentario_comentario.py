# Generated by Django 5.0.2 on 2024-03-05 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Core', '0007_comentario_art_relacionado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='comentario',
            field=models.TextField(max_length=300),
        ),
    ]
