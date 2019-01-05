from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    email = models.EmailField(('email address'), unique=True)
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