# Generated by Django 5.0.1 on 2024-06-15 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mptsite', '0005_alter_schedules_is_cancel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='degree',
            field=models.TextField(default='', null=True, verbose_name='Ученая степень'),
        ),
    ]