# Generated by Django 2.2.5 on 2019-09-26 09:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('start_at', models.DateField(default=datetime.datetime(2019, 9, 26, 9, 25, 4, 232688, tzinfo=utc))),
                ('deadline', models.DateField(default=datetime.datetime(2019, 9, 26, 9, 25, 4, 232710, tzinfo=utc))),
            ],
            options={
                'ordering': ('start_at',),
            },
        ),
    ]
