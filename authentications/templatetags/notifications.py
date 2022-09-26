from django import template
from django.db.models import Count
from authentications.models import Profile, Notification

register = template.Library()


@register.filter
def get_notifications(user):
    notifications = Notification.objects.filter(to_profile=Profile.objects.get(user=user), seen=False)
    return notifications.count()
