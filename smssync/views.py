from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Gateway, Task
from .serializers import TaskSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def task(request):
	if request.method == 'GET':
		task = request.GET.get('task')
		secret = request.GET.get('secret')
		if task != 'send': return Response({'task':'task needed'}, status=status.HTTP_400_BAD_REQUEST)
		try:
			gateway = Gateway.objects.get(secret=secret)
		except Gateway.DoesNotExist:
			gateway = None

		if gateway is None: return Response({}, status=status.HTTP_401_UNAUTHORIZED)
		tasks = Task.objects.filter(gateway=gateway)
		serializer = TaskSerializer(tasks, many=True)
		for task in serializer.data:
			task['uuid'] = task['id']
		# serializer.data['uuid'] = 'jayvee'
		payload = {
			'payload':{
				'task' : 'send',
				'secret' : gateway.secret,
				'messages': serializer.data
			}
		}
		print(serializer.data)
		return Response(payload, status=status.HTTP_200_OK)
	p = {
		"payload":{
			"success":True,
			"error": None
		}
	}
	return Response(p, status=status.HTTP_200_OK)
			



