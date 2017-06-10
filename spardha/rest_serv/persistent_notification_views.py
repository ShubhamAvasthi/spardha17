from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import json
from rest_serv.models import PersistentNotification
from rest_serv.serializers import PersistentNotificationSerializer
from django.views.decorators.http import require_GET

@require_GET
def persistent_notification_list(request):
    if request.method == 'GET':
        persistent_notifications = PersistentNotification.objects.all()
        serializer = PersistentNotificationSerializer(persistent_notifications, many=True)
        return JsonResponse(serializer.data, safe=False)
