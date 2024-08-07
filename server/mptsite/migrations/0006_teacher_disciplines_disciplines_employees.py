# Generated by Django 5.0.3 on 2024-06-01 23:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mptsite', '0005_remove_schedules_teacher_delete_teacher_disciplines'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher_Disciplines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discipline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mptsite.disciplines', verbose_name='Дисциплина')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mptsite.employees', verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'Свод препод - дисциплина',
                'verbose_name_plural': 'Преподаваемые дисциплины',
            },
        ),
        migrations.AddField(
            model_name='disciplines',
            name='employees',
            field=models.ManyToManyField(through='mptsite.Teacher_Disciplines', to='mptsite.employees'),
        ),
    ]
