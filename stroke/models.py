from django.db import models

# Create your models here.
class Questionnaire(models.Model):
    facial_droop = models.BooleanField()
    arm_drift = models.BooleanField()
    speech = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    onset_time = models.DateTimeField()
    additional_notes = models.TextField()
    owner = models.ForeignKey(
        'users.User', related_name='reviews', on_delete=models.CASCADE)

    def __str__(self):
        return self.owner

# Learned timezone confuguration from ---> https://www.sankalpjonna.com/learn-django/how-timezones-work-in-django