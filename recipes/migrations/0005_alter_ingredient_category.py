# Generated by Django 4.2.2 on 2023-06-24 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_alter_recipe_ingredients_delete_recipeingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='category',
            field=models.CharField(max_length=255),
        ),
    ]