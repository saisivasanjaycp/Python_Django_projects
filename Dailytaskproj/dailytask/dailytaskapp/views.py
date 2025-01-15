from django.shortcuts import render
from .models import DailyTaskModel,User
from .serializers import DailyTaskSerializer,UserSerializer
from rest_framework import viewsets
from django.views import View
# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset=DailyTaskModel.objects.all()
    serializer_class=DailyTaskSerializer
    
class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer


class TaskDisplayView(View):
    model=DailyTaskModel
    template_name = 'index.html'
    def get(self,request):
        context={'datas':self.model.objects.all()}
        return render(request,'dailytaskapp/index.html',context=context)
