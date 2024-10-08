# Generated by Django 5.0.1 on 2024-09-16 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mptsite', '0006_alter_questions_subcategory_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='short_description',
        ),
        migrations.AddField(
            model_name='news',
            name='news_content',
            field=models.TextField(default='', null=True, verbose_name='Содержимое новости'),
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(default='', max_length=100, verbose_name='Краткое описание'),
        ),
    ]
