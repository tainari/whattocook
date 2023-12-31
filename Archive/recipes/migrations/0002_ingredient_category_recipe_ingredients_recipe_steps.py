# Generated by Django 4.2.2 on 2023-06-23 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='category',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='recipes.recipeingredients'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='steps',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='recipes.recipesteps'),
        ),
    ]
