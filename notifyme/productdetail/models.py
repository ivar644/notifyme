from django.db import models
from django.contrib.auth.models import auth,User

# Create your models here.
class productdetails(models.Model):
    name=models.CharField(max_length=200)
    userid=models.ForeignKey(User, on_delete = models.CASCADE)
    url=models.CharField(max_length=1000)
    email=models.EmailField()
    price=models.IntegerField()