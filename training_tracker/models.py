from django.db import models

from training_tracker.custom_classes import run_history
from django.contrib.auth.models import User, UserManager, AbstractUser
from django.db.models.signals import post_save
import datetime as dt

from django.dispatch import receiver

# Represents a runner with name, age, and goal information
class Runner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    hours_goal = models.IntegerField(blank=True,null=True)
    minutes_goal = models.IntegerField(blank=True,null=True)
    seconds_goal = models.IntegerField(blank=True,null=True)
    #
    # # returns run history for this runner
    # def get_run_history(self):
    #     data = run_history.run_history(self.pk).get_data()
    #     return data
    def __str__(self):
        return str(self.user) + str(self.age) + str(self.hours_goal)\
               + str(self.minutes_goal) + str(self.seconds_goal)


# Represents a run. Runner_id associates this run with the runner who recorded it.
# run_number is relative to the runner (e.g. run_number = 1 is the first recorded run for this runner)
# record time and date information for the run
class Run(models.Model):
    runner = models.ForeignKey(Runner, on_delete=models.CASCADE)
    run_number = models.IntegerField()
    tot_distance = models.IntegerField(default=0)
    hours = models.IntegerField(blank=True,null=True)
    minutes = models.IntegerField(default=0)
    seconds = models.IntegerField(default=0)
    date = models.DateField(default=dt.date.today())

    # print string for a run
    def __str__(self):
        return "ID: " + str(self.pk) + \
               ", Miles: " + str(self.tot_distance) + \
               ", Time: " + "{0}:{1}:{2}".format(self.hours, self.minutes, self.seconds)

# Represents a mile. Run_id associates a mile to the run it was recorded for. Mile number is similar to run_number
# record minutes and seconds for the mile
class Mile(models.Model):
    run = models.ForeignKey(Run, on_delete=models.CASCADE)
    mile_number = models.IntegerField()
    minutes = models.IntegerField(default=0)
    seconds = models.IntegerField(default=0)

    # print string for mile
    def __str__(self):
        return "ID: " + str(self.run.pk) + \
               ", Mile time: " + "{0}:{1}".format(self.minutes, self.seconds)
