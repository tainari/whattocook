# Generated by Django 4.2.2 on 2023-07-24 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0011_recipe_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipesteps',
            old_name='stepnumber',
            new_name='step_number',
        ),
        migrations.RenameField(
            model_name='recipesteps',
            old_name='steptext',
            new_name='step_text',
        ),
    ]
