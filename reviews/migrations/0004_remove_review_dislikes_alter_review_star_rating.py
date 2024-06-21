# Generated by Django 4.2.13 on 2024-06-21 10:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_review_dislikes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='dislikes',
        ),
        migrations.AlterField(
            model_name='review',
            name='star_rating',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]