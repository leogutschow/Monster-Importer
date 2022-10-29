from django.db import models
from django.contrib.admin.options import InlineModelAdmin
from django.utils import timezone
from authentications.models import Profile
from spells.models import DndSpells

# Create your models here.
from django.utils.text import slugify

games = [
    ('DND5E', 'Dungeons and Dragons 5e'),
    ('TOR20', 'Tormenta20'),
    ('PAF1e', 'Pathfinder 1e'),
    ]

tor20_action_type: list = [
    ('SRD', 'Standard'),
    ('MOV', 'Movement'),
    ('COM', 'Complete'),
    ('FRE', 'Free'),
    ('REA', 'Reaction'),
]


def image_upload_path(instance, filename):
    if isinstance(instance, DnDMonster):
        return 'images/monsters/DnD5e/{0}'.format(filename)
    if isinstance(instance, Tor20Monster):
        return 'images/monsters/Tor20/{0}'.format(filename)
    if isinstance(instance, PathFinderMonster):
        return 'images/monsters/PathFinder1e/{0}'.format(filename)
    return 'images/monsters/fallback/{0}'.format(filename)


class BaseSheet(models.Model):
    name: str = models.CharField(unique=False, max_length=200)
    race: str = models.CharField(max_length=30, blank=True, null=True)
    size: str = models.CharField(max_length=30)
    challenge: str = models.CharField(default="0", max_length=3)
    ac: int = models.IntegerField()
    ac_type: str = models.CharField(max_length=50)
    hp: int = models.IntegerField()
    hp_dices: str = models.CharField(max_length=30)
    movement: str = models.CharField(max_length=100, blank=True, null=True,)
    strength: int = models.IntegerField()
    dexterity: int = models.IntegerField()
    constitution: int = models.IntegerField()
    intelligence: int = models.IntegerField()
    wisdom: int = models.IntegerField()
    charisma: int = models.IntegerField()
    slug: str = models.SlugField(blank=True, null=True)
    game: str = models.CharField(default='', max_length=5, choices=games)
    home_brew: bool = models.BooleanField(default=False)
    created_by = models.ForeignKey(to=Profile, blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(timezone.now, default=timezone.now)
    times_downloaded: int = models.PositiveIntegerField(default=0)
    image: str = models.ImageField(upload_to=image_upload_path, default='images/monsters/DnD5e')
    description: str = models.TextField(default="Placeholder")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.game} {self.name}')
        return super().save()


class DnDMonster(BaseSheet):
    languages: str = models.CharField(max_length=100, default="None")
    alignment: str = models.CharField(max_length=30, default="Neutral")
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


class DnDSpecialTraits(models.Model):
    spellcasting_mod_list = [
        ('STR', 'Strength'),
        ('DEX', 'Dexterity'),
        ('CON', 'Constitution'),
        ('INT', 'Intelligence'),
        ('WIS', 'Wisdom'),
        ('CHA', 'Charisma'),
    ]
    monster = models.ForeignKey(DnDMonster, on_delete=models.CASCADE)
    specialtrait_name: str = models.CharField(max_length=50)
    specialtrait_description: str = models.TextField()
    spellcasting: bool = models.BooleanField(default=False)
    caster_level = models.PositiveIntegerField(blank=True, null=True)
    spellcasting_ability = models.CharField(max_length=3, choices=spellcasting_mod_list, default='WIS', blank=True, null=True)
    spell_attack_mod = models.PositiveIntegerField(blank=True, null=True)
    spell_dc_save = models.PositiveIntegerField(blank=True, null=True)
    dnd_spells = models.ManyToManyField(DndSpells, unique=False, blank=True, null=True)

    class Meta:
        verbose_name = "DnD Special Trait"

    def __str__(self):
        return self.specialtrait_name


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
    fortitude: int = models.PositiveIntegerField(default=0)
    reflex: int = models.PositiveIntegerField(default=0)
    will: int = models.PositiveIntegerField(default=0)
    level: int = models.PositiveIntegerField(default=0)
    mana: int = models.PositiveIntegerField(default=0)
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
    action_description = models.TextField(default='', blank=True, null=True)
    action_type = models.CharField(max_length=3, choices=tor20_action_type, default='SRD', blank=True, null=True)
    mana_cost = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'Generic Action'


class Tor20BaseAttackAction(models.Model):
    monster = models.ForeignKey(Tor20Monster, on_delete=models.CASCADE)
    action_name = models.CharField(max_length=100, default='')
    action_description = models.TextField(default='', blank=True, null=True)
    attack = models.PositiveIntegerField(blank=True, null=True)
    hit = models.CharField(max_length=25, blank=True, null=True)


class Tor20MeleeAction(Tor20BaseAttackAction):
    class Meta:
        verbose_name = 'Melee Action'


class Tor20RangedAction(Tor20BaseAttackAction):
    class Meta:
        verbose_name = 'Ranged Action'


class PathFinderMonster(BaseSheet):
    alignment = [
        ('LG', 'Lawful Good'),
        ('LN', 'Lawful Neutral'),
        ('LE', 'Lawful Evil'),
        ('NG', 'Neutral Good'),
        ('N', 'Neutral'),
        ('CN', 'Chaotic Neutral'),
        ('CG', 'Chaotic Good'),
        ('CN', 'Chaotic Neutral'),
        ('CE', 'Chaotic Evil'),
    ]
    monster_class = models.CharField(max_length=25, default='', blank=True, null=True)
    monster_alignment: str = models.CharField(max_length=30, choices=alignment, default="N")
    type = models.CharField(max_length=20)
    subtype = models.CharField(max_length=50, blank=True, null=True)
    init = models.CharField(max_length=20)
    senses = models.CharField(max_length=100, blank=True, null=True)
    aura = models.CharField(max_length=50, blank=True, null=True)
    ac_mod = models.CharField(max_length=100, blank=True, null=True)
    hp_mod = models.CharField(max_length=100, blank=True, null=True)
    fortitude = models.IntegerField()
    reflex = models.IntegerField()
    will = models.IntegerField()
    save_mods = models.CharField(max_length=100, blank=True, null=True)
    damage_reduction = models.CharField(max_length=50, blank=True, null=True)
    immune = models.CharField(max_length=100, blank=True, null=True)
    resist = models.CharField(max_length=50, blank=True, null=True)
    spell_resistence = models.PositiveIntegerField(blank=True, null=True)
    weaknesses = models.CharField(max_length=50, blank=True, null=True)
    feats = models.TextField(default='', blank=True, null=True)
    speed_mod = models.CharField(max_length=50, blank=True, null=True)
    space = models.CharField(max_length=10, blank=True, null=True)
    reach = models.CharField(max_length=20, blank=True, null=True)
    spell_domain = models.CharField(max_length=100, blank=True, null=True)
    base_attack = models.PositiveIntegerField(blank=True, null=True)
    combat_maneuver_bonus = models.CharField(max_length=50, blank=True, null=True, verbose_name='CMB')
    combat_maneuver_defence = models.CharField(max_length=50, blank=True, null=True, verbose_name='CMD')
    languages = models.CharField(max_length=100, blank=True, null=True)
    special_qualities = models.CharField(max_length=100, blank=True, null=True)
    environment = models.CharField(max_length=100, blank=True, null=True)
    organization = models.CharField(max_length=100, blank=True, null=True)
    treasure = models.CharField(max_length=200, blank=True, null=True)


class PathFinderOffense(models.Model):
    monster = models.ForeignKey(PathFinderMonster, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=1, choices=[('M', 'Melee'), ('R', 'Ranged')])
    attack = models.CharField(max_length=20, blank=True, null=True)
    effect = models.CharField(max_length=20, blank=True, null=True)
    crit_range = models.CharField(max_length=20, blank=True, null=True)
    multiple = models.BooleanField(default=False)
    damage = models.CharField(max_length=20, blank=True, null=True)
    count = models.IntegerField(default=1, blank=True, null=True)


class PathFinderSpecialAbility(models.Model):
    monster = models.ForeignKey(PathFinderMonster, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()


class PathFinderSkill(models.Model):
    skills = [
        ('Acrobatics', 'Acrobatics'),
        ('Appraise', 'Appraise'),
        ('Bluff', 'Bluff'),
        ('Climb', 'Climb'),
        ('Craft', 'Craft'),
        ('Diplomacy', 'Diplomacy'),
        ('Disable Device', 'Disable Device'),
        ('Disguise', 'Disguise'),
        ('Escape Artist', 'Escape Artist'),
        ('Fly', 'Fly'),
        ('Handle Animal', 'Handle Animal'),
        ('Heal', 'Heal'),
        ('Intimidate', 'Intimidate'),
        ('Knowledge (arcana)', 'Knowledge (arcana)'),
        ('Knowledge (dungeoneering)', 'Knowledge (dungeoneering)'),
        ('Knowledge (engineering)', 'Knowledge (engineering)'),
        ('Knowledge (geography)', 'Knowledge (geography)'),
        ('Knowledge (history)', 'Knowledge (history)'),
        ('Knowledge (local)', 'Knowledge (local)'),
        ('Knowledge (nature)', 'Knowledge (nature)'),
        ('Knowledge (nobility)', 'Knowledge (nobility)'),
        ('Knowledge (planes)', 'Knowledge (planes)'),
        ('Knowledge (religion)', 'Knowledge (religion)'),
        ('Knowledge (any one)', 'Knowledge (any one)'),
        ('Linguistics', 'Linguistics'),
        ('Perception', 'Perception'),
        ('Perform', 'Perform'),
        ('Profession', 'Profession'),
        ('Ride', 'Ride'),
        ('Sense Motive', 'Sense Motive'),
        ('Sleight of Hand', 'Sleight of Hand'),
        ('Spellcraft', 'Spellcraft'),
        ('Stealth', 'Stealth'),
        ('Survival', 'Heal'),
        ('Swim', 'Swim'),
        ('Use Magic Device', 'Use Magic Device'),
    ]
    monster = models.ForeignKey(PathFinderMonster, on_delete=models.CASCADE)
    skill = models.CharField(max_length=30, choices=skills)
    skill_bonus = models.IntegerField()
    racial_mod = models.BooleanField(default=False)

