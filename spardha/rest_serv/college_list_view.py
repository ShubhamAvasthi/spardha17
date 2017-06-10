from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_serv.models import College
from rest_serv.serializers import CollegeSerializer

def college_list(request):
    if request.method == 'GET':
        colleges = College.objects.all()
        serializer = CollegeSerializer(colleges, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        #data = JSONParser().parse(request)
        serializer = CollegeSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
