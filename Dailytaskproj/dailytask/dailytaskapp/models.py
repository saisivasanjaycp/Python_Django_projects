from django.db import models

class User(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name}:{self.last_name}'


class DailyTaskModel(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    task=models.TextField()
    status=models.CharField(max_length=100)
    priority=models.BooleanField()

    def __str__(self):
        return f'{self.user}:{self.task}'
        
