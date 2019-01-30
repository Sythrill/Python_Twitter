from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    email = models.EmailField(('email address'), unique=True)
    image = models.FileField(upload_to="profile_img", blank=True)
    twitter = models.URLField(max_length=256, null=True, blank=True)
    facebook = models.URLField(max_length=256, null=True, blank=True)
    google = models.URLField(max_length=256, null=True, blank=True)
    behance = models.URLField(max_length=256, null=True, blank=True)
    REQUIRED_FIELDS = ["username"]


class Message(models.Model):
    content = models.CharField(max_length=140, null=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.CharField(max_length=60, null=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)


class PersonalMessage(models.Model):
    content = models.CharField(max_length=140, null=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="from_user")
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="to_user")


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE, default="1")
    created = models.DateTimeField(auto_now_add=True)
