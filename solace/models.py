from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


# Create your models here.
class CustomUserManager(UserManager):
    def get_by_natural_key(self, username):
        return self.get(username__iexact=username)


class User(AbstractUser):
    pfp = models.FileField(blank="True", default="default.png")
    status = models.CharField(blank="True", max_length=32)
    friends = models.ManyToManyField("self")
    friend_requests = models.ManyToManyField("self")
    objects = CustomUserManager()
    def send_friend_request(self, to_user):
        # Add the 'to_user' to this user's friend_requests
        self.friend_requests.add(to_user)
    def addFriend(self, friend):
        # Add the 'to_user' to this user's friend_requests
        self.friends.add(friend)


class JournalEntry(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    created_at = models.DateTimeField(auto_now_add=True)


class Pet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    name = models.CharField(default="Arthur", max_length=32)
    mood = models.IntegerField(default=5)
    sprite = models.CharField(max_length=64)


class Record(models.Model):
    mood = models.IntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)
