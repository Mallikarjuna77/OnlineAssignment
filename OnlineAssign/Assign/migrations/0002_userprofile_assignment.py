# Generated by Django 4.0.1 on 2022-01-07 04:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Assign', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity', models.CharField(choices=[('teacher', 'teacher'), ('student', 'student'), ('assistant', 'assistant')], default='student', max_length=100)),
                ('courses', models.CharField(default='', max_length=500)),
                ('full_name', models.CharField(max_length=100)),
                ('year', models.IntegerField(choices=[(1, '1st Year'), (2, '2nd Year'), (3, '3rd Year'), (4, '4th Year')], default=1)),
                ('roll_no', models.CharField(max_length=8, unique=True)),
                ('created', models.DateField(editable=False, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(choices=[(1, '1st Year'), (2, '2nd Year'), (3, '3rd Year'), (4, '4th Year')], default=1)),
                ('name', models.CharField(max_length=100)),
                ('questions', models.TextField(max_length=100)),
                ('num', models.IntegerField(default=1)),
                ('created', models.DateField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('deadline', models.DateField()),
                ('course', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Assign.course')),
                ('teacher', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Assign.userprofile')),
            ],
        ),
    ]
