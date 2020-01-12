from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import snips

@api_view(['GET'])
def home(request, format=None):
   return Response({
      'message': 'Hello World!!!',
   })

@api_view(['GET','POST'])
def api_snip(request, format=None):

   if request.method == 'GET':
      slist = []
      all_snips = snips.objects.all()
      for i in all_snips:
         slist.append({'id':i.id,'title':i.title,'publishedOn':i.pubDate})
      return Response(slist)
   elif request.method == 'POST':
      return Response({
         'message': 'Post snips',
      })   