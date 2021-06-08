from django.http import HttpResponse
import requests as r
from django.shortcuts import render
import json
from .utility import parse_date


queryParamNames={
    'title':'qInTitle=',
    'body':'q=',
    'key':'apiKey=',
    'domain':'https://newsapi.org/v2/everything?',
    'page':'page='
}
api_key='587ef66569534cc19dd19a5af6e14a58'

def hello(request):
    return HttpResponse("<strong>Hello Django</strong>")
    
def homepage(request):
    return HttpResponse("<center>Welcome to my first django project</center>")
    
def news(request):
    search_query="America"
    priority='q='
    article_list=[]
    page=1
    while 1:
        url=queryParamNames['domain']+queryParamNames['body']+search_query+"&apiKey="+api_key+'&'+queryParamNames['page']+str(page)
        json_str=r.get(url).text
        json_obj=json.loads(json_str)
        if json_obj['status']=='error':
            break
        article_list=article_list+json_obj['articles']
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
    
    
def newsQ(request):
    search_query=request.GET['q'].replace(' ',',')
    priority=(request.GET['priority'])+'='
    article_list=[]
    page=1
    while 1:
        url=queryParamNames['domain']+priority+search_query+"&apiKey="+api_key+'&'+queryParamNames['page']+str(page)
        json_str=r.get(url).text
        json_obj=json.loads(json_str)
        if json_obj['status']=='error':
            break
        article_list=article_list+json_obj['articles']
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
        

    
