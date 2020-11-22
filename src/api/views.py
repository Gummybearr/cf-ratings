import requests, json
from django.http import HttpResponse

from .utils import crawl_data, generate_card

# Create your views here.
def user(request):
    if request.method != 'GET':
        return HttpResponse(status=400)
    
    try:
        handle = request.GET['handle']
        user_data = crawl_data(handle)
        response = HttpResponse(content=str(generate_card(user_data)))
        response['Content-Type'] = 'image/svg+xml'
        return response

    except:
        return HttpResponse(status=400)
