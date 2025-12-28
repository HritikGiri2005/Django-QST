from django.db import models

# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    about = models.TextField()
    gender = models.CharField(max_length=100)
    skills = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profiles/')
    dob = models.DateField()

    def __str__(self):
        return self.username
    

