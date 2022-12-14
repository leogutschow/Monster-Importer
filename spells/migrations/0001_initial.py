# Generated by Django 4.0.6 on 2022-08-28 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DndSpells',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spell_name', models.CharField(max_length=100)),
                ('range', models.CharField(max_length=50)),
                ('ritual', models.BooleanField(default=False)),
                ('school', models.CharField(choices=[('EVO', 'Evocation'), ('CON', 'Conjuration'), ('NEC', 'Necromancy'), ('ILL', 'Illusion'), ('ABJ', 'Abjuration'), ('TRA', 'Transmutation'), ('DIV', 'Divination'), ('ENC', 'Enchantment')], max_length=50)),
                ('duration', models.CharField(max_length=50)),
                ('spell_description', models.TextField()),
                ('level', models.CharField(choices=[('C', 'Cantrip'), ('1', '1st Level'), ('2', '2nd Level'), ('3', '3rd Level'), ('4', '4th Level'), ('5', '5th Level'), ('6', '6th Level'), ('7', '7th Level'), ('8', '8th Level'), ('9', '9th Level')], max_length=1)),
                ('casting_time', models.CharField(max_length=20)),
                ('verbal', models.BooleanField()),
                ('somatic', models.BooleanField()),
                ('material', models.BooleanField()),
                ('materials_needed', models.CharField(blank=True, default='None', max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'DnD Spell',
            },
        ),
    ]
