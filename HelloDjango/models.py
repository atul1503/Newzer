from django.db import models

class preference(models.Model):
    body=models.CharField(default='Choksi',max_length=30)
    title=models.CharField(default='',max_length=30)
    page=models.IntegerField(default=1)
    max_articles=models.IntegerField(default=15)
    

    
    
    