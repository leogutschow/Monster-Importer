# Generated by Django 4.0.6 on 2022-10-31 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monsters', '0019_alter_pathfinderoffense_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pathfinderoffense',
            name='effect',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]