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
    if 'next' in request.GET:
        return gen_next(request)
    elif 'prev' in request.GET:
        return gen_prev(request)
    url=url_maker('https://newsapi.org/v2/top-headlines?',
    [
     ['category','general'],
     ['page',1],
     ['apiKey',api_key],
    ])
    r=requests.get(url)
    obj=json.loads(r.text)
    return render(request,'headlines.html',{'articles':obj['articles'],'page':1})
    
def gen_prev(request):
    '''
    general form back view
    '''
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
    general form front view
    '''
    print(request.GET)
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
    
    
    
    
    
    
    
    
    
