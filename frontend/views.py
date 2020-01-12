from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from api.models import snips
import requests
import json

@csrf_exempt
def home(request):
   if request.method == 'GET':
      resp = requests.get("http://"+request.get_host()+"/api/snips")
      slist = json.loads(resp.text)
      return render(request, 'index.html', {"slist":slist})
   elif request.method == 'POST':
      message = request.POST.get('text')
      return HttpResponse(str(message))

