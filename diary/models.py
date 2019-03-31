from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Diary(models.Model):
    Status_Choices = (
        ('draft','Draft' ),
        ('published','Published'),
    )

    title = models.CharField(max_length = 250)
    author = models.ForeignKey(User,
                                on_delete = models.CASCADE,
                                related_name = 'DiaryWriter')
    body = models.TextField()
    publish = models.DateTimeField(default = timezone.now)
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now= True)

