from django.db import models

# Create your models here.
from django.utils.text import slugify


class BaseSheet(models.Model):
    name: str = models.CharField(max_length=50)
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
    slug: str = models.SlugField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.id}')
        return super().save()


class Monster(BaseSheet):
    challenge: str = models.CharField(default="0", max_length=3)
    description: str = models.TextField(default="")
