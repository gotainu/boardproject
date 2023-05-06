from django.db import models

# Create your models here.
class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    snsimage = models.ImageField(null=True,blank=True, upload_to='',default=None)
    good = models.IntegerField(null=True,blank=True, default=0)
    read = models.IntegerField(null=True,blank=True, default=1)
    readtext = models.TextField(null=True,blank=True, default='a')