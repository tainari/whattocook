# Generated by Django 4.2.2 on 2023-06-27 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_pantry_recipeingredient_remove_recipe_ingredients_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CookMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Fillingness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Flavour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Texture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='recipe',
            name='step1',
            field=models.CharField(blank=True, default=None, max_length=1000),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='step2',
            field=models.CharField(blank=True, default=None, max_length=1000),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='step3',
            field=models.CharField(blank=True, default=None, max_length=1000),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='step4',
            field=models.CharField(blank=True, default=None, max_length=1000),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='step5',
            field=models.CharField(blank=True, default=None, max_length=1000),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='fillingness_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.fillingness'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='flavour_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.flavour'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.cookmethod'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='texture_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.texture'),
        ),
    ]
