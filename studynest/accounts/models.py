from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.







class Customer(models.Model):
    # user blank, so customer doesnt have a user attached
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="profile.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name or "No name"