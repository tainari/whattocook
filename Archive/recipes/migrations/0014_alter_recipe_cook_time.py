# Generated by Django 4.2.2 on 2023-08-01 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0013_delete_recipesteps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cook_time',
            field=models.CharField(choices=[('S', 'Snap'), ('F', 'Fast'), ('R', 'Regular'), ('L', 'Long'), ('O', 'Overnightttt')], max_length=1),
        ),
    ]