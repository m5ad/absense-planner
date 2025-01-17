# Generated by Django 4.0.2 on 2022-02-21 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('plannerapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='absences',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('absence_date', models.CharField(max_length=200)),
                ('request_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('manager_ID', models.CharField(max_length=200)),
                ('request_accepted', models.BooleanField()),
                ('reason', models.CharField(max_length=200)),
                ('User_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='employees',
        ),
    ]
