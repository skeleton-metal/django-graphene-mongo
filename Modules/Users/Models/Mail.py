from django.db import models
from djongo import models as moD


# Create your models here.
class BaseManager(models.Manager):
    pass


class Mail(models.Model):
    _id = moD.ObjectIdField()
    sender = models.TextField()
    to = models.TextField()
    subject = models.TextField()
    message = models.TextField()
    date = models.DateTimeField()
    objects = BaseManager()
