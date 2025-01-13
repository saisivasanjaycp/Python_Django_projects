from rest_framework import serializers
from .models import DailyTaskModel
class DailyTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=DailyTaskModel
        fields='__all__'