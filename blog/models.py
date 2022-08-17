from django.db import models
from django.utils import timezone


# Create your models here.

class Post(models.Model) :
    STATUS_CHOICES = (
        ('d','Draft'),
        ('p','Published')
    )
    title = models.CharField(max_length = 20)
    slug = models.SlugField( max_length = 15 , unique=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to = "image/" )
    publish = models.DateTimeField(default = timezone.now)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length = 1 , choices= STATUS_CHOICES)


    def __str__(self):
        return self.title