# Generated by Django 4.0.6 on 2022-10-16 03:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authentications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='send_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]