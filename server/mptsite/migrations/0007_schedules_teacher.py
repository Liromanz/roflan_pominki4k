# Generated by Django 5.0.3 on 2024-06-01 23:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mptsite', '0006_teacher_disciplines_disciplines_employees'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedules',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mptsite.teacher_disciplines', verbose_name='Дисциплина'),
        ),
    ]
