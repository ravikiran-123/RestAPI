from django.db import models

# Create your models here.
class Banking(models.Model):
    Name=models.CharField(max_length=100,null=True)
    Email=models.EmailField()
    Address=models.TextField()



    def __str__(self):
        return (self.Name)