from django.db import models

# Create your models here.
class student(models.Model):
    rollnum=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    add=models.CharField(max_length=100)
    per=models.FloatField()
    def __str__(self):
        return self.name

class emp(models.Model):
    eid=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    eadd=models.CharField(max_length=100)
    def __str__(self):
        return self.ename
