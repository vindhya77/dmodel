from django.db import models

# Create your models here.
class student(models.Model):
    sid=models.IntegerField()
    sname=models.CharField(max_length=100)
    sadd=models.CharField(max_length=100)
    sph=models.IntegerField()
    def __str__(self):
        return self.sname
    def data(self):
        return self.sadd
class formModel(models.Model):
    name=models.CharField(max_length=100)
    body=models.TextField()
    def __str__(self):
        return self.name
