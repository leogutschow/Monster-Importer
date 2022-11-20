# Generated by Django 4.0.6 on 2022-10-30 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monsters', '0013_alter_basesheet_hp_dices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pathfindermonster',
            name='monster_alignment',
            field=models.CharField(choices=[('LG', 'Lawful Good'), ('LN', 'Lawful Neutral'), ('LE', 'Lawful Evil'), ('NG', 'Neutral Good'), ('N', 'Neutral'), ('CN', 'Chaotic Neutral'), ('CG', 'Chaotic Good'), ('CN', 'Chaotic Neutral'), ('CE', 'Chaotic Evil')], default='N', max_length=100),
        ),
    ]