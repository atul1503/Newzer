from django.http import HttpResponse
import requests as r
from django.shortcuts import render
import json
from .utility import parse_date


def hello(request):
    return HttpResponse("<strong>Hello Django</strong>")
    
def homepage(request):
    return HttpResponse("<center>Welcome to my first django project</center>")
    
def news(request):
    api_key='587ef66569534cc19dd19a5af6e14a58'
    search_query='Facebook'
    url="https://newsapi.org/v2/everything?q="+search_query+"&apiKey="+api_key
    json_str=r.get(url).text
    json_obj=json.loads(json_str)
    for i in json_obj['articles']:
        i["publishedAt"]=parse_date(i["publishedAt"])
    json_obj['articles'].sort(reverse=True,key=lambda x:x["publishedAt"])
    context={
    'articles':json_obj['articles']
    }
    return render(
    request,'news.html',context
    )