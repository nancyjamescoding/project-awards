from django.db import models
from time import timezone
from django.utils import timezone

# Create your models here.

class Project(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    title = models.TextField(null=False,max_length=140, default='')
    image = models.ImageField(blank=True, null=True)
    caption = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.caption