from django.db import models
from time import timezone
from django.utils import timezone

# Create your models here.

class Project(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    caption = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.caption