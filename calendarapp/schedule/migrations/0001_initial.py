# Generated by Django 5.0.14 on 2025-05-07 09:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sinif_no', models.CharField(max_length=10, unique=True)),
                ('kapasite', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Sınıf',
                'verbose_name_plural': 'Sınıflar',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=200)),
                ('instructor', models.CharField(max_length=100)),
                ('capacity', models.IntegerField(default=0)),
                ('total_students', models.IntegerField(default=0)),
                ('duration', models.IntegerField(default=60)),
            ],
        ),
        migrations.CreateModel(
            name='ScheduledCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday')])),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.course')),
            ],
            options={
                'ordering': ['day', 'start_time'],
            },
        ),
    ]
