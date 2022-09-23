from django.db import models
from django.utils import timezone
from authentications.models import Profile


# Create your models here.
class Category(models.Model):
    name: str = models.CharField(max_length=20)
    description: str = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Forum(models.Model):
    title: str = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(timezone.now, default=timezone.now)
    published: bool = models.BooleanField(default=True)


class ForumComment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(timezone.now, default=timezone.now)
    published: bool = models.BooleanField(default=True)
