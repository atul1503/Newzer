from django.shortcuts import render
from HelloDjango.utility import *
import json
import requests
from HelloDjango.views import api_key

# Create your views here.



def general(request):
    '''
    Get initial News from general category.
    '''
    url=url_maker('https://newsapi.org/v2/top-headlines?',
    [
     ['category','general'],
     ['page',1],
     ['apiKey',api_key],
    ])
    r=requests.get(url)
    obj=json.loads(r.text)
    print(obj['articles'][0])
    return render(request,'headlines.html',{'articles':obj['articles'],'page':1})
    
def gen_prev(request)
    
    
    
    
    
    
    
    
