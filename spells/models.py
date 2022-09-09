from django.db import models


# Create your models here.
class DndSpells(models.Model):
    spell_name: str = models.CharField(max_length=100)
    range: str = models.CharField(max_length=50)
    ritual: bool = models.BooleanField(default=False)
    school: str = models.CharField(max_length=50, choices=[
        ('EVO', 'Evocation'),
        ('CON', 'Conjuration'),
        ('NEC', 'Necromancy'),
        ('ILL', 'Illusion'),
        ('ABJ', 'Abjuration'),
        ('TRA', 'Transmutation'),
        ('DIV', 'Divination'),
        ('ENC', 'Enchantment'),
    ])
    duration: str = models.CharField(max_length=50)
    spell_description: str = models.TextField()
    level: str = models.CharField(max_length=1, choices=[
        ('C', 'Cantrip'),
        ('1', '1st Level'),
        ('2', '2nd Level'),
        ('3', '3rd Level'),
        ('4', '4th Level'),
        ('5', '5th Level'),
        ('6', '6th Level'),
        ('7', '7th Level'),
        ('8', '8th Level'),
        ('9', '9th Level'),
    ])
    casting_time: str = models.CharField(max_length=20)
    verbal: bool = models.BooleanField()
    somatic: bool = models.BooleanField()
    material: bool = models.BooleanField()
    materials_needed: str = models.CharField(max_length=100, default='None', blank=True, null=True)

    class Meta:
        verbose_name = 'DnD Spell'

    def save(self):
        if not self.material:
            self.materials_needed = 'None'

        return super().save()

    def __str__(self):
        return self.spell_name