# Generated by Django 4.0.6 on 2022-08-15 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monsters', '0012_dndreaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='basesheet',
            name='home_brew',
            field=models.BooleanField(default=False),
        ),
    ]