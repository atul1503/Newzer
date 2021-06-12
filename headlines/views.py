from django.shortcuts import render
from HelloDjango.utility import *
import json
import requests
from HelloDjango.views import api_key

# Create your views here.



def general(request):
    '''
    Get top headlines.
    '''
    category=request.GET.get('categ',0)
    if not category:
        category='general'
    url=url_maker('https://newsapi.org/v2/top-headlines?',
    [
     ['category',category],
     ['page',1],
     ['apiKey',api_key],
    ])
    r=requests.get(url)
    obj=json.loads(r.text)
    return render(request,'headlines.html',{'articles':obj['articles'],'page':1})
    
def gen_prev(request):
    '''
    headlines form back view
    '''
    category=request.GET.get('categ',0)
    if not category:
        category='general'
    page=int(request.GET.get('pageno'))
    url=url_maker('https://newsapi.org/v2/top-headlines?',
    [
     ['category','general'],
     ['page',page-1],
     ['apiKey',api_key],
    ])
    r=requests.get(url)
    obj=json.loads(r.text)
    return render(request,'headlines.html',{'articles':obj['articles'],'page':page-1})
    
def gen_next(request):
    '''
    headlines form front view
    '''
    category=request.GET.get('categ',0)
    if not category:
        category='general'
    page=int(request.GET.get('pageno'))
    url=url_maker('https://newsapi.org/v2/top-headlines?',
    [
     ['category','general'],
     ['page',page+1],
     ['apiKey',api_key],
    ])
    r=requests.get(url)
    obj=json.loads(r.text)
    return render(request,'headlines.html',{'articles':obj['articles'],'page':page+1})
    
    
    
    
    
    
    
    
    
