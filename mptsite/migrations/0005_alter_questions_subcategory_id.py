# Generated by Django 5.0.1 on 2024-08-20 16:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mptsite', '0004_alter_disciplines_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='subcategory_id',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mptsite.subcategory_of_questions', verbose_name='Подкатегория'),
        ),
    ]
