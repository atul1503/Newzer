from django.http import HttpResponse
import requests as r
from django.shortcuts import render
import json
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
    
def news(request):
    '''
    intitialization page for /news
    '''
    q=preference()
    q.max_articles=20
    q.body='Bollywood'
    q.title=''
    article_list=[]
    run=1
    page=1
    arts=q.max_articles
    while run: 
        url=url_maker(
        queryParamNames['domain'],
        [
            ['q',q.body],
            ['page',page],
            ['apiKey',api_key],
            ['qInTitle',q.title]
        ]
        )
        json_str=r.get(url).text
        json_obj=json.loads(json_str)
        i=0
        while i<len(json_obj['articles']):
            article_list.append(json_obj['articles'][i])
            arts=arts-1
            if arts<1:
                run=0
                break
            i=i+1
        page=page+1
                
    article_list.sort(reverse=True,key=lambda x:x["publishedAt"])
    for i in article_list:
        i["publishedAt"]=parse_date(i["publishedAt"])
    context={
    'articles':article_list,
    'form':q
    }
    return render(
    request,'news.html',context
    )
    
    
def newsQ(request):
    '''
    page after query request 
    
    '''
    q=request.GET
    article_list=[]
    run=1
    page=1
    arts=int(q['max_articles'])
    while run: 
        url=url_maker(
        queryParamNames['domain'],
        [
            ['q',q['body']],
            ['page',page],
            ['apiKey',api_key],
            ['qInTitle',q['title']]
        ]
        )
        json_str=r.get(url).text
        json_obj=json.loads(json_str)
        i=0
        while i<len(json_obj['articles']):
            article_list.append(json_obj['articles'][i])
            arts=arts-1
            if arts<1:
                run=0
                break
            i=i+1
        page=page+1
                
    article_list.sort(reverse=True,key=lambda x:x["publishedAt"])
    for i in article_list:
        i["publishedAt"]=parse_date(i["publishedAt"])
    context={
    'articles':article_list
    }
    return render(
    request,'news.html',context
    )    

    
