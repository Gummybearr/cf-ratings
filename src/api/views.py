import requests, json
from django.http import HttpResponse

from .utils import crawl_data

# Create your views here.
def user(request):
    if request.method != 'GET':
        return HttpResponse(status=400)
    
    try:
        handle = request.GET['handle']
        user_data = crawl_data(handle)
        print(user_data)
        response = HttpResponse(content=str(user_data))
        response = HttpResponse(content="<div style='background-color: black'>asdfasdf</div>")
        return response

    except:
        return HttpResponse(status=400)