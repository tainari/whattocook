# Generated by Django 4.2.2 on 2023-06-23 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_ingredient_category_recipe_ingredients_recipe_steps'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='steps',
        ),
        migrations.AddField(
            model_name='recipe',
            name='step1',
            field=models.CharField(default=None, max_length=1000),
        ),
        migrations.AddField(
            model_name='recipe',
            name='step2',
            field=models.CharField(default=None, max_length=1000),
        ),
        migrations.AddField(
            model_name='recipe',
            name='step3',
            field=models.CharField(default=None, max_length=1000),
        ),
        migrations.AddField(
            model_name='recipe',
            name='step4',
            field=models.CharField(default=None, max_length=1000),
        ),
        migrations.AddField(
            model_name='recipe',
            name='step5',
            field=models.CharField(default=None, max_length=1000),
        ),
        migrations.AddField(
            model_name='recipeingredients',
            name='num_units',
            field=models.FloatField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.recipeingredients'),
        ),
        migrations.AlterField(
            model_name='recipeingredients',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.ingredient'),
        ),
        migrations.DeleteModel(
            name='RecipeSteps',
        ),
        migrations.AddField(
            model_name='recipeingredients',
            name='unit',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='recipes.unit'),
            preserve_default=False,
        ),
    ]
