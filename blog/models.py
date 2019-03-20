from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    Status_Choices = (
        ('draft','Draft' ),
        ('published','Published'),
    )

    title = models.CharField(max_length = 250)
    slug = models.SlugField(max_length = 250,unique_for_date = 'published')
    ##grammer may have changed for field


    author = models.ForeignKey(User,
                                on_delete = models.CASCADE,
                                related_name = 'blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default = timezone.now)
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now= True)
    status = models.CharField(max_length = 10,
                            choices = Status_Choices,
                            default = 'draft'
                            )

    class Meta:
        ordering = ('-publish',)
        def __str__(self):
            return self.title