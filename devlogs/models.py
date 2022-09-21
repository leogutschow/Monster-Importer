from django.db import models
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

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.author.user.is_staff:
            return
        return super().save()
