# Generated by Django 5.0.2 on 2024-03-02 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Core', '0002_alter_post_introduccion_alter_post_podcast_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='podcast',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
