from django.shortcuts import render
from .models import DailyTaskModel
from .serializers import DailyTaskSerializer
from rest_framework import viewsets
# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset=DailyTaskModel.objects.all()
    serializer_class=DailyTaskSerializer
    

