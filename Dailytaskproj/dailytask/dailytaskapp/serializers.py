from rest_framework import serializers
from .models import DailyTaskModel,User
class DailyTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=DailyTaskModel
        fields='__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'