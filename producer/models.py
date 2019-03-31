from django.db import models

class Producer (models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    sex = models.CharField(max_length=20)
    dateOfBirth = models.DateField()
    bio = models.TextField()
    image = models.ImageField(upload_to='static/images/producers', default='../static/images/no_image.png')