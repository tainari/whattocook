# Generated by Django 4.2.2 on 2023-08-01 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0014_alter_recipe_cook_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='flavour_category',
            new_name='flavour_category_a',
        ),
    ]