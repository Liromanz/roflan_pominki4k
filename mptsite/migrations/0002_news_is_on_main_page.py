# Generated by Django 5.0.1 on 2024-08-20 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mptsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='is_on_main_page',
            field=models.BooleanField(default=False, verbose_name='Показать на главной странице'),
        ),
    ]
