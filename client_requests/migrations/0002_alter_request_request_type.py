# Generated by Django 4.0.6 on 2022-08-23 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_requests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='request_type',
            field=models.CharField(choices=[('O', 'Other'), ('M', 'Monsters'), ('A', 'Add new Game'), ('T', 'Add new Translation'), ('B', 'Found a Bug')], default='', max_length=1),
        ),
    ]