from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tasks(models.Model):
    task=models.CharField(max_length=300)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)
    checked = models.BooleanField(default=False)
    def __str__(self):
        return self.task
    