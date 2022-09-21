from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from authentications.models import Profile
from monsters.models import games
from multiselectfield import MultiSelectField


# Create your models here.
class DevLog(models.Model):
    tags = [
        ('Development and Production', (
            ('BUGS', 'Bug Fixing'),
            ('DEV', 'Development'),
            ('ANNO', 'Announcement'),
            )),
        ('Games', games),
    ]
    author = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200, default="Devlog(0.0.0) The Title Here")
    tags = MultiSelectField(choices=tags)
    devlog_text = models.TextField()
    created_at = models.DateTimeField(timezone.now, default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.author.user.is_staff:
            return
        if not self.slug:
            self.slug = slugify(f'{self.title}')
        return super().save()


class DevLogComment(models.Model):
    devlog = models.ForeignKey(DevLog, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, default="", on_delete=models.CASCADE, blank=True, null=True)
    commentary = models.TextField()
    created_at = models.DateTimeField(timezone.now, default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'Comment by {self.author} in {self.devlog}'
