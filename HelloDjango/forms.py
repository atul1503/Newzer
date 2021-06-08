from django import forms

class NewsQuery(forms.Form):
    query=forms.CharField(label='newsQ')