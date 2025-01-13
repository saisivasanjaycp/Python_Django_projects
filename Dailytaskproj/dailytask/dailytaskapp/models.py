from django.db import models

class DailyTaskModel(models.Model):
    user=models.CharField(max_length=100)
    task=models.TextField()
    status=models.CharField(max_length=100)
    priority=models.BooleanField()

    def __str__(self):
        return f'{self.user}:{self.task}'
        
