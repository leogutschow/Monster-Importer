from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser


# Create your models here.
class Profile(models.Model):
    roles: list = [
        ('NEGM', 'New GM'),
        ('WBGM', 'World Builder GM'),
        ('MMGM', 'Master Mind GM'),
        ('GLGM', 'Godlike GM'),
    ]
    user: int = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    image: str = models.ImageField(upload_to=f'images/profiles/{user}', blank=True, null=True)
    motto: str = models.CharField(max_length=100, blank=True, null=True, help_text='Your warcry!')
    role: str = models.CharField(max_length=4, choices=roles, default='NEGM')
    slug: str = models.SlugField(blank=True, null=True)
    created_at = models.DateTimeField(timezone.now(), default=timezone.now())

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(f'{self.user}')
        return super().save()

    def __str__(self):
        return str(self.user)
