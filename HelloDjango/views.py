from django.http import HttpResponse
import requests as r
from django.shortcuts import render
import json
import jsonpickle
from .utility import parse_date,url_maker
from .models import preference


queryParamNames={
    'title':'qInTitle=',
    'body':'q=',
    'key':'apiKey',
    'domain':'https://newsapi.org/v2/everything?',
    'page':'page'
}
api_key='587ef66569534cc19dd19a5af6e14a58'


def hello(request):
    return HttpResponse("<strong>Hello Django</strong>")
    
def homepage(request):
    return HttpResponse("<center>Welcome to my first django project</center>")
    
    
    
def newsQ(request):
    '''
    page after query request 
    
    '''
    if 'body' in request.GET:
        return prefReq(request)
    elif 'next' in request.GET:
        return nextPage(request)
    elif 'prev' in request.GET:
        return prevPage(request)
    else:
        return initRequest(request)
        
def prefReq(request):
    pref=preference(request.GET)
    page=1
    q=request.GET
    article_list=[]
    url=url_maker(queryParamNames['domain'],
    [
        ['q',q.get('body')],
        ['qInTitle',q.get('title')],
        ['page',page],
        ['apiKey',api_key]
    ])
    json_str=r.get(url).text
    json_obj=json.loads(json_str)
    if json_obj['status']=='error':
        return render(request,'news.html',{})
    article_list=article_list+json_obj['articles']
    article_list.sort(reverse=True,key=lambda x:x["publishedAt"])
    for i in article_list:
        i["publishedAt"]=parse_date(i["publishedAt"])
    request.session['pref']=jsonpickle.encode(q)
    request.session['page']=page
    context={
    'articles':article_list,
    'form':pref
    }
    return render(request,'news.html',context)


def nextPage(request):
    query=jsonpickle.decode(request.session['pref'])
    pref=preference(query)
    page=int(request.session['page'])+1
    article_list=[]
    q=query
    url=url_maker(queryParamNames['domain'],
    [
       ['q',q.get('body')],
        ['qInTitle',q.get('title')],
        ['page',page],
        ['apiKey',api_key]
    ])
    json_str=r.get(url).text
    json_obj=json.loads(json_str)
    if json_obj['status']=='error':
        return render(request,'news.html',{})
    article_list=article_list+json_obj['articles']
    article_list.sort(reverse=True,key=lambda x:x["publishedAt"])
    for i in article_list:
        i["publishedAt"]=parse_date(i["publishedAt"])
    request.session['pref']=jsonpickle.encode(pref)
    request.session['page']=page
    context={
    'articles':article_list,
    'form':pref
    }
    return render(request,'news.html',context)
    
    
def prevPage(request):
    pref=jsonpickle.decode(request.session['pref'])
    page=int(request.session['page'])-1
    article_list=[]
    q=request.session['pref']
    url=url_maker(queryParamNames['domain'],
    [
        ['q',q.get('body')],
        ['qInTitle',q.get('title')],
        ['page',page],
        ['apiKey',api_key]
    ])
    json_str=r.get(url).text
    json_obj=json.loads(json_str)
    if json_obj['status']=='error':
        return render(request,'news.html',{})
    article_list=article_list+json_obj['articles']
    article_list.sort(reverse=True,key=lambda x:x["publishedAt"])
    for i in article_list:
        i["publishedAt"]=parse_date(i["publishedAt"])
    request.session['pref']=jsonpickle.encode(pref)
    request.session['page']=page
    context={
    'articles':article_list,
    'form':pref
    }
    return render(request,'news.html',context)
    
    
def initRequest(request):
    pref=preference()
    pref.body="Bollywood"
    pref.title=""
    page=1
    article_list=[]
    url=url_maker(queryParamNames['domain'],
    [
        ['q',pref.body],
        ['qInTitle',pref.title],
        ['page',page],
        ['apiKey',api_key]
    ])
    json_str=r.get(url).text
    json_obj=json.loads(json_str)
    if json_obj['status']=='error':
        return render(request,'news.html',{})
    article_list=article_list+json_obj['articles']
    article_list.sort(reverse=True,key=lambda x:x["publishedAt"])
    for i in article_list:
        i["publishedAt"]=parse_date(i["publishedAt"])
    request.session['pref']=jsonpickle.encode({'body':'Bollywood','title':''})
    request.session['page']=page
    context={
    'articles':article_list,
    'form':pref
    }
    return render(request,'news.html',context)