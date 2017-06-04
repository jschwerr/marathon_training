from django.db import models
import django.utils.timezone as tz
import datetime

# Create your models here.
class Runner(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    hours_goal = models.IntegerField()
    minutes_goal = models.IntegerField()
    seconds_goal = models.IntegerField()

    def __str__(self):
        return self.name

class Run(models.Model):
    runner = models.ForeignKey(Runner, on_delete=models.CASCADE)
    run_number = models.IntegerField()
    tot_distance = models.IntegerField(default=0)
    hours = models.IntegerField(default=0)
    minutes = models.IntegerField(default=0)
    seconds = models.IntegerField(default=0)
    date = models.DateField()

    def __str__(self):
        return "ID: " + str(self.pk) + \
               ", Miles: " + str(self.tot_distance) + \
               ", Time: " + "{0}:{1}:{2}".format(self.hours, self.minutes, self.seconds)

class Mile(models.Model):
    run = models.ForeignKey(Run, on_delete=models.CASCADE)
    mile_number = models.IntegerField()
    minutes = models.IntegerField(default=0)
    seconds = models.IntegerField(default=0)

    def __str__(self):
        return "ID: " + str(self.run.pk) + \
               ", Mile time: " + "{0}:{1}:{2}".format(self.hours, self.minutes, self.seconds)
