# Generated by Django 4.2.2 on 2023-08-01 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0015_rename_flavour_category_recipe_flavour_category_a'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipeingredient',
            name='r',
            field=models.FloatField(default=0, null=True),
        ),
    ]
