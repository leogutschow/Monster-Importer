# Generated by Django 4.0.6 on 2022-10-29 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monsters', '0008_alter_pathfindermonster_special_qualities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pathfindermonster',
            name='organization',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
