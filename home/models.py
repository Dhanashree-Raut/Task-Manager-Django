from django.db import models
from django.utils import timezone


# Create your models here.

class Task(models.Model):

    # Data about task 
    title = models.CharField(max_length=50)
    desc = models.TextField()
    duedate = models.DateField()
    timestamp =  models.DateTimeField(default=timezone.now) #editable entry date - to diplay 
    
    # State of the Task 
    is_complete = models.BooleanField(default=False)
    is_trash = models.BooleanField(default=False)

    # If nedede for futher use case like log entry for each user 
    created_at = models.DateTimeField(auto_now_add=True) # on created  - Non editable field to made sure correct entries are saved
    updated_at = models.DateTimeField(auto_now=True) # on each save / update -  Non editable field to made sure correct entries are saved