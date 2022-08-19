from django.db import models

languages: list = [
    ('PT', 'Portuguese'),
    ('EN', 'English'),
]

categories = [
    ('MON', 'Monsters'),
    ('PLA', 'PlayerBooks'),
    ('GMS', 'Game Masters Guides'),

]


# Create your models here.
class Manual(models.Model):
    name: str = models.CharField(max_length=100)
    file_path = models.FileField(upload_to='documents/manuals/')
    language: str = models.CharField(max_length=2, choices=languages)
    category: str = models.CharField(default='MON', max_length=3, choices=categories)
    image = models.ImageField(upload_to='documents/manuals/thumbs/')

    def __str__(self):
        return self.name
