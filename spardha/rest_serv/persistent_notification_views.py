from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import json
from rest_serv.models import PersistentNotification
from rest_serv.serializers import PersistentNotificationSerializer

def persistent_notification_list(request):
    if request.method == 'GET':
        persistent_notifications = PersistentNotification.objects.all()
        serializer = PersistentNotificationSerializer(persistent_notifications, many=True)
        return JsonResponse(serializer.data, safe=False)
    return HttpResponse(json.dumps({"error":"true","detail":"bad_request"}), status=400, content_type="application/json")
