from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
# Create your models here.

class post(models .Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    Author = get_user_model()
    Created_date = models.DateTimeField(default=datetime.today)
    Published_date = models.DateTimeField(default=datetime.today)



