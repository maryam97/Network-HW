from django.db import models
from user.models import User

# Create your models here.


class Receipt(models.Model):
    rec = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
