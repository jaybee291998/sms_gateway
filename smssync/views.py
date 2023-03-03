from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Gateway, Task
from .serializers import TaskSerializer, TaskPostSerializer

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
			del task['id']
			del task['gateway']
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
	print(request.data)
	p = {
		"payload":{
			"success":True,
			"error": None
		}
	}
	return Response(p, status=status.HTTP_200_OK)
			

@api_view(['POST'])
def post_task(request):
	serializer = TaskPostSerializer(data=request.data)
	if not serializer.is_valid(): return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	api_key = request.data['api_key']
	to = request.data['to']
	message = request.data['message']
	try:
		gateway = Gateway.objects.get(api_key=api_key)
	except Gateway.DoesNotExist:
		gateway = None

	if gateway is None: return Response({"api_key":"provide a valid api key"}, status=status.HTTP_401_UNAUTHORIZED)

	# new_task = Task(gateway=gateway, to=to, message=message)
	new_task = {
		'gateway':gateway.id,
		'to':to,
		'message': message
	}
	task_serializer = TaskSerializer(data=new_task)
	if task_serializer.is_valid(): task_serializer.save()

	return Response(task_serializer.data, status=status.HTTP_200_OK)