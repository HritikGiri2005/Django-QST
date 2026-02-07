from django.db import models

# Create your models here.
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class AadharCard(models.Model):
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        related_name="aadhar"   # 👈 reverse relation name
    )
    number = models.IntegerField()

    def __str__(self):
        return str(self.number)




class Father(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Children(models.Model):
    father = models.ForeignKey(Father,on_delete=models.CASCADE)
    child_name = models.CharField(max_length=50)

    def __str__(self):
        return self.child_name
    
