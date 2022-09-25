from django.db import models
from django.utils import timezone
from authentications.models import Profile
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
    name: str = models.CharField(max_length=20)
    description: str = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.slug:
            self.slug = slugify(f'{self.name}')
        return super().save()


class Forum(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title: str = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(timezone.now, default=timezone.now)
    published: bool = models.BooleanField(default=True)
    slug = models.SlugField(blank=True, null=True)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.slug:
            self.slug = slugify(f'{self.title}')
        return super().save()


class ForumComment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(timezone.now, default=timezone.now)
    published: bool = models.BooleanField(default=True)
