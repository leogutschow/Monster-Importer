from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monsters', '0001_initial'),
        ('monsters', '0003_alter_basesheet_charisma_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dndaction',
            name='hit_dice',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
