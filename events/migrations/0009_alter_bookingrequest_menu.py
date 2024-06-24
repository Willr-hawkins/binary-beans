# Generated by Django 4.2.13 on 2024-06-23 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_eventmenus'),
        ('events', '0008_bookingrequest_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingrequest',
            name='menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu', to='menu.eventmenus'),
        ),
    ]