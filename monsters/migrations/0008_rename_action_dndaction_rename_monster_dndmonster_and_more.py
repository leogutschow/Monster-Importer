# Generated by Django 4.0.6 on 2022-08-15 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monsters', '0007_alter_basesheet_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Action',
            new_name='DnDAction',
        ),
        migrations.RenameModel(
            old_name='Monster',
            new_name='DnDMonster',
        ),
        migrations.RenameModel(
            old_name='Skill',
            new_name='DnDSkill',
        ),
        migrations.RenameModel(
            old_name='SpecialTraits',
            new_name='DnDSpecialTraits',
        ),
    ]
