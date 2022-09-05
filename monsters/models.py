from django.db import models
from django.contrib.admin.options import InlineModelAdmin
from django.utils import timezone
from authentications.models import Profile
from spells.models import DndSpells

# Create your models here.
from django.utils.text import slugify

games = [
        ('DND5E', 'Dungeons and Dragons 5e'),
        ('TOR20', 'Tormenta20')
    ]


def image_upload_path(instance, filename):
    if isinstance(instance, DnDMonster):
        return 'images/monsters/DnD5e/{0}'.format(filename)
    if isinstance(instance, Tor20Monster):
        return 'images/monsters/Tor20/{0}'.format(filename)
    return 'images/monsters/fallback/{0}'.format(filename)


class BaseSheet(models.Model):
    name: str = models.CharField(unique=False, max_length=50)
    race: str = models.CharField(max_length=30)
    size: str = models.CharField(max_length=30)
    challenge: str = models.CharField(default="0", max_length=3)
    ac: int = models.IntegerField()
    ac_type: str = models.CharField(max_length=50)
    hp: int = models.IntegerField()
    hp_dices: str = models.CharField(max_length=10)
    movement: str = models.CharField(max_length=30)
    strength: int = models.IntegerField()
    dexterity: int = models.IntegerField()
    constitution: int = models.IntegerField()
    intelligence: int = models.IntegerField()
    wisdom: int = models.IntegerField()
    charisma: int = models.IntegerField()
    languages: str = models.CharField(max_length=100, default="None")
    slug: str = models.SlugField(blank=True, null=True)
    game: str = models.CharField(default='', max_length=5, choices=games)
    home_brew: bool = models.BooleanField(default=False)
    created_by = models.ForeignKey(to=Profile, blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(timezone.now(), default=timezone.now())
    times_downloaded: int = models.PositiveIntegerField(default=0)
    image: str = models.ImageField(upload_to=image_upload_path, default='images/monsters/DnD5e')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.game} {self.name}')
        return super().save()


class DnDMonster(BaseSheet):
    alignment: str = models.CharField(max_length=30, default="Neutral")
    description: str = models.TextField(default="")
    senses: str = models.CharField(max_length=100, blank=True, null=True)
    damage_resistances: str = models.CharField(max_length=100, blank=True, null=True)
    damage_immunities: str = models.CharField(max_length=100, blank=True, null=True)
    condition_immunities: str = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "DnD Monster"


class DnDAction(models.Model):
    monster = models.ForeignKey(DnDMonster, on_delete=models.CASCADE)
    action_name: str = models.CharField(max_length=30)
    action_description: str = models.TextField()
    is_attack: bool = models.BooleanField(default=False)
    weapon_type: str = models.CharField(max_length=50, blank=True, null=True)
    attack: int = models.IntegerField(blank=True, null=True)
    reach: str = models.CharField(max_length=50, blank=True, null=True)
    hit: int = models.IntegerField(blank=True, null=True)
    hit_dice: str = models.CharField(max_length=10, blank=True, null=True)
    damage_type: str = models.CharField(max_length=50, blank=True, null=True)
    
    class Meta:
        verbose_name = "DnD Action"

    def __str__(self):
        return self.action_name


class DnDLegendaryAction(models.Model):
    monster = models.ForeignKey(DnDMonster, on_delete=models.CASCADE)
    legendary_name = models.CharField(max_length=50)
    legendary_description = models.TextField()


class DnDSpecialTraits(models.Model):
    monster = models.ForeignKey(DnDMonster, on_delete=models.CASCADE)
    specialtrait_name: str = models.CharField(max_length=20)
    specialtrait_description: str = models.TextField()
    spellcasting: bool = models.BooleanField(default=False)
    dnd_spells = models.ManyToManyField(DndSpells, unique=False, blank=True, null=True)

    class Meta:
        verbose_name = "DnD Special Trait"

    def __str__(self):
        return self.specialtrait_name


class DnDSkill(models.Model):
    skill_list: list = [
        ('Athletics', 'Athletics'),
        ('Acrobatics', 'Acrobatics'),
        ('Sleight of Hand', 'Sleight of Hand'),
        ('Stealth', 'Stealth'),
        ('Arcana', 'Arcana'),
        ('History', 'History'),
        ('Investigation', 'Investigation'),
        ('Nature', 'Nature'),
        ('Religion', 'Religion'),
        ('Animal Handling', 'Animal Handling'),
        ('Insight', 'Insight'),
        ('Medicine', 'Medicine'),
        ('Perception', 'Perception'),
        ('Survival', 'Survival'),
        ('Deception', 'Deception'),
        ('Intimidation', 'Intimidation'),
        ('Performance', 'Performance'),
        ('Persuasion', 'Persuasion')
    ]
    monster = models.ForeignKey(DnDMonster, on_delete=models.CASCADE)
    skill_name: str = models.CharField(max_length=15, choices=skill_list)
    modifier: int = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = "DnD Skill"


class DnDSavingThrows(models.Model):
    monster = models.ForeignKey(DnDMonster, on_delete=models.CASCADE, default=4)
    attr: str = models.CharField(max_length=3, choices=[
        ('STR', 'Strength'),
        ('DEX', 'Dexterity'),
        ('CON', 'Constitution'),
        ('INT', 'Intelligence'),
        ('WIS', 'Wisdom'),
        ('CHA', 'Charisma'),
    ])
    bonus: int = models.PositiveIntegerField()

    class Meta:
        verbose_name = "DnD Saving Throw"


class DndReaction(models.Model):
    monster = models.ForeignKey(DnDMonster, on_delete=models.CASCADE)
    reaction_name: str = models.CharField(max_length=20)
    reaction_description: str = models.TextField()

    class Meta:
        verbose_name = "DnD Reaction"


class Tor20Monster(BaseSheet):
    description: str = models.TextField()
    fortitude: int = models.PositiveIntegerField(default=0)
    reflex: int = models.PositiveIntegerField(default=0)
    will: int = models.PositiveIntegerField(default=0)
    level: int = models.PositiveIntegerField()
    mana: int = models.PositiveIntegerField()
    equipment: str = models.CharField(max_length=200, default='None')
    treasure = models.CharField(max_length=200, default='None')


class Tor20Skill(models.Model):
    skill_list: list = [
        ('Acrobatics', 'Acrobatics'),
        ('Taming', 'Taming'),
        ('Athletics', 'Athletics'),
        ('Performance', 'Performance'),
        ('Riding', 'Riding'),
        ('Knowledge', 'Knowledge'),
        ('Healing', 'Healing'),
        ('Diplomacy', 'Diplomacy'),
        ('Deception', 'Deception'),
        ('Fortitude', 'Fortitude'),
        ('Stealth', 'Stealth'),
        ('War', 'War'),
        ('Initiative', 'Initiative'),
        ('Intimidation', 'Intimidation'),
        ('Intuition', 'Intuition'),
        ('Investigation', 'Investigation'),
        ('Gambling', 'Gambling'),
        ('Sleight of Hand', 'Sleight of Hand'),
        ('Fight', 'Fight'),
        ('Mistic Arts', 'Mistic Arts'),
        ('Nobility', 'Nobility'),
        ('Diligent', 'Diligent'),
        ('Perception', 'Perception'),
        ('Pilotage', 'Pilotage'),
        ('Aiming', 'Aiming'),
        ('Reflexes', 'Reflexes'),
        ('Religion', 'Religion'),
        ('Survival', 'Survival'),
        ('Will', 'Will')
    ]
    monster = models.ForeignKey(Tor20Monster, on_delete=models.CASCADE)
    skill_name: str = models.CharField(max_length=15, default='', choices=skill_list)
    skill_bonus: int = models.PositiveIntegerField()


class Tor20GenericAction(models.Model):
    monster = models.ForeignKey(Tor20Monster, on_delete=models.CASCADE)
    action_name = models.CharField(max_length=100)
    ranged = models.BooleanField(default=False)
    action_description = models.TextField(blank=True, null=True)


class Tor20MeleeAction(models.Model):
    monster = models.ForeignKey(Tor20Monster, on_delete=models.CASCADE)
    action_name = models.CharField(max_length=100)
    attack = models.PositiveIntegerField(blank=True, null=True)
    hit = models.CharField(max_length=25, blank=True, null=True)


class Tor20RangedAction(models.Model):
    monster = models.ForeignKey(Tor20Monster, on_delete=models.CASCADE)
    action_name = models.CharField(max_length=100)
    attack = models.PositiveIntegerField(blank=True, null=True)
    hit = models.CharField(max_length=25, blank=True, null=True)
