from django.http import HttpResponse

def hello(request):
    return HttpResponse("<strong>Hello Django</strong>")
    
def homepage(request):
    return HttpResponse("<center>Welcome to my first django project</center>")
    
def vagina(request):
    return HttpResponse("Not funny")