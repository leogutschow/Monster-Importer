# Generated by Django 4.0.6 on 2022-10-31 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monsters', '0017_alter_pathfindermonster_save_mods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pathfindermonster',
            name='special_qualities',
            field=models.TextField(blank=True, null=True),
        ),
    ]