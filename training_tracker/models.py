from django.db import models

from training_tracker import run_history


# Create your models here.
class Runner(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    hours_goal = models.IntegerField()
    minutes_goal = models.IntegerField()
    seconds_goal = models.IntegerField()

    def __str__(self):
        return self.name

    def get_run_history(self):
        data = run_history.run_history(self.pk).get_data()
        return data

class Run(models.Model):
    runner_id = models.ForeignKey(Runner, on_delete=models.CASCADE)
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
    run_id = models.ForeignKey(Run, on_delete=models.CASCADE)
    mile_number = models.IntegerField()
    minutes = models.IntegerField(default=0)
    seconds = models.IntegerField(default=0)

    def __str__(self):
        return "ID: " + str(self.run.pk) + \
               ", Mile time: " + "{0}:{1}:{2}".format(self.hours, self.minutes, self.seconds)
