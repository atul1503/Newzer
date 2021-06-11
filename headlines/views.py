from django.shortcuts import render
from HelloDjango.utility import *
import json
import requests

# Create your views here.

def general(request):
    '''
    Get initial News from general category.
    '''
    url=url_maker('https://newsapi.org/v2/top-headlines?',{
    'category':'general'
    'page':1
    }
    r=requests.get(url)
    obj=json.loads(r.text)
    return render(request,'headlines.html',{'articles':json['articles'],'page':1}
    
    
    
    
    
    
    
    
