from django.db import models
from django.utils import timezone

class Source(models.Model):
    name = models.CharField(max_length = 30)
    latitude = models.FloatField()
    longitude = models.FloatField()
    desc = models.TextField()

class Dest(models.Model):
    name = models.CharField(max_length = 30)
    latitude = models.FloatField()
    longitude = models.FloatField()
    desc = models.TextField()
    is_accepting_donations = models.PositiveSmallIntegerField()
    requirement = models.PositiveSmallIntegerField()

class Resources(models.Model):
    rec_source = models.ForeignKey(Source, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    date_posted = models.DateTimeField(default=timezone.now)
    exp_date = models.DateTimeField()
    will_handle_delivery = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()
