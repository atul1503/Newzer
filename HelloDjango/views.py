from django.http import HttpResponse
import requests as r
from django.template import loader
import json


def hello(request):
    return HttpResponse("<strong>Hello Django</strong>")
    
def homepage(request):
    return HttpResponse("<center>Welcome to my first django project</center>")
    
def news(request):
    api_key='587ef66569534cc19dd19a5af6e14a58'
    search_query='money'
    url="https://newsapi.org/v2/everything?q="+search_query+"&apiKey="+api_key
    json_str=r.get(url).text
    json_obj=json.loads(json_str)
    template_obj=loader.get_template('news.html')
    context={
    'articles':json_obj['articles']
    }
    return HttpResponse(
        template_obj.render(context)
        )