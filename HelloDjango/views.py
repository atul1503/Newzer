from django.http import HttpResponse
import requests as r
import json


def hello(request):
    return HttpResponse("<strong>Hello Django</strong>")
    
def homepage(request):
    return HttpResponse("<center>Welcome to my first django project</center>")
    
def news(request):
    url="https://newsapi.org/v2/everything?q=*&apiKey=587ef66569534cc19dd19a5af6e14a58"
    obj=json.loads(r.get(url).text)
    articles=
    for i in obj["articles"]:
        
    responseHTML="
    <html>
    

    </html>
    "
    return HttpResponse(responseHTML)