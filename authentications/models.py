from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User, AbstractUser
from datetime import datetime


# Create your models here.
class Profile(models.Model):
    user: int = models.OneToOneField(User, on_delete=models.CASCADE)
    username: str = models.CharField(max_length=150, blank=True, null=True)
    email: str = models.EmailField(default='')
    image: str = models.ImageField(upload_to=f'images/profiles/{user}', blank=True, null=True)
    motto: str = models.CharField(max_length=100, blank=True, null=True, help_text='Your warcry!')
    slug: str = models.SlugField(blank=True, null=True)
    created_at = models.DateTimeField(datetime.now())

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(f'{self.user}')
        if not self.username:
            self.username = self.user.username
        if not self.email:
            self.email = self.user.email

        return super().save()
