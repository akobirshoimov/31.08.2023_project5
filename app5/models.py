from django.db import models

# Create your models here.
class Bozorlar(models.Model):
    name = models.CharField(max_length=90,default= 'TTZ bozori')
    build_in = models.DateField(default = '12-02-2012')

    def __str__(self) -> str:
        return self.name

class OnlineDokonlar(models.Model):
    name = models.CharField(max_length=100,default = ' ')
    who_created = models.CharField(max_length=100, default  = 'nomalum ')
    when_created = models.DateField(default = '10-02-2020')
     
    def __str__(self) -> str:
        return self.name 
    
