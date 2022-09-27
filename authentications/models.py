from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser


def image_path(instance, filename):
    return f'images/profiles/{instance}/{filename}'


# Create your models here.
class Profile(models.Model):
    roles: list = [
        ('NEGM', 'New GM'),
        ('WBGM', 'World Builder GM'),
        ('MMGM', 'Master Mind GM'),
        ('GLGM', 'Godlike GM'),
    ]
    user: int = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    image: str = models.ImageField(upload_to=image_path, blank=True, null=True)
    motto: str = models.CharField(max_length=100, blank=True, null=True, help_text='Your warcry!')
    role: str = models.CharField(max_length=4, choices=roles, default='NEGM')
    slug: str = models.SlugField(blank=True, null=True)
    created_at = models.DateTimeField(timezone.now, default=timezone.now)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(f'{self.user}')
        return super().save()

    def __str__(self):
        return str(self.user)


class Notification(models.Model):
    notification_type = [
        ('FC', 'Forum Comment'),
        ('NL', 'News Letter'),
    ]
    to_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=notification_type)
    message = models.TextField()
    seen = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.type}-{self.to_profile}-{self.message}'
