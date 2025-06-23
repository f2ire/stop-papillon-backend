from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models


### Create your models here.  

class User(AbstractUser):
    """
    Custom user model that extends Django's AbstractUser.
    This allows for additional fields and methods in the future.
    """
    pass

class Session(models.Model):
    """
    Represents a user session
    """
    user = models.ForeignKey("focus.User", on_delete=models.CASCADE, related_name="sessions")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    was_successful = models.BooleanField(default=False)
    distrations = models.PositiveIntegerField(default=0)

    def duration(self):
        if self.end_time:
            return self.end_time - self.start_time
        return 0
    
    def __str__(self):
        return f"Session for {self.user.username} ({self.start_time.date()})"
    

class Papillon(models.Model):
    user = models.ForeignKey("focus.User", on_delete=models.CASCADE, related_name="papillons")
    name = models.CharField(max_length=100)
    image_url = models.URLField()
    unlocked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.user.username}"
    