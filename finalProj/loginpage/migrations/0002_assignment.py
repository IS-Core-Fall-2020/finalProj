# Generated by Django 3.1.2 on 2020-11-21 04:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assign_name', models.CharField(max_length=30)),
                ('assign_description', models.CharField(max_length=250)),
                ('assign_completion', models.BooleanField()),
                ('assign_duedate', models.DateField(blank=True, default=datetime.datetime.today)),
            ],
        ),
    ]