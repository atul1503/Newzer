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
    if 'next' in request.GET:
        return gen_next(request)
    elif 'prev' in request.GET:
        return gen_prev(request)
    category=request.GET.get('categ',0)
    if not category:
        category='general'
    url=url_maker('https://newsapi.org/v2/top-headlines?',
    [
     ['category',category],
     ['page',1],
     ['apiKey',api_key],
    ])
    request.session['pref']=request.GET
    request.session['page']=1
    r=requests.get(url)
    obj=json.loads(r.text)
    return render(request,'headlines.html',{'articles':obj['articles'],'page':1})
    
def gen_prev(request):
    '''
    headlines form back view
    '''
    category=request.session['pref']['categ']
    page=int(request.session['page'])-1
    if not category:
        category='general'
    url=url_maker('https://newsapi.org/v2/top-headlines?',
    [
     ['category',category],
     ['page',page],
     ['apiKey',api_key],
    ])
    r=requests.get(url)
    obj=json.loads(r.text)
    request.session['page']=page
    return render(request,'headlines.html',{'articles':obj['articles'],'page':page-1})
    
def gen_next(request):
    '''
    headlines form front view
    '''
    category=request.session['pref']['categ']
    if not category:
        category='general'
    page=int(request.session['page'])+1
    url=url_maker('https://newsapi.org/v2/top-headlines?',
    [
     ['category',category],
     ['page',page],
     ['apiKey',api_key],
    ])
    r=requests.get(url)
    obj=json.loads(r.text)
    request.session['page']=page
    return render(request,'headlines.html',{'articles':obj['articles'],'page':page+1})
    
    
    
    
    
    
    
    
    
