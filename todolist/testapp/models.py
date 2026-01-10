from django.db import models

# Create your models here.
class todo(models.Model):
    task_name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
