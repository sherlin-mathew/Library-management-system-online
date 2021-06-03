from django.db import models

# Create your models here.
class Administrator(models.Model):
    email = models.CharField(max_length=50)
    password =  models.CharField(max_length=100)
    class Meta:
        db_table = "Administrator"


class bookdetails(models.Model):
	bookname = models.CharField(max_length=100,null=True)
	author = models.CharField(max_length=100,null=True)
	year = models.CharField(max_length=1000,null=True)
	publisher = models.CharField(max_length=200,null=True)
	pdf = models.FileField()
	class Meta:
		db_table = "Book Table"
    


        