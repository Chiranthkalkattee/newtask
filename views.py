from django.shortcuts import render
from .models import Candidate_details,skill_details
from .serializers import CandidateSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

@csrf_exempt
def Candidate_list(request):
    if request.method == 'GET':
        candidate = Candidate_details.objects.all()
        serializer = CandidateSerializer(candidate,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method == 'POST':

        serializer = CandidateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
