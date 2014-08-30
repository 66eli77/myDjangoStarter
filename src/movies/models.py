from django.db import models
from django.utils import simplejson

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=220, null=True, blank=True)
    year = models.CharField(max_length=220, null=True, blank=True)
    movie_id = models.CharField(max_length=120, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __unicode__(self):
        return self.title
