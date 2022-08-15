from django.db import models
from django.contrib.admin.options import InlineModelAdmin

# Create your models here.
from django.utils.text import slugify


class BaseSheet(models.Model):
    name: str = models.CharField(unique=True, max_length=50)
    race: str = models.CharField(max_length=30)
    size: str = models.CharField(max_length=30)
    ac: int = models.IntegerField()
    ac_type: str = models.CharField(max_length=20)
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
    game: str = models.CharField(default='', max_length=5, choices=[
        ('DND5E', 'Dungeons and Dragons 5e'),
        ('PF2E', 'Pathfinder 2e')
    ])
    home_brew: bool = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.name}')
        return super().save()


class DnDMonster(BaseSheet):
    alignment: str = models.CharField(max_length=30, default="Neutral")
    challenge: str = models.CharField(default="0", max_length=3)
    description: str = models.TextField(default="")
    image: str = models.ImageField(upload_to='images/monsters/')
    senses: str = models.CharField(max_length=100, blank=True, null=True)
    damage_resistances: str = models.CharField(max_length=50, blank=True, null=True)
    damage_immunities: str = models.CharField(max_length=50, blank=True, null=True)
    condition_immunities: str = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = "DnD Monster"


class DnDAction(models.Model):
    monster = models.ForeignKey(DnDMonster, on_delete=models.CASCADE)
    name: str = models.CharField(max_length=30)
    description: str = models.TextField()
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
        return self.name

    def save(self, *args, **kwargs):
        if not self.is_attack:
            self.weapon_type = None
            self.attack = None
            self.reach = None
            self.hit = None
            self.hit_dice = None
            self.damage_type = None

        return super().save()


class DnDSpecialTraits(models.Model):
    monster = models.ForeignKey(DnDMonster, on_delete=models.CASCADE)
    name: str = models.CharField(max_length=20)
    description: str = models.TextField()

    class Meta:
        verbose_name = "DnD Special Trait"

    def __str__(self):
        return self.name


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
    name: str = models.CharField(max_length=15, choices=skill_list)
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
    name: str = models.CharField(max_length=20)
    description: str = models.TextField()

    class Meta:
        verbose_name = "DnD Reaction"
