# Generated by Django 4.0.6 on 2022-08-10 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manuals', '0004_alter_manual_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manual',
            name='image',
        ),
    ]