from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import json
from rest_serv.models import Event
from rest_serv.serializers import EventSerializer
from django.views.decorators.http import require_GET

@require_GET	
def EventView(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return JsonResponse(serializer.data, safe=False)
