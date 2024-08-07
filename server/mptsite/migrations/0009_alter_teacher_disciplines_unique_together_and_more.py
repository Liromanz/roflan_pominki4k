# Generated by Django 5.0.1 on 2024-06-16 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mptsite', '0008_alter_teacher_disciplines_unique_together_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='teacher_disciplines',
            constraint=models.UniqueConstraint(condition=models.Q(('employee', None)), fields=('discipline',), name='Teacher_Null_Disc_UQ'),
        ),
    ]