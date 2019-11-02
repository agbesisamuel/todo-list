# Generated by Django 2.2.5 on 2019-09-26 09:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='deadline',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='start_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
