from django.db import models

# Create your models here.
def author_image_file_path(instance,filename):
    return '/'.join([str(instance.first_name),filename])

class Authorcls(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    age=models.IntegerField()
    profile = models.ImageField(upload_to=author_image_file_path,null=True,blank=True)
    
    def __str__(self):
        return f'first_name:{self.first_name} last_name:{self.last_name} age:{self.age}'