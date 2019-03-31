
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Record(models.Model):
    book_name = models.CharField(max_length = 200)
    date = models.DateField(default = timezone.now) 
    time = models.IntegerField(default = 1)
    author = models.ForeignKey(User,
                                on_delete = models.CASCADE,
                                related_name = 'reading_record')
    startpage =  models.IntegerField(default = 1)
    endpage = models.IntegerField(default = 1)
    words = models.IntegerField()
    readingnotes = models.TextField()

    