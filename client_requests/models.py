from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Request(models.Model):
    client: int = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type: str = models.CharField(default='O', max_length=1, choices=[
        ('O', 'Other Issues'),
        ('M', 'Monsters'),
        ('F', 'Found a Bug'),
        ('A', 'Add a Game'),
        ('T', 'Add a Translation'),
    ])
    request_title: str = models.CharField(max_length=50)
    request_text: str = models.TextField()
