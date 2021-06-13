from django import forms

class preference(forms.Form):
    
    def __init__(self):
        self.body=forms.CharField(label='Search in article body',initial='Bollywood',max_length=30,required=False)
        self.title=forms.CharField(label='Search in article title',max_length=30,required=False)
    

    
    
    