# Generated by Django 5.0.7 on 2024-08-28 08:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_stories_story'),
    ]

    operations = [
        migrations.AddField(
            model_name='stories',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активный'),
        ),
        migrations.AlterField(
            model_name='story',
            name='stories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stories', to='pages.stories'),
        ),
    ]
