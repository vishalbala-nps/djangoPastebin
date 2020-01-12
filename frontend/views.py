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
      title = request.POST.get('title')
      message = request.POST.get('text')
      resp = requests.post("http://"+request.get_host()+"/api/snips/", {"title": title,"text": message})
      sid = json.loads(resp.text)["message"]
      return HttpResponse(str(sid))

def viewsnip(request,id):

   resp = requests.get("http://"+request.get_host()+"/api/snip/"+id)
   slist = json.loads(resp.text)
   return render(request, 'display_paste.html', {"title":slist['title'],"text":slist['text'],"pubDate":slist['pubDate']})

