from datetime import timedelta

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.contenttypes.fields import GenericRelation
from django.db.models import Max, Min, Count, F, Value, CharField, Prefetch
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


from forum.core.models import TimeStampedModel


class User(AbstractUser):
    GENDER_OPTIONS = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    gender = models.CharField(
        max_length=20, choices=GENDER_OPTIONS, blank=True)
    signature = models.TextField(max_length=127, blank=True)
    location = models.CharField(max_length=32, blank=True)
    website = models.URLField(max_length=50, blank=True)
    followers = models.ManyToManyField(
        'self', related_name='following', symmetrical=False, blank=True
    )
    # following = models.ManyToManyField(
    #     'self', related_name='followers',  blank=True
    # )
    last_seen = models.DateTimeField(default=timezone.now)
    email_confirmed = models.BooleanField(default=False)
    avatar_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username

    def is_online(self):
        timeout = 5 * 60  # 5 minutes.
        return timezone.now() < self.last_seen + timedelta(seconds=timeout)

    def is_owner(self, user):
        return self == user

    def is_required_filter_owner(self, user, filter_str):
        owner_only = ['me', 'following', 'new']
        if filter_str not in owner_only:
            return True
        return self.is_owner(user)

    def get_avatar_url(self):
        return self.avatar_url

    def update_notification_info(self, request, url, count):
        request.user.notif_url = url
        request.user.notif_count = count

    def toggle_followers(self, follower):
        if follower not in self.followers.all():
            self.followers.add(follower)
        else:
            self.followers.remove(follower)

    def get_absolute_url(self):
        return reverse('accounts:user_stats', kwargs={'username': self.username})

    def get_user_follow_url(self):
        return reverse('accounts:user_follow', kwargs={'username': self.username})

    def get_userprofile_update_url(self):
        return reverse(
            'accounts:user_edit', kwargs={'username': self.username}
        )

    def get_login_url(self):
        return reverse('accounts:login')
