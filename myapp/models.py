from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # add additional fields in here
    email= models.EmailField(unique=True , max_length=254, null=False, blank=False)
    name=models.CharField(max_length=50, default='', blank=True)
    username=models.CharField(max_length=50, unique=False, null=True, blank= True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    def __str__(self):
        return self.email 

    


