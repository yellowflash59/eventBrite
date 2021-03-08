from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

# Create your models here.
class Event(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    event_name = models.CharField(max_length = 64,blank=False, null=False)
    data = models.TextField(blank=True, null=True)
    location = models.CharField(max_length = 250,blank = True,null = True)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    image = models.ImageField(upload_to='images',blank = True)
    is_liked = models.ManyToManyField(User, related_name = "events_likes",blank = True)

    def __str__(self):
        return self.event_name
