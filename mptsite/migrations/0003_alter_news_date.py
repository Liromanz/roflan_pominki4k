# Generated by Django 5.0.1 on 2024-08-20 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mptsite', '0002_news_is_on_main_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(verbose_name='Дата новости'),
        ),
    ]