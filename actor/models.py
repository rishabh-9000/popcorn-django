from django.db import models

class Actor (models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    sex = models.CharField(max_length=20)
    dateOfBirth = models.DateField()
    bio = models.TextField()