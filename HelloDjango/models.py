from django import forms

class preference(forms.Form):
    body=forms.CharField(label='Search in article body',max_length=30,required=False)
    title=forms.CharField(label='Search in article title',max_length=30,required=False)
    max_articles=forms.IntegerField(label='Number of Articles',initial=10)
    

    
    
    