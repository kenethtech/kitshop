from django.db import models
from django.contrib.auth.models import User
from checkout.models import BaseOrderInfo



class UserProfile(BaseOrderInfo):
    user = models.OneToOneField(User, unique=True, on_delete= models.CASCADE, related_name='profile')

    def __str__(self):
        return 'User Profile for: ' + self.user.username
# Create your models here.
