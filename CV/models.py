from django.db import models

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=500, null=True)
    #picture = models.ImageField()
    profession = models.CharField(max_length=500, null=True)
    obtained_ranks = models.IntegerField(null=True)
    max_ranks = models.IntegerField(null=True)
    user_id = models.CharField(max_length=500, null=True)
    email = models.EmailField(max_length=500, null=True)
    phone = models.IntegerField(null=True)
    skills = models.TextField(null=True)
    work_links = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
