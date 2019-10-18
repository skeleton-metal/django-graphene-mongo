from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from djongo import models as moD


class User(AbstractUser):
    _id = moD.ObjectIdField()
    email = models.EmailField(blank=True, unique=True)
    phone = models.TextField()
    avatar = models.ImageField(null=True, upload_to="avatars")
