# Generated by Django 4.0.2 on 2022-02-15 17:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facial_droop', models.BooleanField()),
                ('arm_drift', models.BooleanField()),
                ('speech', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('onset_time', models.DateTimeField()),
                ('additional_notes', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facial_droop', models.BooleanField()),
                ('arm_drift', models.BooleanField()),
                ('speech', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('onset_time', models.DateTimeField()),
                ('additional_notes', models.TextField(blank=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questionnaires', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
