from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

from .serializers import RegisterSerializer, JobsSerializer, ApplicationSerializer

from .models import Job, Application

@api_view(['GET'])
def hello(req):
    print(req)
    return Response({'message': 'Hi Django'})

@api_view(['POST'])
def registerUser(req):
    serializer = RegisterSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save() # Save user
        return Response({'message': 'User register done!'}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def basicLogin(req):
    username = req.data.get('username')
    password = req.data.get('password')

    try:
        user = User.objects.get(username=username, password=password)
        return Response({ 'user_id': user.id, 'username': user.username, 'message': 'Login done!'}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'message': 'Invalid datas!'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def jobList(req):
    jobs = Job.objects.all()
    serializer = JobsSerializer(jobs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def applyJob(req):
    serializer = ApplicationSerializer(data=req.data)
    # check application  exists
    job_id = req.data.get("job")
    applicant_id = req.data.get("applicant")
    if Application.objects.filter(job_id=job_id, applicant_id=applicant_id).exists():
        return Response({'message': 'Already applied!'}, status=status.HTTP_400_BAD_REQUEST)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Application submitted done!'}, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


