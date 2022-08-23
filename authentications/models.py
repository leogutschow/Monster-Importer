from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user: int = models.OneToOneField(User, on_delete=models.CASCADE)
    image: str = models.ImageField(upload_to=f'images/profiles/{user.username}', blank=True, null=True)
    motto: str = models.CharField(max_length=100, blank=True, null=True, help_text='Your warcry!')

