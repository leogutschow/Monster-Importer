# Generated by Django 4.0.6 on 2022-08-11 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manuals', '0006_manual_image_alter_manual_file_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manual',
            name='image',
            field=models.ImageField(upload_to='documents/manuals/thumbs/'),
        ),
    ]