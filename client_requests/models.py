from django.db import models
from authentications.models import Profile


# Create your models here.
class Request(models.Model):
    client: int = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    request_type: str = models.CharField(default='', max_length=1, choices=[
        ('O', 'Other'),
        ('M', 'Monsters'),
        ('A', 'Add new Game'),
        ('T', 'Add new Translation'),
        ('B', 'Found a Bug'),
    ])
    request_title: str = models.CharField(max_length=50)
    request_text: str = models.TextField()


