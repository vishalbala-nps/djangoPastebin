from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.models import snips
from datetime import *
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
      rjson = request.data
      now = date.today()
      try:
         new_snip = snips(title=rjson["title"], text=rjson["text"], pubDate=str(now))
      except:
         return Response({"message":"Invalid Input!"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
      new_snip.save()

      return Response({'message': str(new_snip.id)})   