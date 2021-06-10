from django.db import models

class preference(models.Model):
    priority=models.CharField(default='q',max_length=30)
    page=models.IntegerField(default=1)
    count=models.IntegerField(default=20)
    