from django.db import models


# Create your models here.
class Action(models.Model):
    name: str = models.CharField(max_length=30)
    description: str = models.TextField()
    is_attack: bool = models.BooleanField(default=False)
    weapon_type: str = models.CharField(max_length=50, blank=True, null=True)
    attack: int = models.IntegerField(blank=True, null=True)
    reach: str = models.CharField(max_length=50, blank=True, null=True)
    hit: int = models.IntegerField(blank=True, null=True)
    hit_dice: str = models.CharField(max_length=10, blank=True, null=True)
    damage_type: str = models.CharField(max_length=50, blank=True, null=True)

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

