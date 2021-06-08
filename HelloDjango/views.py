from django.http import HttpResponse
import requests as r
from django.shortcuts import render
import json
from .utility import parse_date


queryParamNames={
    'title':'qInTitle=',
    'body':'q=',
    'key':'apiKey=',
    'domain':'https://newsapi.org/v2/everything?'
}

def hello(request):
    return HttpResponse("<strong>Hello Django</strong>")
    
def homepage(request):
    return HttpResponse("<center>Welcome to my first django project</center>")
    
def news(request):
    api_key='587ef66569534cc19dd19a5af6e14a58'
    search_query="America"
    url=queryParamNames['domain']+queryParamNames['body']+search_query+'&'+queryParamNames['key']+api_key
    json_str=r.get(url).text
    json_obj=json.loads(json_str)
    if json_obj['status']=='error':
        return HttpResponse('Errors are part of life.Dont be disheartened')
    json_obj['articles'].sort(reverse=True,key=lambda x:x["publishedAt"])
    for i in json_obj['articles']:
        i["publishedAt"]=parse_date(i["publishedAt"])
    context={
    'articles':json_obj['articles']
    }
    return render(
    request,'news.html',context
    )
    
def newsQ(request):
    api_key='587ef66569534cc19dd19a5af6e14a58'
    search_query=request.GET['q'].replace(' ','+')
    priority=request.GET['priority']+'='
    url=queryParamNames['domain']+priority+search_query+"&apiKey="+api_key
    json_str=r.get(url).text
    json_obj=json.loads(json_str)
    if json_obj['status']=='error':
        return HttpResponse('Errors are part of life.Dont be disheartened')
    json_obj['articles'].sort(reverse=True,key=lambda x:x["publishedAt"])
    for i in json_obj['articles']:
        i["publishedAt"]=parse_date(i["publishedAt"])
    context={
    'articles':json_obj['articles']
    }
    return render(
    request,'news.html',context
    )
