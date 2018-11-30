from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    type = models.CharField(max_length=100)
    # userType = models.CharField(max_length=)


