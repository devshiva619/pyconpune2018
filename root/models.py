from django.db import models


class Base(models.Model):
    """ Abstract model to save the common data """
    timestamp = models.DateTimeField(auto_now_add=True)
    year = models.PositiveIntegerField(default=2018)

    class Meta:
        abstract = True

class Speakers(models.Model):
    
    speaker_photo = models.ImageField(upload_to="speaker_photo/", blank=True, null=True)
    name = models.CharField(max_length=255)
    work_details = models.CharField(max_length=255)

    class Meta:
        abstract = True