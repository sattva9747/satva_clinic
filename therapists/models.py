
from django.db import models


class Therapist(models.Model):

    name = models.CharField(max_length=100)

    photo = models.ImageField(upload_to="therapists/")

    qualification = models.CharField(max_length=200)

    designation = models.CharField(max_length=150)

    about = models.TextField()

    specialization = models.TextField()

    languages = models.CharField(max_length=255)

    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
