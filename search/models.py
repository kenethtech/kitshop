from django.db import models
from django.contrib.auth.models import User

class SearchTerm(models.Model):
    word = models.CharField(max_length=50)
    search_date = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    tracking_id = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.word


# Create your models here.
