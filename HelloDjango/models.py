from django import forms

class preference(forms.Form):
    body=forms.CharField(label='Search in article body',initial='Choksi',max_length=30)
    title=forms.CharField(label='Search in article title',initial='the',max_length=30)
    max_articles=forms.IntegerField(label='Number of Articles',initial=10)
    

    
    
    