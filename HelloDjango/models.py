from django.db import models

class preference(models.Model):
    body=models.CharField(default='Choksi',label='Search in article body',max_length=30)
    title=models.CharField(default='',label='Search in article title',max_length=30)
    max_articles=models.IntegerField(default=15,label='Number of Articles')
    

    
    
    