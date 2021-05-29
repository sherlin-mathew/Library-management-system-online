from django.db import models

# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    code = models.CharField(max_length=20,null=True)
    verified = models.CharField(max_length=20,null=True)
    
    class Meta:
        db_table = "User table"


