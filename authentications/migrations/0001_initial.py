# Generated by Django 4.0.6 on 2022-10-15 19:46

import authentications.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=authentications.models.image_path)),
                ('motto', models.CharField(blank=True, help_text='Your warcry!', max_length=100, null=True)),
                ('role', models.CharField(choices=[('NEGM', 'New GM'), ('WBGM', 'World Builder GM'), ('MMGM', 'Master Mind GM'), ('GLGM', 'Godlike GM')], default='NEGM', max_length=4)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name=django.utils.timezone.now)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('type', models.CharField(choices=[('FC', 'Forum Comment'), ('NL', 'News Letter')], max_length=2)),
                ('message', models.TextField()),
                ('seen', models.BooleanField(default=False)),
                ('to_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentications.profile')),
            ],
        ),
    ]
