# Generated by Django 4.0.1 on 2022-01-07 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Assign', '0002_userprofile_assignment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_date', models.DateField()),
                ('title', models.CharField(default='', max_length=100)),
                ('body', models.TextField(default='', max_length=1000)),
                ('points', models.FloatField(default=0.0)),
                ('comments', models.CharField(default='', max_length=200)),
                ('worked', models.BooleanField(default=False)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Assign.assignment')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Assign.userprofile')),
            ],
        ),
    ]
