# Generated by Django 4.0.6 on 2022-11-21 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monsters', '0002_remove_cocmonster_attacks_per_round'),
    ]

    operations = [
        migrations.AddField(
            model_name='cocmonster',
            name='attacks_per_round',
            field=models.CharField(blank=True, default='1D8', max_length=255, null=True),
        ),
    ]
