# Generated by Django 4.0.1 on 2022-01-24 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_color_pokemon_type_delete_project_color_pokemon'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
