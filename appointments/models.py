from django.db import models
from django.contrib.auth.models import User



class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    description = models.TextField()
    status = models.CharField(max_length=10, choices=[
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ], default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
